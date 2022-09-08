<script context='module'>

import Filter from './filter.svelte';
import Filterhisto from './filterhisto.svelte'
import Filtermajorbreakdown from './filtermajorbreakdown.svelte';
import Filteraccept from './filteraccept.svelte'
import Filteraveragescore from './filteraveragescore.svelte'


</script>


<head> 

</head> 
<body>
	<div class = 'introbar'>
	<img class='collegeresultslogo' src='..\college results logo.png' alt= 'logo of r/collegeresults'/>
	<h1 style="font-size:2.5rem;">Data from r/collegeresults </h1>	
	<a href='https://github.com/Dinhbaon/webscraping-reddit' target="_blank"><img class='githublogo' src='..\githublogo.png' alt="github logo"></a> 
	</div> 


<Filter/>
<Filterhisto/>
<Filtermajorbreakdown/>
<Filteraccept/>
<Filteraveragescore/>





		


	


	
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
		z-index: 2; 
		
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
	.collegeresultslogo{ 
		float: left; 
		height: 10vh; 
		padding-left: 2vw; 
	}
	.githublogo{ 
		float: right; 
		height: 10vh; 
		margin-right: 10vw; 
		border-left: solid black 1px;
		border-right: solid black 1px;
		border-radius: 1vh

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