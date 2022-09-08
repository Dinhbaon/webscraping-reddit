<div style="position: absolute; left: 50%; transform: translateX(-50%); width: 35vw; height: 70vh; display:block; overflow-y: auto">
<div style="position: absolute; left: 50%; transform: translateX(-50%); width: 35vw; height: 1000vh; display:block; overflow-y: auto">
    <canvas id = 'myChartMajor' style="width: 100%; height: 100%"    bind:this={ctx}/>
</div>
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
let urlfilter = []
let open = false; 
import { onMount, afterUpdate } from 'svelte';
import Chart from 'chart.js/auto';
import { tick } from 'svelte';
import ChartDataLabels from 'chartjs-plugin-datalabels';
import { writable } from 'svelte/store';
import {fade} from 'svelte/transition'
export let satchecked;
export let satuservalue; 
export let actchecked; 
export let actuservalue;
export let acceptselected; 
export let acceptchecked; 
export let rejectselected; 
export let rejectchecked; 
export let genderchecked; 
export let genderselected; 
export let ecschecked; 
export let ecselected; 

async function fetchMajor(){ 
    let majordatajson = await fetch('http://127.0.0.1:5000/api/Majors')
    let majordata = await majordatajson.json()
    return majordata 
}
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
async function fetchEcs(){ 
    let ecdatajson = await fetch('http://127.0.0.1:5000/api/Extracurriculars')
    let ecdata = await ecdatajson.json()
    return ecdata
}

var ctx
var myChartMajor

async function drawGraphMajor(){
    if(myChartMajor) myChartMajor.destroy();

let majorCount = {}
let majorlist = await fetchMajor();
    await tick()
    if(satchecked == true){ 
        let satdata = await fetchSAT();
        let satindex = []
        satindex = Object.entries(satdata).filter(([, i]) => i < $satuservalue[0] || i> $satuservalue[1] || i == "[]" ).map(([k]) => k);
        satindex.forEach(a=>delete majorlist[a])
}

    if(actchecked == true){ 
        let actdata = await fetchACT();
        let actindex = []
        actindex = Object.entries(actdata).filter(([, i]) => i < $actuservalue[0] || i> $actuservalue[1] || i == "[]" ).map(([k]) => k);
        actindex.forEach(a=>delete majorlist[a])
}
    if( acceptchecked == true){ 
        let acceptdata = await fetchAccept(); 
        let acceptindex = Object.entries(acceptdata).filter(([, i]) => $acceptselected.map(x=>x.toLowerCase()).every(r => i.includes(r))).map(([k]) => k)
        Object.keys(majorlist).forEach((key) => acceptindex.includes(key) || delete majorlist[key])   
    }
    if (rejectchecked == true){ 
        let rejectdata = await fetchReject(); 
        let rejectindex = Object.entries(rejectdata).filter(([, i]) => $rejectselected.map(x=>x.toLowerCase()).every(r => i.includes(r))).map(([k]) => k)
        Object.keys(majorlist).forEach((key) => rejectindex.includes(key) || delete majorlist[key]) 
    }
    if (genderchecked == true){ 
        let genderdata = await fetchGender(); 
        let genderindex = Object.entries(genderdata).filter(([, i]) => $genderselected == i ).map(([k]) => k)
        Object.keys(majorlist).forEach((key) => genderindex.includes(key) || delete majorlist[key]) 
    }
    if (ecschecked == true){ 
        let ecdata = await fetchEcs(); 
        let ecindex = Object.entries(ecdata).filter(([, i]) => $ecselected.map(x=>x.toLowerCase()).every(r => i.includes(r))).map(([k]) => k)
        Object.keys(majorlist).forEach((key) => ecindex.includes(key) || delete majorlist[key]) 
    }

    


Object.values(majorlist).forEach(function (x) { majorCount[x] = (majorCount[x] || 0) + 1; });
let number  = Object.values(majorCount).reduce((a,b)=>a+b)

let sortedmajorcount = Object.fromEntries(
    Object.entries(majorCount).sort(([,a],[,b]) => b-a))

myChartMajor = new Chart(ctx, {
    type: 'bar',
    data: { 
        labels: Object.keys(sortedmajorcount),
        datasets: [{
            label: '# Gender ',
            data: Object.values(sortedmajorcount),
        backgroundColor: [
                'rgba(255, 99, 132, 0.2)',  
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
           
            ],
        }]
    },options: { 
        maintainAspectRatio:  false, 
        responsive:  true,    
        indexAxis: 'y',
    plugins: {datalabels:{
        font: {
            size: 20
        }
    },title:{
        display: true, 
        text: 'Demographics - Most popular Major combination'
    },    subtitle: {
                display: true,
                text: 'n=' + number
            }
}
    }
    , plugins: [ChartDataLabels]} 
    
);
myChartMajor.canvas.onclick = clickHandler
async function clickHandler(click){ 
    open = true; 
    let urljson = await fetch('http://127.0.0.1:5000/api/URL')
    let url = await urljson.json(); 
    const points = myChartMajor.getElementsAtEventForMode(click, 'nearest', {intersect: true}, true)
    if (points[0]){
        const index = points[0].index; 
        const label = myChartMajor.data.labels[index];
        let clickfilter = Object.keys(majorlist).filter(function(key) {
        return majorlist[key].toString() === label;
    });

   
    urlfilter = clickfilter.map(x=> {return url[x]})

    }
}

}




afterUpdate(drawGraphMajor)


</script>

<style>

.urlsidebar{ 
    float: right; 
    width: 20vw; 
    overflow-y: auto; 
    position: relative; 
    height: 50vh; 
    transition: 2s; 
    visibility: hidden; 

}
.opened{ 
    visibility: visible 

}
</style> 