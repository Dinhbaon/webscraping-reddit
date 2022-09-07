


<div style="position: absolute; left: 50%; transform: translate(-50%); width: 35vw; height: 50vh; overflow-y: auto">
    <canvas id="mychartAccept" bind:this = {ctx} ></canvas>
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
let urlfilter= []
let open = false; 
export let acceptselected
export  let satchecked
export let actchecked
export let satuservalue
export let actuservalue
export let majorselected
export let majorchecked

async function fetchAccept(){
    let acceptdatajson = await fetch('http://127.0.0.1:5000/api/Acceptances')
    let acceptdata = acceptdatajson.json()
    return acceptdata
}
async function fetchReject(){ 
    let rejectdatajson = await fetch('http://127.0.0.1:5000/api/Rejections') 
    let rejectdata = rejectdatajson.json()
    return rejectdata 
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

let ctx 
let myChartAccept

async function drawGraphAccept(){
    if(myChartAccept) myChartAccept.destroy();
let acceptcount = []
let rejectcount = []
let acceptdata = await fetchAccept()
let rejectdata = await fetchReject()

if(satchecked == true){ 
        let satdata = await fetchSAT();
        let satindex = []
        satindex = Object.entries(satdata).filter(([, i]) => i < $satuservalue[0] || i> $satuservalue[1] || i == "[]" ).map(([k]) => k);
        satindex.forEach(a=>delete acceptdata[a])
        satindex.forEach(a=>delete  rejectdata[a])
}

    if(actchecked == true){ 
        let actdata = await fetchACT();
        let actindex = []
        actindex = Object.entries(actdata).filter(([, i]) => i < $actuservalue[0] || i> $actuservalue[1] || i == "[]" ).map(([k]) => k);
        actindex.forEach(a=>delete acceptdata[a])
        actindex.forEach(a=>delete rejectdata[a])
}
    if(majorchecked == true){ 
        let majordata = await fetchMajor(); 
        let majorindex = Object.entries(majordata).filter(([, i]) => $majorselected.map(x=>x.toLowerCase()).every(r => i.includes(r))).map(([k]) => k)
        Object.keys(acceptdata).forEach((key) => majorindex.includes(key) || delete acceptdata[key])  
        Object.keys(rejectdata).forEach((key) => majorindex.includes(key) || delete rejectdata[key])  
    }

acceptcount = $acceptselected.map(x=>Object.values(acceptdata).filter((i)=>i.includes(x.toLowerCase())).length)
rejectcount = $acceptselected.map(x=>Object.values(rejectdata).filter((i)=>i.includes(x.toLowerCase())).length)


let label = $acceptselected


let average = acceptcount.map((x,i)=>Math.round(x/(x+rejectcount[i])*100))

myChartAccept = new Chart(ctx, {
    type: 'bar',
    data: { 
        labels: label,
        datasets: [{
            label: '# Acceptance rate ',
            data: average,
        backgroundColor: [
                'rgba(255, 99, 132, 0.2)',  
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
           
            ],
        }]
    },options: { 
        scales:{
                y: {
                    min: 0,
                    max: 100,
  
        maintainAspectRatio:  false, 
        responsive:  true,    
    plugins: {datalabels:{
        font: {
            size: 20
        }
    },title:{
        display: true, 
        text: 'Demographics - Most popular Major combination'
    }

       

       }
    }  
}
    }
    , plugins: [ChartDataLabels]} 
    
);
myChartAccept.canvas.onclick = clickHandler
async function clickHandler(click){ 
    open = true; 
    let urljson = await fetch('http://127.0.0.1:5000/api/URL')
    let url = await urljson.json(); 
    const points = myChartAccept.getElementsAtEventForMode(click, 'nearest', {intersect: true}, true)
    if (points[0]){
        const index = points[0].index; 
        const label = myChartAccept.data.labels[index];
        let clickfilter = Object.keys(acceptdata).filter(function(key) {
        return acceptdata[key].toString() === label;
    });

   
    urlfilter = clickfilter.map(x=> {return url[x]})

    }
}

}

afterUpdate(drawGraphAccept)
</script>