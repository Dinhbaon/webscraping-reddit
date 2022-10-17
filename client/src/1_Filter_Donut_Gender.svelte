<script context='module'>
import { writable} from "svelte/store";

import Genderbreakdown from './1_Chart_Donut_Gender.svelte'
import {unilist, majorlist, eclist} from './list'

</script>

<script >


    
    const jq = window.$; 
    
    let satchecked = false;
    let actchecked = false; 
    let acceptchecked = false; 
    let rejectchecked = false; 
    let majorchecked = false; 
    let ecschecked = false; 
    let majorselected = writable([])
    let satuservalue = writable([]);
    let actuservalue = writable([]);
    let acceptselected = writable([]);
    let rejectselected = writable([]);
    let ecselected = writable([])

var satfilteron = () => {
    $satuservalue = [800,1600];
    jq(function(){
    jq('#satrangeslider').slider({
    step: 10,
    range: true,
    min: 800,
    max: 1600,
    values: [ 800, 1600 ],
    stop: function( event, ui ) {
     $satuservalue = ui.values;
    }
    ,slide: function(event,ui){ 
        jq('#satrangeval').html(ui.values[0]+" - "+ui.values[1])
    }
  });
});
} 

var actfilteron = () => {
    $actuservalue = [0,36];
    jq(function(){
    jq('#actrangeslider').slider({
    step: 1,
    range: true,
    min: 1,
    max: 36,
    values: [ 0, 36 ],
    stop: function(event,ui){
      $actuservalue = ui.values
    },
    slide: function( event, ui ) {
      jq('#actrangeval').html(ui.values[0]+" - "+ui.values[1]);
    }
  });
});
} 

function responsiveFont(){ 
    if(window.outerWidth>999){ 
        Chart.options.plugins.datalabels.font = 20
    }
    if(window.outerWidth<999 && window.outerWidth>750){ 
        Chart.options.plugins.datalabels.font = 15
    }
    if(window.outerwidth<500 && window.outerWidth>250){
        Chart.options.plugins.datalabels.font = 10
    }
    if(window.outerwidth<250 && window.outerWidth>0){
        Chart.options.plugins.datalabels.font = 5
    }
}
</script>

<div style="float: left; transform: translateX(20%); position: absolute; " class='filter'>
  <h2 style= "font-size: clamp(3re,1.7vmax,2rem)">Filter by: </h2>
<div style="display: flex; flex-wrap: nowrap ;  justify-content: center;">
<div style = "display: grid; grid-template-coloumn: auto auto; column-gap: 10vw; width:12vw; "> 
<div>
  <label for='SAT' style="float:left; font-size: 1.2rem">SAT</label>
  <span style="display: block; overflow: hidden;  padding: 0 1vw 0 1vw; text-align:left;"><input type= 'checkbox' id='SAT' value='SAT' name='SAT' bind:checked={satchecked} on:change = {satfilteron}/></span>
