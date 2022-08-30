<script context='module'>

	import Genderbreakdown from './genderbreakdown.svelte'
	
	import Filters from './filter.svelte'
	import { writable } from 'svelte/store';
import Filter from './filter.svelte';

</script>


<head> 

</head> 
<body>
	<div class = 'introbar'>
	<img src='..\college results logo.png' alt= 'logo of r/collegeresults'/>
	<h1 style="font-size:5vh;">Data from r/collegeresults </h1>	
	</div> 

	
<div style=" height:35vh; width:35vw; position:absolute; transform : translateX(-50%); left: 50% "> 

	<Genderbreakdown />
</div>
<div style="float: left; transform: translateX(5vw)">
<Filter/>
</div>

		


	


	
</body>

<style>
	@font-face {font-family: "RockoFLF"; src: url("//db.onlinewebfonts.com/t/019989000d415bd433b4074af1e753a5.eot");
}
	.introbar{ 
		height: 10vh; 
		background-color: hsl(29, 100%, 60%); 
		font-size: 0.9rem; 
		font-family: RockoFLF; 
		width: 100vw; 
		
	}
	.introbar h1{ 
		float: left; 
		padding-left: 4vw; 
		font-size: 2rem; 
		font-weight: 600; 
		top: 50%;
		position: relative;
		transform: translateY(-50%);
		margin: 0; 
	}
	.introbar img{ 
		float: left; 
		height: 10vh; 
		padding-left: 2vw; 
	}
	
	body {
		text-align: center;
		max-width: 240px;
		padding: 0 ;
		overflow-x:hidden; 
	}

	@media (min-width: 640px) {
		body {
			max-width: none;
		}
	}

</style>