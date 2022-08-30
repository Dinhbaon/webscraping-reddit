
<canvas id = 'myChart'  bind:this={ctx}/>


<script>
import { onMount, afterUpdate } from 'svelte';
import Chart from 'chart.js/auto';
import { tick } from 'svelte';
import ChartDataLabels from 'chartjs-plugin-datalabels';
export let satchecked;
export let satuservalue; 
export let actchecked; 
export let actuservalue;
export let acceptselected; 
export let acceptchecked; 
export let rejectselected; 
export let rejectchecked; 
export let majorchecked; 
export let majorselected

async function fetchGender(){ 
    let countresponse = await fetch(`http://127.0.0.1:5000/api/Gender`);
    let genderlist = await countresponse.json(); 
    return genderlist
}

async function fetchSAT(){ 
    let satdatajson = await fetch(`http://127.0.0.1:5000/api/SAT`)
    let satdata = await satdatajson.json()
    return satdata
}

async function fetchACT(){ 
    let actdatajson = await fetch('http://127.0.0.1:5000/api/ACT')
    let actdata = await actdatajson.json();
    return actdata 
}
async function fetchAccept(){ 
    let acceptdatajson = await fetch('http://127.0.0.1:5000/api/Acceptances')
    let acceptdata  = await acceptdatajson.json(); 
    return acceptdata
}
async function fetchReject(){ 
    let rejectdatajson = await fetch('http://127.0.0.1:5000/api/Rejections')
    let rejectdata = await rejectdatajson.json()
    return rejectdata
}
async function fetchMajor(){ 
    let majordatajson = await fetch('http://127.0.0.1:5000/api/Majors')
    let majordata = await  majordatajson.json()
    return majordata
}

let myChart = null
let ctx


onMount(
    async function drawGraph(){
 ctx = document.getElementById('myChart');
let genderCount = {}
console.log(myChart)
let genderlist = await fetchGender();
    if(myChart != null) {
        
        await tick()
    if(satchecked == true){ 
        let satdata = await fetchSAT();
        let satindex = []
        satindex = Object.entries(satdata).filter(([, i]) => i <= $satuservalue[0] || i>= $satuservalue[1] || i == "[]" ).map(([k]) => k);
        satindex.forEach(a=>delete genderlist[a])
}

    if(actchecked == true){ 
        let actdata = await fetchACT();
        let actindex = []
        actindex = Object.entries(actdata).filter(([, i]) => i <= $actuservalue[0] || i>= $actuservalue[1] || i == "[]" ).map(([k]) => k);
        actindex.forEach(a=>delete genderlist[a])
}
    if( acceptchecked == true){ 
        let acceptdata = await fetchAccept(); 
        let acceptindex = Object.entries(acceptdata).filter(([, i]) => $acceptselected.map(x=>x.toLowerCase()).every(r => i.includes(r))).map(([k]) => k)
        Object.keys(genderlist).forEach((key) => acceptindex.includes(key) || delete genderlist[key])   
    }
    if (rejectchecked == true){ 
        let rejectdata = await fetchReject(); 
        let rejectindex = Object.entries(rejectdata).filter(([, i]) => $rejectselected.map(x=>x.toLowerCase()).every(r => i.includes(r))).map(([k]) => k)
        Object.keys(genderlist).forEach((key) => rejectindex.includes(key) || delete genderlist[key]) 
    }
    if (majorchecked == true){ 
        let majordata = await fetchMajor(); 
        let majorindex = Object.entries(majordata).filter(([, i]) => $majorselected.map(x=>x.toLowerCase()).every(r => i.includes(r))).map(([k]) => k)
        console.log(majorindex)
        Object.keys(genderlist).forEach((key) => majorindex.includes(key) || delete genderlist[key]) 
    }

    let data = Object.values(genderlist).forEach(function (x) { genderCount[x] = (genderCount[x] || 0) + 1; });
    myChart.data.datasets.data = data
    myChart.update();
}else{
myChart = new Chart(ctx, {
    type: 'doughnut',
    data: { 
        labels: Object.keys(await genderCount),
        datasets: [{
            label: '# of Votes',
            data: Object.values(await genderlist),
        backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
           
            ],
        }]
    },options: {
    plugins: {datalabels:{
        font: {
            size: 20
        }
    }
}
    }
    , plugins: [ChartDataLabels]} 
    
);}});


  </script>
