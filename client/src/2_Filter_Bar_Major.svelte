<script> 
import Majorbreakdown from './2_Chart_Bar_Major.svelte'
import {unilist, majorlist, eclist} from './list'
import { writable } from 'svelte/store';

let satchecked = false; 
let actchecked = false
let acceptchecked = false; 
let rejectchecked = false; 
let genderchecked = false; 
let ecschecked = false; 
let satuservalue  = writable([])
let actuservalue = writable([])
let acceptselected = writable([]);
let rejectselected = writable([]);
let genderselected = writable([]); 
let ecselected = writable([]);

const jq = window.$; 
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

</script>

<div style="top:20%; position: relative" class="filter">
<div style="margins: 10vh, 0; ">
<div style="float: left; transform: translate(20%,350%); height:10vh;  ">

  <div style="display: flex; flex-wrap: nowrap ;  justify-content: center;">
  <div style = "display: grid; grid-template-coloumn: auto auto; column-gap: 10vw; width:12vw; "> 
  <div>
    <label for='SATmajor' style="float:left; font-size: 1.2rem;">SAT</label>
    <span style="display: block; overflow: hidden;  padding: 0 1vw 0 1vw; text-align:left;"><input type= 'checkbox' id='SATmajor' value='SAT' name='SAT' bind:checked={satchecked} on:change = {satfilteron}/></span>
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
    <label for='ACTmajor' style="float:left;font-size:1.2rem;">ACT</label>
    <span style="display: block; overflow: hidden;  padding: 0 1vw 0 1vw;text-align:left;"><input type= 'checkbox' id='ACTmajor' value='ACT' name='ACT' bind:checked={actchecked} on:change = {actfilteron}/></span>
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
    
  
  
  
  <div style="display: flex; flex-wrap: nowrap ;  justify-content: center; " class="filter">
    <div style = "display: grid; grid-template-coloumn: auto auto; column-gap: 10vw; width: 12vw;  "> 
  <div>
    <label for='acceptsmajor' style="float:left; font-size: 1.2rem;">Acceptances</label>
    <span style="display: block; overflow: hidden; padding: 0 1vw 0 1vw ;text-align:left;"><input type= 'checkbox' id='acceptsmajor' value='accepts' name='accepts' bind:checked={acceptchecked}/></span>
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
    <label for='rejectsmajor' style="float:left;font-size: 1.2rem; " >Rejections</label>
     <span style="display: block; overflow: hidden;  padding: 0 1vw 0 1vw; text-align:left;"><input type= 'checkbox' id='rejectsmajor' value='rejects' name='rejects' bind:checked={rejectchecked}/></span>
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
        <label for='gendersmajor' style="float:left;font-size: 1.2rem; " >Gender</label>
        <span style="display: block; overflow: hidden;  padding: 0 1vw 0 1vw; text-align:left;"><input type= 'checkbox' id='gendersmajor' value='genders' name='genders' bind:checked={genderchecked}/></span>
      </div>
    {#if genderchecked== true}   
    <select  class="dropdown" name ="gender" id="genderselect" bind:value={$genderselected} style="height: 3vw;">
        <option value='Male' style="font-size:0.75rem">Male</option>
        <option value='Female' style="font-size:0.75rem">Female</option>
        <option value='Other/LGBTQ+' style="font-size:0.75rem">Other/LGBTQ+</option>
    </select>
    {/if}
    </div>
    <div style = "display: grid; grid-template-coloumn: auto auto; column-gap: 10vw; width: 12vw;  ">  
      <div>
        <label for='ecsmajor' style="float:left;font-size: 1.2rem; " >Ecs</label>
        <span style="display: block; overflow: hidden;  padding: 0 1vw 0 1vw; text-align:left;"><input type= 'checkbox' id='ecsmajor' value='ecs' name='ecs' bind:checked={ecschecked}/></span>
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
</div>

<Majorbreakdown {satchecked} {satuservalue} 
                {actchecked} {actuservalue} 
                {acceptchecked} {acceptselected} 
                {rejectchecked} {rejectselected} 
                {genderchecked} {genderselected}
                {ecschecked} {ecselected}/>
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
  @media (max-width: 640px){
.filter{ 
  visibility: hidden; 
}
}
  </style>