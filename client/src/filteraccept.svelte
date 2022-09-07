<script>
import { writable } from 'svelte/store';
import {unilist, majorlist} from './list'
import Acceptrate from './acceptrate.svelte'

let acceptselected = writable(['Princeton'])
const jq = window.$; 
    
    let satchecked = false;
    let actchecked = false; 
    let acceptchecked = false; 
    let rejectchecked = false; 
    let majorchecked = false; 
    let majorselected = writable([])
    let satuservalue = writable([]);
    let actuservalue = writable([]);

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

<div style="top: 200%; position: relative; ; display:grid; grid-template-rows: auto auto; grid-template-columns: auto">
    <Acceptrate {acceptselected} {actchecked} {satchecked} {satuservalue} {actuservalue} {majorselected} {majorchecked}/>
    
        <div style=" position: relative;  left:50%; transform:translateX(-50%); top:40vh; width: 12vw;">
            <div style="display: grid; grid-template-coloumn: auto auto; column-gap: 10vw;  ">
                <div>
                    <label for='accepts' style="float:left; font-size: 1.2rem;">Acceptances</label>
                   
                </div>
               
                    <label for = 'acceptselect' ></label>
                    <select multiple name ="accept" id="acceptselect" class="dropdown"bind:value={$acceptselected} style="height: 15vw; margin-bottom: 2vw;">
                {#each unilist as uni}
                    <option value={uni} style="font-size:0.75rem">{uni}</option>
                {/each}
                    </select>

            </div>
        </div> 

        <div style="float: left;transform: translateX(-65%); position: absolute; display: grid; grid-template-rows: auto auto;">
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
        <div style="display: grid; grid-template-coloumn: auto auto; column-gap: 10vw; width: 12vw;">
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