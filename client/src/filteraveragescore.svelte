<script>
    import { writable } from 'svelte/store';
    import {unilist, majorlist, eclist} from './list'
    import Averagescore from './averagescorebyuni.svelte'
    
    let acceptselected = writable(['Princeton','Harvard'])
    const jq = window.$; 
        
        let satchecked = true;
        let actchecked = false; 
        let acceptchecked = false; 
        let rejectchecked = false; 
        let majorchecked = false; 
        let ecschecked = false; 
        let majorselected = writable([]);
        let satuservalue = writable([]);
        let actuservalue = writable([]);
        let ecselected = writable([])
    
    var satfilteron = () => {
        actchecked = false; 
    } 
    
    var actfilteron = () => {
        satchecked = false; 
    }  
    
    
    </script> 
    
    <div style="top: 250%; position: relative; ; display:grid; grid-template-rows: auto auto; grid-template-columns: auto; left: 50%; transform: translateX(-50%)">
        <Averagescore {acceptselected} {actchecked} {satchecked} {satuservalue} {actuservalue} {majorselected} {majorchecked}/>
        
            <div style=" position: relative;  left:50%; transform:translateX(-50%); top:40vh; width: 12vw; display: grid; grid-template-columns: auto auto auto; gap: 5vw">
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
              
            <div style="float: left;transform: translateX(-65%); position: absolute; display: grid; grid-template-rows: auto auto;">
                
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
              <div style = "display: grid; grid-template-coloumn: auto auto; column-gap: 10vw; width: 12vw;  "> 
                <div style="width: 12vw;">
                  <div>
                      <label for='Ecs' style="float:left;font-size: 1.2rem; " >Ecs</label>
                      <span style="display: block; overflow: hidden;  padding: 0 1vw 0 1vw; text-align:left;"><input type= 'checkbox' id='majors' value='ecs' name='ecs' bind:checked={ecschecked}/></span>
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