{#await fetchSAT()}
<div style="margin: auto;transform: translate(100%,0%);" >
    <img src="loadingwheel.gif" alt=loadingwheel style="height: 20vh;">
</div>
{:then}
{#if satchecked == true||actchecked == true}
<div style="justify-content: center;  transform: translateX(-50%); position:absolute; left:50%" id="chartcontainer"> 
    <canvas id="histogram" bind:this = {ctx} ></canvas></div>
{:else}
<div style="text-align: center; font-size: 3rem;     position: absolute;left: 50%;transform: translateX(-50%);margin: 0;top: 40%;">Please choose an x-axis</div>
{/if}
{/await}


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
let open = false;  
let urlfilter= []; 
import Chart from 'chart.js/auto';
import { afterUpdate, onMount } from 'svelte';
import { tick } from 'svelte';
import {fade} from 'svelte/transition'  
export let satchecked;
export let actchecked ;
export let majorchecked;
export let acceptchecked; 
export let rejectchecked
export let genderchecked; 
export let satuservalue;
export let actuservalue;
export let majorselected
export let acceptselected; 
export let rejectselected; 
export let genderselected; 
export let ecschecked; 
export let ecselected;
let ctx
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
        return await fetchACT()
    }

}

async function fetchAccept() { 
    try{
        let acceptdatajson = await fetch('https://dinhbaon.pythonanywhere.com/api/Acceptances')
        let acceptdata = await acceptdatajson.json();
        return acceptdata 
    }
    catch{ 
        return await fetchAccept()
    }
}
async function fetchMajor(){ 
    try{
        let majordatajson = await fetch('https://dinhbaon.pythonanywhere.com/api/Majors')
        let majordata = await majordatajson.json()
        return majordata
    }
    catch{ 
        return await fetchMajor
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
function steprange(start, end, step) {
  const len = Math.floor((end - start) / step) + 1
  return Array(len).fill().map((_, idx) => start + (idx * step))
}

let histogram;
async function drawHistogram(){ 
    if(histogram) histogram.destroy();
        await tick()
        let filtered = {};
        let scoredata = {};
        let count = {}
        let label
        if (satchecked == true){ 
            scoredata = await fetchSAT() 
            label = steprange($satuservalue[0],$satuservalue[1],10)
            if(acceptchecked == true){ 
                let acceptdata = await fetchAccept(); 
                let acceptindex = Object.entries(acceptdata).filter(([, i]) => $acceptselected.map(x=>x.toLowerCase()).every(r => i.includes(r))).map(([k]) => k)
                Object.keys(scoredata).forEach((key) => acceptindex.includes(key) || delete scoredata[key])
    
             }
             if(majorchecked == true){ 
                let majordata = await fetchMajor(); 
                let majorindex = Object.entries(majordata).filter(([, i]) => $majorselected.map(x=>x.toLowerCase()).every(r => i.includes(r))).map(([k]) => k)
                Object.keys(scoredata).forEach((key) => majorindex.includes(key) || delete scoredata[key])  
            }
            if(genderchecked == true){ 
                let genderdata = await fetchGender(); 
                let genderindex = Object.entries(genderdata).filter(([, i]) => $genderselected == i ).map(([k]) => k)
                Object.keys(scoredata).forEach((key) => genderindex.includes(key) || delete scoredata[key])  

            }
            if(rejectchecked == true){ 
                let rejectdata = await fetchReject(); 
                let rejectindex = Object.entries(rejectdata).filter(([, i]) => $rejectselected.map(x=>x.toLowerCase()).every(r => i.includes(r))).map(([k]) => k)
                Object.keys(scoredata).forEach((key) => rejectindex.includes(key) || delete scoredata[key]) 
            }
            if (ecschecked == true){ 
                let ecdata = await fetchEcs(); 
                let ecindex = Object.entries(ecdata).filter(([, i]) => $ecselected.map(x=>x.toLowerCase()).every(r => i.includes(r))).map(([k]) => k)
                Object.keys(scoredata).forEach((key) => ecindex.includes(key) || delete scoredata[key]) 
    }
            Object.values(scoredata).forEach(function (x) { count[x] = (count[x] || 0) + 1; });

        }   
        if (actchecked == true){ 
            scoredata = await fetchACT(); 
            label = steprange($actuservalue[0],$actuservalue[1],1)
            if(acceptchecked == true){ 
                let acceptdata = await fetchAccept(); 
                let acceptindex = Object.entries(acceptdata).filter(([, i]) => $acceptselected.map(x=>x.toLowerCase()).every(r => i.includes(r))).map(([k]) => k)
                Object.keys(scoredata).forEach((key) => acceptindex.includes(key) || delete scoredata[key])  
            }
            if(majorchecked == true){ 
                let majordata = await fetchMajor(); 
                let majorindex = Object.entries(majordata).filter(([, i]) => $majorselected.map(x=>x.toLowerCase()).every(r => i.includes(r))).map(([k]) => k)
                Object.keys(scoredata).forEach((key) => majorindex.includes(key) || delete scoredata[key])  
            }
            if(genderchecked == true){ 
                let genderdata = await fetchGender(); 
                let genderindex = Object.entries(genderdata).filter(([, i]) => $genderselected == i).map(([k]) => k)
                Object.keys(scoredata).forEach((key) => genderindex.includes(key) || delete scoredata[key])  

            }
            if(rejectchecked == true){ 
                let rejectdata = await fetchReject(); 
                let rejectindex = Object.entries(rejectdata).filter(([, i]) => $rejectselected.map(x=>x.toLowerCase()).every(r => i.includes(r))).map(([k]) => k)
                Object.keys(scoredata).forEach((key) => rejectindex.includes(key) || delete scoredata[key]) 
            }
            if (ecschecked == true){ 
                let ecdata = await fetchEcs(); 
                let ecindex = Object.entries(ecdata).filter(([, i]) => $ecselected.map(x=>x.toLowerCase()).every(r => i.includes(r))).map(([k]) => k)
                Object.keys(scoredata).forEach((key) => ecindex.includes(key) || delete scoredata[key]) 
    }
        Object.values(scoredata).forEach(function (x) { count[x] = (count[x] || 0) + 1; });
        
        // count = Object.fromEntries(
        // Object.entries(count).map(([k, v]) => [k.slice(0,-1), v]))

        }


        Object.keys(count).forEach(x =>  x=1)
        let labelzero = label.map(key => ({[key]:0 }))
        filtered = Object.assign({},...labelzero)
        Object.keys(filtered).forEach(key => {
                        if (key in count) {
                        filtered[key] = count[key];
                        }
                    });
        let scorecount = {}
        Object.values(scoredata).forEach(function (x) { scorecount[x] = (scorecount[x] || 0) + 1; });
        let number = Object.values(scorecount).slice(0,-1).reduce((a,b)=>a+b)
        let average = (Object.entries(scorecount).map(x=>parseInt(x[0])*x[1]).slice(0,-1).reduce((a,b)=>a+b))/number
histogram = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: label,
        datasets: [{
            label: 'Frequency of test scores',
            data: Object.values(filtered),
            backgroundColor: [

                'rgba(54, 162, 235, 0.2)',

            ],
            borderColor: [

                'rgba(54, 162, 235, 1)',

            ],
            borderWidth: 1,
            barPercentage: 1,
            categoryPercentage:1
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: true,
        scales: {
            

            y: {
                beginAtZero: true
            }
        }, plugins: 
        {title:{
        display: true, 
        text: 'Distribution of frequency of SAT/ACT scores with filters'
    },   
    subtitle: {
                display: true,
                text: 'average= ' + Math.round(average)+'        n=' + number
            },
            tooltip: { 
                callbacks:{ 

                }
            }
        }
    }
});
histogram.canvas.onclick = clickHandler
async function clickHandler(click){ 
    open = true; 
    let urljson = await fetch('https://dinhbaon.pythonanywhere.com/api/URL')
    let url = await urljson.json(); 
    const points = histogram.getElementsAtEventForMode(click, 'nearest', {intersect: true}, true)
    if (points[0]){
        const index = points[0].index; 
        const label = histogram.data.labels[index];
        let clickfilter = Object.keys(scoredata).filter(function(key) {
        return scoredata[key] == label;
    })
    urlfilter = clickfilter.map(x=> {return url[x]}).reverse()

    }
}

}
afterUpdate(drawHistogram)

</script>
<style> 
.urlsidebar{ 
    float: right; 
    width: 20vw; 
    overflow-y: auto; 
    position: relative; 
    height: 50vh;
    top: 20%; 
    transition: 2s; 
    visibility: hidden; 
    left: 40%; 
}
.opened{ 
    visibility: visible 

}
#chartcontainer{
            width: 40%;
            height:40%; 
        }
@media (max-width: 640px) {
		#chartcontainer{
            width: 90vw; 
            height:auto; 
        }
		}
    
    
    </style>