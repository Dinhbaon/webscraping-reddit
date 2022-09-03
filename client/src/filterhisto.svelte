<script> 
import Histogram from './histogram.svelte'
import {unilist, majorlist} from './list'
import { writable} from "svelte/store";
let satchecked = true; 
let actchecked = false; 
let majorchecked = false; 
let acceptchecked = false; 
let rejectchecked = false; 
let genderchecked = false; 
let satuservalue = writable([800,1600]);
let actuservalue = writable([0,36]);
let majorselected  = writable([])
let acceptselected =writable([])
let rejectselected = writable([])
let genderselected = writable([])
const jq = window.$; 


    
if (satchecked == true){
    actchecked = false; 
    jq(function(){
    jq('#satrangesliderhisto').slider({
    step: 10,
    range: true,
    min: 800,
    max: 1600,
    values: [ 800, 1600 ],
    stop: function( event, ui ) {
     $satuservalue = ui.values;
    }
    ,slide: function(event,ui){ 
        jq('#satrangevalhisto').html(ui.values[0]+" - "+ui.values[1])
    }
  });
});}
var satfilteron =() => {
    actchecked = false; 
    jq(function(){
    jq('#satrangesliderhisto').slider({
    step: 10,
    range: true,
    min: 800,
    max: 1600,
    values: [ 800, 1600 ],
    stop: function( event, ui ) {
     $satuservalue = ui.values;
    }
    ,slide: function(event,ui){ 
        jq('#satrangevalhisto').html(ui.values[0]+" - "+ui.values[1])
    }
  });
});
}

var actfilteron = () => {
    satchecked = false; 

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
});}


</script>

    
<div style="position: relative; top: 100%; ">
    <div style="position: relative;width: 80vw; height: auto; display: flex; justify-content:center; width: 100%">  

            <div style="display: grid; grid-template: auto auto/ auto auto; position: absolute; right:75%;  ">
            <div style="display: grid; grid-template-coloumn: auto auto; column-gap: 10vw; width: 12vw;">
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
            <div style="display: grid; grid-template-coloumn: auto auto; column-gap: 10vw; width: 12vw;">
                <div>
                    <label for='majors' style="float:left;font-size: 2.5vmin; " >Major</label>
                    <span style="display: block; overflow: hidden;  padding: 0 1vw 0 1vw; text-align:left;"><input type= 'checkbox' id='majors' value='majors' name='majors' bind:checked={majorchecked}/></span>
                </div>
                {#if majorchecked== true}  
                    <label for = 'majorselect' ></label>
                    <select multiple name ="major" id="majorselect" class="dropdown"bind:value={$majorselected} style="height: 15vw;">
                {#each majorlist as majors}
                    <option value={majors} style="font-size:1.1vmax">{majors}</option>
                {/each}
                    </select>
                {/if}
            </div>
            
        
            <div style="display: grid; grid-template-coloumn: auto auto; column-gap: 10vw; width: 12vw;">
                <div>
                    <label for='rejects' style="float:left; font-size: 2.5vmin;">Rejections</label>
                    <span style="display: block; overflow: hidden; padding: 0 1vw 0 1vw ;text-align:left;"><input type= 'checkbox' id='accepts' value='accepts' name='accepts' bind:checked={rejectchecked}/></span>
                </div>
               
        
                {#if rejectchecked == true}
                    <label for = 'rejectselect' ></label>
                    <select multiple name ="reject" id="rejectselect" class="dropdown"bind:value={$rejectselected} style="height: 15vw; margin-bottom: 2vw;">
                {#each unilist as uni}
                    <option value={uni} style="font-size:1.1vmax">{uni}</option>
                {/each}
                    </select>
                {/if}
            </div>
            <div style="width: 12vw;">
                <div>
                    <label for='genders' style="float:left;font-size: 2.5vmin; " >Gender</label>
                    <span style="display: block; overflow: hidden;  padding: 0 1vw 0 1vw; text-align:left;"><input type= 'checkbox' id='majors' value='majors' name='majors' bind:checked={genderchecked}/></span>
                </div>
                {#if genderchecked== true}  
                    <label for = 'genderselect' ></label>
                    <select name ="gender" id="genderselect" bind:value={$genderselected} style="height: 3vw;">
                        <option value='Male' style="font-size:1.1vmax">Male</option>
                        <option value='Female' style="font-size:1.1vmax">Female</option>
                        <option value='Other/LGBTQ+' style="font-size:1.1vmax">Other/LGBTQ+</option>
                    </select>
                {/if}
            </div>
        </div>
 
         
         <Histogram {satchecked} {actchecked} 
                    {satuservalue} {actuservalue}
                    {majorchecked} {majorselected}
                    {acceptchecked} {acceptselected}
                    {genderchecked} {genderselected}
                    {rejectchecked} {rejectselected}/>
             

                   
    </div>
    <h2 style= "font-size: 1.7vmax; margin: 0; position: absolute; left:50%">X-axis: </h2>
    <div style="display: flex; flex-wrap: nowrap ;  justify-content: center; float: left; position: relative; transform: translateY(-900%); left: 2vw;">  
        
  
 
  </div>

        <div>    
                <div style="display: flex; flex-wrap: nowrap ;  justify-content: center; gap:10vw; position: absolute; left: 50%; transform: translateX(-50%); margin:0; bottom:-25%;">
                    <div style = "width:12vw; margin:0; transform: translateX(50%); position: relative"> 
                        <div>
                            <label for='SAT' style="float:left; font-size: 2.5vmin;">SAT</label>
                                <span style="display: block; overflow: hidden;  padding: 0 1vw 0 1vw; text-align:left;"><input type= 'checkbox' id='SAT' value='SAT' name='SAT' bind:checked={satchecked} on:change={satfilteron} /></span>
                        </div>
                        {#if satchecked == true}
                            <span class = "slider" >
                                <div  id="satrangesliderhisto"></div>
                                <div id="satrangedval" style="font-size: 2vmin;">
                                    SAT range: <span id="satrangevalhisto" style="white-space: nowrap; ">800 - 1600</span>
                                </div>
                            </span>
                        {/if}
                    </div>

                    <div style = "width: 12vw;  margin:0; left:50%; transform: translateX(-50)"> 
                        <div>
                            <label for='ACT' style="float:left;font-size: 2.5vmin;">ACT</label>
                            <span style="display: block; overflow: hidden;  padding: 0 1vw 0 1vw;text-align:left;"><input type= 'checkbox' id='ACT' value='ACT' name='ACT' bind:checked={actchecked} on:change={actfilteron}/></span>
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