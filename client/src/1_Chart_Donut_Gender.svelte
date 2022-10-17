

    <canvas id = 'myChart'  bind:this={ctx}/>

    <div id="firsturlsidebar"class="urlsidebar " class:opened={open} transition:fade>
    <ol>
        {#each urlfilter as url}
       <li> <a style="font-size: 2vmin "target="_blank" href="{url}">
        {url}
        </a>
        {/each}
    </ol>
        </div>



<script>

let urlfilter= [];  
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
export let majorchecked; 
export let majorselected
export let ecschecked; 
export let ecselected; 


async function fetchGender(){ 
    try{ 
        let countresponse = await fetch('https://dinhbaon.pythonanywhere.com/api/Gender');
        let genderlist = await countresponse.json(); 
        return genderlist
    }
    catch{ 
        return await fetchGender()
    }
}

async function fetchSAT(){ 
    try{ 
        let satdatajson = await fetch('https://dinhbaon.pythonanywhere.com/api/SAT')
        let satdata = await satdatajson.json()
        return satdata
    }
    catch{ 
        return await fetchSAT()
    }
}

async function fetchACT(){ 
    try{ 
        let actdatajson = await fetch('https://dinhbaon.pythonanywhere.com/api/ACT')
        let actdata = await actdatajson.json();
        return actdata 
    }
    catch{ 
        return await fetchACT()
    }
}
async function fetchAccept(){ 
    try{
        let acceptdatajson = await fetch('https://dinhbaon.pythonanywhere.com/api/Acceptances')
        let acceptdata  = await acceptdatajson.json(); 
        return acceptdata
    }
    catch{ 
        return await fetchAccept()
    }
}
async function fetchReject(){ 
    try{
        let rejectdatajson = await fetch('https://dinhbaon.pythonanywhere.com/api/Rejections')
        let rejectdata = await rejectdatajson.json()
        return rejectdata
    }
    catch{ 
        return await fetchReject()
    }
}
async function fetchMajor(){ 
    try{ 
        let majordatajson = await fetch('https://dinhbaon.pythonanywhere.com/api/Majors')
        let majordata = await  majordatajson.json()
        return majordata
    }
    catch{ 
        return await fetchMajor()
    }
}
async function fetchEcs(){ 
    try{ 
        let ecdatajson = await fetch('https://dinhbaon.pythonanywhere.com/api/Extracurriculars')
        let ecdata = await ecdatajson.json()
        return ecdata
    }
    catch{ 
        return await fetchEcs()
    }
}

var myChart
var ctx 


async function drawGraph(){
    if(myChart) myChart.destroy();

let genderCount = {}
let genderlist = await fetchGender();
    await tick()
    if(satchecked == true){ 
        let satdata = await fetchSAT();
        let satindex = []
        satindex = Object.entries(satdata).filter(([, i]) => i < $satuservalue[0] || i> $satuservalue[1] || i == "[]" ).map(([k]) => k);
        satindex.forEach(a=>delete genderlist[a])
}

    if(actchecked == true){ 
        let actdata = await fetchACT();
        let actindex = []
        actindex = Object.entries(actdata).filter(([, i]) => i < $actuservalue[0] || i> $actuservalue[1] || i == "[]" ).map(([k]) => k);
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
        Object.keys(genderlist).forEach((key) => majorindex.includes(key) || delete genderlist[key]) 
    }
    if (ecschecked == true){ 
        let ecdata = await fetchEcs(); 
        let ecindex = Object.entries(ecdata).filter(([, i]) => $ecselected.map(x=>x.toLowerCase()).every(r => i.includes(r))).map(([k]) => k)
        Object.keys(genderlist).forEach((key) => ecindex.includes(key) || delete genderlist[key]) 
    }
    

    


Object.values(genderlist).forEach(function (x) { genderCount[x] = (genderCount[x] || 0) + 1; });
let number  = Object.values(genderCount).reduce((a,b)=>a+b)




myChart = new Chart(ctx, {
    type: 'doughnut',
    data: { 
        labels: ['Male','Female','Other/LGBTQ+'],
        datasets: [{
            label: '# Gender ',
            data: [genderCount['Male'],genderCount['Female'],genderCount['Other/LGBTQ+']],
        backgroundColor: [
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 99, 132, 0.2)',  
                'rgba(255, 206, 86, 0.2)',
           
            ],
        }]
    },options: {
    plugins: {datalabels:{
        font: {
            size: function(context) {
                var width = context.chart.width;
                var size = Math.round(width / 32);

                return {
                    weight: 'bold',
                    size: size
                };
            }
        }
    },title:{
        display: true, 
        text: 'Demographics - Gender makeup'
    },    subtitle: {
                display: true,
                text: 'n=' + number
            }
}
    }
    , plugins: [ChartDataLabels]} 
    
);
myChart.canvas.onclick = clickHandler
async function clickHandler(click){ 

    open = true; 
    let urljson = await fetch('https://dinhbaon.pythonanywhere.com/api/URL')
    let url = await urljson.json(); 
    const points = myChart.getElementsAtEventForMode(click, 'nearest', {intersect: true}, true)
    if (points[0]){
        const index = points[0].index; 
        const label = myChart.data.labels[index];
        let clickfilter = Object.keys(genderlist).filter(function(key) {
        return genderlist[key] === label;
    });
    
    urlfilter = clickfilter.map(x=> {return url[x]})

    }
}

}




afterUpdate(drawGraph)
  </script>
  
<style> 
.urlsidebar{ 
    float: right; 
    width: 20vw; 
    overflow-y: auto; 
    position: relative; 
    height: 100%; 
    left: 91%;
    transform: translateY(-100%); 
    transition: 2s; 
    visibility: hidden; 
}
.opened{ 
    visibility: visible 

}



</style>