</div>
{#if satchecked == true}
<span class = "slider" >
  <div  id="satrangeslider"></div>
  <div id="satrangedval" style="font-size: 1rem;">
    SAT range: <span id="satrangeval" style="white-space: nowrap; ">800 - 1600</span>
  </div>
</span>
{/if}
</div>
<div style = "display: grid; grid-template-coloumn: auto auto; column-gap: 10vw; width: 12vw; "> 
<div>
  <label for='ACT' style="float:left;font-size: 1.2rem;">ACT</label>
  <span style="display: block; overflow: hidden;  padding: 0 1vw 0 1vw;text-align:left;"><input type= 'checkbox' id='ACT' value='ACT' name='ACT' bind:checked={actchecked} on:change = {actfilteron}/></span>
</div>

{#if actchecked == true}
<div class = "slider">
    <div  id="actrangeslider"></div>
    <div id="actrangedval" style="font-size: 1rem;">
      ACT range: <span id="actrangeval" style="white-space: nowrap;">1 - 36</span>
    </div>
  </div>
{/if}
</div>
</div>
  



<div style="display: flex; flex-wrap: nowrap ;  justify-content: center; ">
  <div style = "display: grid; grid-template-coloumn: auto auto; column-gap: 10vw; width: 12vw;  "> 
<div>
  <label for='accepts' style="float:left;font-size: 1.2rem;">Acceptances</label>
  <span style="display: block; overflow: hidden; padding: 0 1vw 0 1vw ;text-align:left;"><input type= 'checkbox' id='accepts' value='accepts' name='accepts' bind:checked={acceptchecked}/></span>
</div>
  {#if acceptchecked == true}
  <label for = 'acceptselect' ></label>
  <select multiple name ="accept" id="acceptselect" class="dropdown"bind:value={$acceptselected} style="height: 15vw; margin-bottom: 2vw;">
{#each unilist as uni}
  <option value={uni} style="font-size: 0.75rem">{uni}</option>
{/each}
  </select>
{/if}
</div>
<div style = "display: grid; grid-template-column: auto auto; column-gap: 10vw; width: 12vw; "> 
<div>
  <label for='rejects' style="float:left;font-size: 1.2rem; " >Rejections</label>
   <span style="display: block; overflow: hidden;  padding: 0 1vw 0 1vw; text-align:left;"><input type= 'checkbox' id='rejects' value='rejects' name='rejects' bind:checked={rejectchecked}/></span>
</div>
   {#if rejectchecked== true}
  <label for = 'rejectselect' ></label>
  <select multiple name ="reject" id="rejectselect" class="dropdown"bind:value={$rejectselected} style="height: 15vw;">
{#each unilist as uni}
  <option value={uni} style="font-size:0.75rem">{uni}</option>
{/each}
  </select>
{/if}
</div>
</div>

<div style="display: flex; flex-wrap: nowrap ;  justify-content: center; ">
  <div style = "display: grid; grid-template-coloumn: auto auto; column-gap: 10vw; width: 12vw;  "> 
    <div>
      <label for='majors' style="float:left;font-size: 1.2rem; " >Major</label>
      <span style="display: block; overflow: hidden;  padding: 0 1vw 0 1vw; text-align:left;"><input type= 'checkbox' id='majors' value='majors' name='majors' bind:checked={majorchecked}/></span>
    </div>
  {#if majorchecked== true}  
    <label for = 'majorselect' ></label>
    <select multiple name ="major" id="majorselect" class="dropdown"bind:value={$majorselected} style="height: 15vw;">
  {#each majorlist as majors}
    <option value={majors} style="font-size:0.75rem">{majors}</option>
  {/each}
    </select>
  {/if}
  </div>
<div style = "display: grid; grid-template-coloumn: auto auto; column-gap: 10vw; width: 12vw;  ">  
  <div>
    <label for='ecs' style="float:left;font-size: 1.2rem; " >Ecs</label>
    <span style="display: block; overflow: hidden;  padding: 0 1vw 0 1vw; text-align:left;"><input type= 'checkbox' id='ecs' value='ecs' name='ecs' bind:checked={ecschecked}/></span>
  </div>
{#if ecschecked== true}  
  <label for = 'ecselect' ></label>
  <select multiple name ="ec" id="ecselect" class="dropdown"bind:value={$ecselected} style="height: 15vw;">
{#each eclist as ecs}
  <option value={ecs} style="font-size:0.75rem">{ecs}</option>
{/each}
  </select>
{/if}

</div>
</div>


</div>
 






<style> 
.slider{ 
    display: block;
    width: 10vw; 
    overflow: hidden; 
    margin:0; 
    padding: 0;
}
.dropdown{ 
  width: 10vw; 
  margin: 0; 
  padding:0; 
}
.filter{ 
  visibility: hidden; 
}
</style>

<div style="position: absolute; left: 50%; transform: translateX(-50%); width: 35vw; height: 35vw; display:block;">
<Genderbreakdown {satchecked} {satuservalue} 
{actuservalue} {actchecked} 
{acceptselected} {acceptchecked} 
{rejectchecked} {rejectselected}
{majorchecked} {majorselected}
{ecschecked} {ecselected} onresize="responseiveFont()"/>
</div>

