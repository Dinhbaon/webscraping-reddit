<script>
import { writable } from 'svelte/store';
import {unilist, majorlist} from './list'
import Acceptrate from './acceptrate.svelte'

let acceptselected = writable([])

</script> 

<div style="top: 200%; position: relative; ; display:grid; grid-template-rows: auto auto; grid-template-columns: auto">
    <Acceptrate {acceptselected} />
    
<div style=" position: relative;  left:50%; transform:translateX(-50%); top:50vh; width: 12vw;">
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



</div>

