<div style="position: absolute; left: 50%; transform: translate(-50%); overflow-y: auto" class="chartcontainer">
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
export let genderchecked
export let genderselected
export let ecschecked
export let ecselected

async function fetchAccept(){
    try{
        let acceptdatajson = await fetch('https://dinhbaon.pythonanywhere.com/api/Acceptances')
        let acceptdata = acceptdatajson.json()
        return acceptdata
    }
    catch{ 
        return await fetchAccept()
    }
}
async function fetchReject(){ 
    try{
        let rejectdatajson = await fetch('https://dinhbaon.pythonanywhere.com/api/Rejections') 
        let rejectdata = rejectdatajson.json()
        return rejectdata 
    }
    catch{ 
        return await fetchReject()
    }
}

async function fetchSAT(){ 
    try{
        let satdatajson = await fetch(`https://dinhbaon.pythonanywhere.com/api/SAT`)
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
        return await fetchSAT()
    }
}
async function fetchMajor(){ 
    try{ 
        let majordatajson = await fetch('https://dinhbaon.pythonanywhere.com/api/Majors')
        let majordata = await majordatajson.json()
        return majordata
    }
    catch{ 
        return await fetchMajor()
    }
}
async function fetchGender(){
    try{ 
        let genderdatajson = await fetch('https://dinhbaon.pythonanywhere.com/api/Gender')
        let genderdata = await genderdatajson.json()
        return genderdata
    }
    catch{ 
        return await fetchGender()
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
    if(genderchecked == true){ 
        let genderdata = await fetchGender(); 
        let genderindex = Object.entries(genderdata).filter(([, i]) => $genderselected == i ).map(([k]) => k)
        Object.keys(acceptdata).forEach((key) => genderindex.includes(key) || delete acceptdata[key])  
        Object.keys(rejectdata).forEach((key) => genderindex.includes(key) || delete rejectdata[key]) 

            }
    if(ecschecked == true){ 
        let ecdata = await fetchEcs(); 
        let ecindex = Object.entries(ecdata).filter(([, i]) => $ecselected.map(x=>x.toLowerCase()).every(r => i.includes(r))).map(([k]) => k)
        Object.keys(acceptdata).forEach((key) => ecindex.includes(key) || delete acceptdata[key])  
        Object.keys(rejectdata).forEach((key) => ecindex.includes(key) || delete rejectdata[key]) 

            }

acceptcount = $acceptselected.map(x=>Object.values(acceptdata).filter((i)=>i.includes(x.toLowerCase())).length)
rejectcount = $acceptselected.map(x=>Object.values(rejectdata).filter((i)=>i.includes(x.toLowerCase())).length)


let label = $acceptselected


let acceptancerate = acceptcount.map((x,i)=>Math.round(x/(x+rejectcount[i])*100))
let total  = acceptcount.map((x,i)=>x+rejectcount[i])
myChartAccept = new Chart(ctx, {
    type: 'bar',
    data: { 
        labels: label,
        datasets: [{
            label: 'Acceptance rate %',
            data: acceptancerate,
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
            afterLabel: (tooltipItems)=> {console.log(tooltipItems); return 'Total: '+total[tooltipItems.dataIndex]+ '\n# of Acceptances: ' +acceptcount[tooltipItems.dataIndex]+ '\n# of Rejections: '+rejectcount[tooltipItems.dataIndex]}
            
          }

        },
        datalabels:{
            font: 
                function(ctx) {
                var width = ctx.chart.width;
                var size = Math.round(width / 30);

                return {
                    size: size
                };
            }
            
        },title:{
            display: true, 
            text: 'Acceptance rate by university'
        },    
},
        scales:{
                y: {
                    min: 0,
                    max: 100,
                    callbacks: function(acceptancerate) {
               return acceptancerate + "%"
           },
           
        maintainAspectRatio:  false, 
        responsive:  true,    

    }  
}

        }
    , plugins: [ChartDataLabels]} 
    
);


myChartAccept.canvas.onclick = clickHandler
async function clickHandler(click){ 
    open = true; 
    let urljson = await fetch('https://dinhbaon.pythonanywhere.com/api/URL')
    let url = await urljson.json(); 
    const points = myChartAccept.getElementsAtEventForMode(click, 'nearest', {intersect: true}, true)
    if (points[0]){
        const index = points[0].index; 
        const label = myChartAccept.data.labels[index];
        let clickfilter = Object.keys(acceptdata).filter(function(key) {
        return acceptdata[key].includes(label.toLowerCase());
    });

    urlfilter = clickfilter.map(x=> {return url[x]})

    }
}

}

afterUpdate(drawGraphAccept)
</script>

<style> 
    .urlsidebar{ 
        float: right; 
        width: 20vw; 
        overflow-y: auto; 
        position: relative; 
        height: 100%; 
        left: 100%;
        position: absolute; 
        transition: 2s; 
        visibility: hidden; 
    }
    .opened{ 
        visibility: visible ;
    
   
    }
    .chartcontainer{ 
        width: 35vw; 
        height: 50vh;
    }
    @media (max-width:640px){ 
    .chartcontainer{ 
        width: 90vw; 
        height: auto;
    }
    }
    
    
    
    </style>