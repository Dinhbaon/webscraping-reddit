


<div style="position: absolute; left: 50%; transform: translate(-50%); width: 35vw; height: 50vh; ">
    <canvas id="mychartAveragescores" bind:this = {ctx} ></canvas>
</div>
<div id="firsturlsidebar"class="urlsidebar " class:opened={open}>
    <ol>
        {#each urlfilter as url}
       <li> <a style="font-size: 2vmin "target="_blank" href="{url}">
        {url}
        </a>
        {/each}
    </ol>
        </div>
<script>
import Chart from 'chart.js/auto';
import { afterUpdate, onMount } from 'svelte';
import { tick } from 'svelte';

import ChartDataLabels from 'chartjs-plugin-datalabels';
import { object_without_properties } from 'svelte/internal';
let urlfilter= []
let open = false; 
export let acceptselected
export  let satchecked
export let actchecked
export let majorselected
export let majorchecked
export let ecschecked
export let ecselected; 
export let genderchecked; 
export let genderselected; 

async function fetchAccept(){
    let acceptdatajson = await fetch('http://127.0.0.1:5000/api/Acceptances')
    let acceptdata = acceptdatajson.json()
    return acceptdata
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
async function fetchMajor(){ 
    let majordatajson = await fetch('http://127.0.0.1:5000/api/Majors')
    let majordata = await majordatajson.json()
    return majordata
}
async function fetchEcs(){ 
    let ecdatajson = await fetch('http://127.0.0.1:5000/api/Extracurriculars')
    let ecdata = await ecdatajson.json()
    return ecdata
}
async function fetchGender(){ 
    let genderdatajson = await fetch('http://127.0.0.1:5000/api/Gender')
    let genderdata = await genderdatajson.json()
    return genderdata
}

let ctx 
let myChartAveragescores

async function drawGraphAveragescore(){
    if(myChartAveragescores) myChartAveragescores.destroy();
let average = [] 
let acceptdata = await fetchAccept();
let total = []
    if(satchecked == true){ 
        let satdata = await fetchSAT();
        if (majorchecked == true){ 
            let majordata = await fetchMajor(); 
            let majorindex = Object.entries(majordata).filter(([, i]) => $majorselected.map(x=>x.toLowerCase()).every(r => i.includes(r))).map(([k]) => k)
            Object.keys(satdata).forEach((key) => majorindex.includes(key) || delete satdata[key]) 
            Object.keys(acceptdata).forEach((key) => majorindex.includes(key) || delete acceptdata[key])
        }
        if (ecschecked == true){ 
            let ecdata = await fetchEcs(); 
            let ecindex = Object.entries(ecdata).filter(([, i]) => $ecselected.map(x=>x.toLowerCase()).every(r => i.includes(r))).map(([k]) => k)
            Object.keys(satdata).forEach((key) => ecindex.includes(key) || delete satdata[key]) 
            Object.keys(acceptdata).forEach((key) => ecindex.includes(key) || delete acceptdata[key])
    }
        if(genderchecked == true){ 
            let genderdata = await fetchGender(); 
            let genderindex = Object.entries(genderdata).filter(([, i]) => $genderselected == i ).map(([k]) => k)
            Object.keys(satdata).forEach((key) => genderindex.includes(key) || delete satdata[key])  
            Object.keys(acceptdata).forEach((key) => genderindex.includes(key) || delete acceptdata[key])  

            }
        let satdatafiltered = $acceptselected.map(x=>Object.entries(acceptdata).filter(([k,i])=>i.includes(x.toLowerCase()))).map(a=>a.map(b=> satdata[b[0]]).filter( Number ))
        console.log(satdatafiltered)
        average = satdatafiltered.map((x,i)=>Math.round(x.reduce((a,b)=>parseInt(a)+parseInt(b),0)/(satdatafiltered[i].length)*10)/10)
        console.log(satdatafiltered.map((x,i)=>x.reduce((a,b)=>a+b,0)))
        let satindex = []
        satindex = Object.entries(satdata).filter(([, i]) => i == "[]" ).map(([k]) => k);
        satindex.forEach(a=>delete acceptdata[a])
        total = Object.values(satdatafiltered).map((x,i)=>satdatafiltered[i].length)
    }

    if(actchecked == true){ 
        let actdata = await fetchACT();
        if (majorchecked == true){ 
            let majordata = await fetchMajor(); 
            let majorindex = Object.entries(majordata).filter(([, i]) => $majorselected.map(x=>x.toLowerCase()).every(r => i.includes(r))).map(([k]) => k)
            Object.keys(actdata).forEach((key) => majorindex.includes(key) || delete actdata[key]) 
            Object.keys(acceptdata).forEach((key) => majorindex.includes(key) || delete acceptdata[key])
        }
        if (ecschecked == true){ 
            let ecdata = await fetchEcs(); 
            let ecindex = Object.entries(ecdata).filter(([, i]) => $ecselected.map(x=>x.toLowerCase()).every(r => i.includes(r))).map(([k]) => k)
            Object.keys(actdata).forEach((key) => ecindex.includes(key) || delete actdata[key]) 
            Object.keys(acceptdata).forEach((key) => ecindex.includes(key) || delete acceptdata[key])
    }
        if(genderchecked == true){ 
            let genderdata = await fetchGender(); 
            let genderindex = Object.entries(genderdata).filter(([, i]) => $genderselected == i ).map(([k]) => k)
            Object.keys(actdata).forEach((key) => genderindex.includes(key) || delete actdata[key])  
            Object.keys(acceptdata).forEach((key) => genderindex.includes(key) || delete acceptdata[key])

            }
        let actdatafiltered = $acceptselected.map(x=>Object.entries(acceptdata).filter(([k,i])=>i.includes(x.toLowerCase()))).map(a=>a.map(b=> actdata[b[0]]).filter( Number ))
        average = actdatafiltered.map((x,i)=>Math.round(x.reduce((a,b)=>parseInt(a)+parseInt(b),0)/(actdatafiltered[i].length)*10)/10)
        let actindex = []
        actindex = Object.entries(actdata).filter(([, i]) => i == "[]" ).map(([k]) => k);
        actindex.forEach(a=>delete acceptdata[a])
        total = Object.values(actdatafiltered).map((x,i)=>actdatafiltered[i].length)
    }


console.log(average)



let label = $acceptselected


// let acceptancerate = acceptcount.map((x,i)=>Math.round(x/(x+rejectcount[i])*100))
// let total  = acceptcount.map((x,i)=>x+rejectcount[i])
myChartAveragescores = new Chart(ctx, {
    type: 'bar',
    data: { 
        labels: label,
        datasets: [{
            label: 'Test scores',
            data: average,
        backgroundColor: [
                'rgba(255, 99, 132, 0.2)',  
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
           
            ],
        }]
    },options: { 
        plugins: {
        tooltip:{ 
          callbacks:{ 
            afterLabel: (tooltipItems)=> {console.log(tooltipItems); return 'n: '+total[tooltipItems.dataIndex]}
            
          }

        },
        datalabels:{
            font: {
                size: 20
            }
        },title:{
            display: true, 
            text: 'Average test scores by university'
        },    
},
        scales:{
        //         y: {
        //             min: 0,
        //             max: 100,
        //             callbacks: function(acceptancerate) {
        //        return acceptancerate + "%"
        //    },
           
    //     maintainAspectRatio:  false, 
    //     responsive:  true,    

    // }  
}

        }
    , plugins: [ChartDataLabels]} 
    
);


myChartAveragescores.canvas.onclick = clickHandler
async function clickHandler(click){ 
    open = true; 
    let urljson = await fetch('http://127.0.0.1:5000/api/URL')
    let url = await urljson.json(); 
    const points = myChartAveragescores.getElementsAtEventForMode(click, 'nearest', {intersect: true}, true)
    if (points[0]){
        const index = points[0].index; 
        const label = myChartAveragescores.data.labels[index];
        console.log(label)
        let clickfilter = Object.keys(acceptdata).filter(function(key) {
        return acceptdata[key].includes(label.toLowerCase());
    });

   console.log(clickfilter)
    urlfilter = clickfilter.map(x=> {return url[x]})

    }
}

}

afterUpdate(drawGraphAveragescore)
</script>

<style> 
    .urlsidebar{ 
        float: right; 
        width: 20vw; 
        overflow-y: auto;  
        height: 100%; 
        left: 295%;
        position: absolute; 
        transition: 2s; 
        visibility: hidden; 
    }
    .opened{ 
        visibility: visible 
    
    }
    
    
    
    </style>