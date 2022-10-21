<script>
import { writable } from 'svelte/store';
import {unilist, majorlist, eclist} from './list'
import Acceptrate from './4_Chart_Bar_Acceptrate.svelte'

let acceptselected = writable(['Princeton','Harvard'])
const jq = window.$; 
    
    let satchecked = false;
    let actchecked = false; 
    let majorchecked = false; 
    let ecschecked = false; 
    let genderchecked = false; 
    let genderselected  =writable([]); 
    let majorselected = writable([]);
    let satuservalue = writable([]);
    let actuservalue = writable([]);
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


</script> 

<div style="top: 250%; position: relative; ; display:grid; grid-template-rows: auto auto; grid-template-columns: auto">
    <Acceptrate {acceptselected} {actchecked} {satchecked} {satuservalue} {actuservalue} {majorselected} {majorchecked} {genderchecked} {genderselected}/>
    
        <div style=" position: relative;  left:50%; transform:translateX(-50%); top:40vh; width: 12vw;" class="filter">
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

        <div style="float: left;transform: translateX(-65%); position: absolute; display: grid; grid-template-rows: auto auto;" class="filter">
            <div style="display: flex; flex-wrap: nowrap ;  justify-content: center;">
            <div style = "display: grid; grid-template-coloumn: auto auto; column-gap: 10vw; width:12vw; "> 
            <div>
              <label for='SATaccept' style="float:left; font-size: 1.2rem">SAT</label>
              <span style="display: block; overflow: hidden;  padding: 0 1vw 0 1vw; text-align:left;"><input type= 'checkbox' id='SATaccept' value='SAT' name='SAT' bind:checked={satchecked} on:change = {satfilteron}/></span>
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
              <label for='ACTaccept' style="float:left;font-size: 1.2rem;">ACT</label>
              <span style="display: block; overflow: hidden;  padding: 0 1vw 0 1vw;text-align:left;"><input type= 'checkbox' id='ACTaccept' value='ACT' name='ACT' bind:checked={actchecked} on:change = {actfilteron}/></span>
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
        <div style="display: grid; grid-template-columns: auto auto; width: 12vw;">
          <div style="width: 12vw;">
            <div>
                <label for='majorsaccept' style="float:left;font-size: 1.2rem; " >Major</label>
                <span style="display: block; overflow: hidden;  padding: 0 1vw 0 1vw; text-align:left;"><input type= 'checkbox' id='majorsaccept' value='majors' name='majors' bind:checked={majorchecked}/></span>
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
            <div style="width: 12vw;">
              <div>
                  <label for='gendersavg' style="float:left;font-size: 1.2rem; " >Gender</label>
                  <span style="display: block; overflow: hidden;  padding: 0 1vw 0 1vw; text-align:left;"><input type= 'checkbox' id='gendersavg' value='genders' name='majors' bind:checked={genderchecked}/></span>
              </div>
              {#if genderchecked== true}  
                  <label for = 'genderselecthisto' ></label>
                  <select class="dropdown" name ="gender" id="genderselecthisto" bind:value={$genderselected} style="height: 3vw;">
                      <option selected value='Male' style="font-size:0.75rem">Male</option>
                      <option value='Female' style="font-size:0.75rem">Female</option>
                      <option value='Other/LGBTQ+' style="font-size:0.75rem">Other/LGBTQ+</option>
                  </select>
              {/if}
          </div>
        </div>
        <div style = "display: grid; grid-template-coloumn: auto auto; column-gap: 10vw; width: 12vw;  ">  
          <div>
            <label for='ecsaccept' style="float:left;font-size: 1.2rem; " >Ecs</label>
            <span style="display: block; overflow: hidden;  padding: 0 1vw 0 1vw; text-align:left;"><input type= 'checkbox' id='ecsaccept' value='ecs' name='ecs' bind:checked={ecschecked}/></span>
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
    @media (max-width:640px){
    .filter{ 
        visibility: hidden; 
    }
    }
    </style>