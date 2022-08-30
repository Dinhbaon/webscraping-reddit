<script context='module'>
import { writable} from "svelte/store";
import { setContext } from "svelte";

import Genderbreakdown from './genderbreakdown.svelte'


</script>

<script >
import { each } from "svelte/internal";

    
    const jq = window.$; 
    let unilist = ['Princeton', 'Harvard', ' Mit ', 'Yale', 'Stanford', 'Uchicago', 'Upenn', 'Caltech', 'Duke', 'Jhu', 'Northwestern', 'Dartmouth', 'Brown', 'Vanderbilt', 'Washu', 'Cornell', 'Rice', 'University of notre dame', 'Ucla', 'Emory', 'Uc berkeley', 'Georgetown', 'Umich', 'Cmu', ' uva ', ' usc ', 'Nyu', 'Tufts', 'Ucsb', ' uf ', 'Unc', 'Wake forest', 'Ucsd', 'University of rochester', 'Boston college', 'Uci', 'Gatech', 'Uc davis', 'Ut austin', 'William & mary', ' bu ', 'Brandeis', 'Cwru', 'Tulane', 'Uw madison', 'Uiuc', 'Uga', 
'Lehigh', 'Northeastern', 'Osu', 'Pepperdine', 'Purdue', 'Villanova', 'Williams', 'Amherst college', 'Swarthmore', 'Pomona', 'Wellesley', 'Bowdoin', 'Claremont', 'Carleton', 'Middlebury', 'Washington & lee', 'Davidson', 'Grinnell', 'Hamilton', 'Haverford', 'Barnard', 'Colby', 'Colgate', 'Smith', 'Wesleyan']
    let majorlist = ['Math', 'Physics', 'Bio', 'Premed', 'Neuroscience', 'Chemistry', 'Computer science', 'Mechanical engineer', 'Chemical engineer', 'Computer engineering', 'Electrical engineering', 'Aerospace engineering', 'Econ', 'Finance', 'Business', 'Marketing', 'History', 'Political science', 'Philosophy', 'Law', 'English', 'Undecided', 'Arts', 'Anthropology', 'Environmental', ' international relations', 'Nursing', 'Sociology', 'Psychology']
    let satchecked = false;
    let actchecked = false; 
    let acceptchecked = false; 
    let rejectchecked = false; 
    let majorchecked = false; 
    let majorselected = writable([])
    let satuservalue = writable([]);
    let actuservalue = writable([]);
    let acceptselected = writable([]);
    let rejectselected = writable([]);

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

<div>
  <h2 style= "font-size: 1.7vmax">Filter by: </h2>
<div style="display: flex; flex-wrap: nowrap ;  justify-content: center;">
<div style = "display: grid; grid-template-coloumn: auto auto; column-gap: 10vw; width:12vw; "> 
<div>
  <label for='SAT' style="float:left; font-size: 2.5vmin;">SAT</label>
  <span style="display: block; overflow: hidden;  padding: 0 1vw 0 1vw; text-align:left;"><input type= 'checkbox' id='SAT' value='SAT' name='SAT' bind:checked={satchecked} on:change = {satfilteron}/></span>
</div>
{#if satchecked == true}
<span class = "slider" >
  <div  id="satrangeslider"></div>
  <div id="satrangedval" style="font-size: 2vmin;">
    SAT range: <span id="satrangeval" style="white-space: nowrap; ">800 - 1600</span>
  </div>
</span>
{/if}
</div>
<div style = "display: grid; grid-template-coloumn: auto auto; column-gap: 10vw; width: 12vw; "> 
<div>
  <label for='ACT' style="float:left;font-size: 2.5vmin;">ACT</label>
  <span style="display: block; overflow: hidden;  padding: 0 1vw 0 1vw;text-align:left;"><input type= 'checkbox' id='ACT' value='ACT' name='ACT' bind:checked={actchecked} on:change = {actfilteron}/></span>
</div>

{#if actchecked == true}
<div class = "slider">
    <div  id="actrangeslider"></div>
    <div id="actrangedval" style="font-size: 2vmin;">
      ACT range: <span id="actrangeval" style="white-space: nowrap;">1 - 36</span>
    </div>
  </div>
{/if}
</div>
</div>
  



<div style="display: flex; flex-wrap: nowrap ;  justify-content: center; ">
  <div style = "display: grid; grid-template-coloumn: auto auto; column-gap: 10vw; width: 12vw;  "> 
<div>
  <label for='accepts' style="float:left; font-size: 2.5vmin;">Acceptances</label>
  <span style="display: block; overflow: hidden; padding: 0 1vw 0 1vw ;text-align:left;"><input type= 'checkbox' id='accepts' value='accepts' name='accepts' bind:checked={acceptchecked}/></span>
</div>
  {#if acceptchecked == true}
  <label for = 'acceptselect' ></label>
  <select multiple name ="accept" id="acceptselect" class="dropdown"bind:value={$acceptselected} style="height: 15vw; margin-bottom: 2vw;">
{#each unilist as uni}
  <option value={uni} style="font-size:1.1vmax">{uni}</option>
{/each}
  </select>
{/if}
</div>
<div style = "display: grid; grid-template-column: auto auto; column-gap: 10vw; width: 12vw; "> 
<div>
  <label for='rejects' style="float:left;font-size: 2.5vmin; " >Rejections</label>
   <span style="display: block; overflow: hidden;  padding: 0 1vw 0 1vw; text-align:left;"><input type= 'checkbox' id='rejects' value='rejects' name='rejects' bind:checked={rejectchecked}/></span>
</div>
   {#if rejectchecked== true}
  <label for = 'rejectselect' ></label>
  <select multiple name ="reject" id="rejectselect" class="dropdown"bind:value={$rejectselected} style="height: 15vw;">
{#each unilist as uni}
  <option value={uni} style="font-size:1.1vmax">{uni}</option>
{/each}
  </select>
{/if}
</div>
</div>

<div style="display: flex; flex-wrap: nowrap ;  justify-content: center; ">
  <div style = "display: grid; grid-template-coloumn: auto auto; column-gap: 10vw; width: 12vw;  "> 
  <div>
    <label for='majors' style="float:left;font-size: 2.5vmin; " >Major</label>
     <span style="display: block; overflow: hidden;  padding: 0 1vw 0 1vw; text-align:left;"><input type= 'checkbox' id='majors' value='majors' name='majors' bind:checked={majorchecked}/></span>
  </div>
     {#if majorchecked== true}  
    <label for = 'majorselect' ></label>
    <select multiple name ="major" id="majorselect" class="dropdown"on:change:value={$majorselected} style="height: 15vw;">
  {#each majorlist as majors}
    <option value={majors} style="font-size:1.1vmax">{majors}</option>
  {/each}
    </select>
  {/if}
</div>
<div style = "display: grid; grid-template-coloumn: auto auto; column-gap: 10vw; width: 12vw;  ">  </div>
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
</style>
<Genderbreakdown {satchecked} {satuservalue} 
{actuservalue} {actchecked} 
{acceptselected} {acceptchecked} 
{rejectchecked} {rejectselected}
{majorchecked} {majorselected}/>