


<div style="position: absolute; left: 50%; transform: translate(-50%); width: 35vw; height: 50vh; overflow-y: auto">
    <canvas id="mychartAccept" bind:this = {ctx} ></canvas>
</div>
<!-- <div id="firsturlsidebar"class="urlsidebar " class:opened={open}>
    <ol>
        {#each urlfilter as url}
       <li> <a style="font-size: 2vmin "target="_blank" href="{url}">
        {url}
        </a>
        {/each}
    </ol>
        </div> -->
<script>
import Chart from 'chart.js/auto';
import { afterUpdate, onMount } from 'svelte';
import { tick } from 'svelte';

import ChartDataLabels from 'chartjs-plugin-datalabels';
let urlfilter= []
let open = false; 
export let acceptselected

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

let ctx 
let myChartAccept

async function drawGraphAccept(){
    if(myChartAccept) myChartAccept.destroy();
let acceptdata = await fetchAccept()
let rejectdata = await fetchReject()
let acceptcount = $acceptselected.map(x=>Object.values(acceptdata).filter((i)=>i.includes(x.toLowerCase())).length)
let rejectcount = $acceptselected.map(x=>Object.values(rejectdata).filter((i)=>i.includes(x.toLowerCase())).length)

$acceptselected.map((x)=>console.log(x.toLowerCase()))
console.log(rejectcount)
let label = $acceptselected
console.log(acceptcount)

let average = acceptcount.map((x,i)=>Math.round(x/(x+rejectcount[i])*100))
console.log(average)
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
        maintainAspectRatio:  false, 
        responsive:  true,    
    plugins: {datalabels:{
        font: {
            size: 20
        }
    },title:{
        display: true, 
        text: 'Demographics - Most popular Major combination'
    },  scales:{
        y: {
           min: 0,
           max: 100,
        //    callback: function(average) {
        //        return average + "%"
        //    }
       
       scaleLabel: {
           display: true,
           labelString: "Percentage"
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
        let clickfilter = Object.keys(majorlist).filter(function(key) {
        return majorlist[key].toString() === label;
    });

   
    urlfilter = clickfilter.map(x=> {return url[x]})

    }
}

}

afterUpdate(drawGraphAccept)
</script>