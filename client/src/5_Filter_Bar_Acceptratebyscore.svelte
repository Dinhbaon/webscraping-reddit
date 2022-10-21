<script>
    import { writable } from 'svelte/store';
    import {unilist, majorlist, eclist} from './list'
    import Averagescore from './5_Chart_Bar_Acceptratebyscore.svelte'
    
    let acceptselected = writable(['Princeton','Harvard'])
    const jq = window.$; 
        
        let satchecked = true;
        let actchecked = false; 
        let majorchecked = false; 
        let ecschecked = false; 
        let genderchecked= false; 
        let majorselected = writable([]);
        let satuservalue = writable([]);
        let actuservalue = writable([]);
        let ecselected = writable([])
        let genderselected = writable([])
    
    var satfilteron = () => {
        actchecked = false; 
    } 
    
    var actfilteron = () => {
        satchecked = false; 
    }  
    
    
    </script> 
    
    <div style="top: 410%;position: absolute;display: grid;grid-template-rows: auto auto;grid-template-columns: auto;left: 50%;transform: translateX(-50%);">
        <Averagescore {acceptselected} {actchecked} 
                      {satchecked} {satuservalue} 
                      {actuservalue} {majorselected} 
                      {majorchecked} {ecschecked} 
                      {ecselected} {genderchecked}
                      {genderselected}/>
        
            <div style=" position: relative;  left:50%; transform:translateX(-50%); top:40vh; width: 12vw; display: grid; grid-template-columns: auto auto auto; gap: 5vw" class="filter">
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
                <div> 
                <div style = "display: grid; grid-template-coloumn: auto auto; column-gap: 10vw; width:12vw; "> 
                    <div>
                      <label for='SAT' style="float:left; font-size: 1.2rem">SAT</label>
                      <span style="display: block; overflow: hidden;  padding: 0 1vw 0 1vw; text-align:left;"><input type= 'checkbox' id='SAT' value='SAT' name='SAT' bind:checked={satchecked} on:change = {satfilteron}/></span>
                    </div>

                    </div>
                    <div style = "display: grid; grid-template-coloumn: auto auto; column-gap: 10vw; width: 12vw; "> 
                    <div>
                      <label for='ACT' style="float:left;font-size: 1.2rem;">ACT</label>
                      <span style="display: block; overflow: hidden;  padding: 0 1vw 0 1vw;text-align:left;"><input type= 'checkbox' id='ACT' value='ACT' name='ACT' bind:checked={actchecked} on:change = {actfilteron}/></span>
                    </div>
                    

                    </div>
            </div> 
    
            
            </div>
              
            <div style="float: left; position: absolute; display: grid; grid-template-columns: auto auto; left:-300%;" class="filter">
                
              <div style="display: grid; grid-template-coloumn: auto auto; column-gap: 10vw; width: 10vw;">
                  <div>
                      <label for='majorsavg' style="float:left;font-size: 1.2rem; " >Major</label>
                      <span style="display: block; overflow: hidden;  padding: 0 1vw 0 1vw; text-align:left;"><input type= 'checkbox' id='majorsavg' value='majorsavg' name='majorsavg' bind:checked={majorchecked}/></span>
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
                  <label for='ecsavg' style="float:left;font-size: 1.2rem; " >Ecs</label>
                  <span style="display: block; overflow: hidden;  padding: 0 1vw 0 1vw; text-align:left;"><input type= 'checkbox' id='ecsavg' value='ecsavg' name='ecsavg' bind:checked={ecschecked}/></span>
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