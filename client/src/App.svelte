<script context='module'>

import Filter from './1_Filter_Donut_Gender.svelte';
import Filterhisto from './3_Filter_Histo_Scores.svelte'
import Filtermajorbreakdown from './2_Filter_Bar_Major.svelte';
import Filteraccept from './4_Filter_Bar_Acceptrate.svelte'
import Filteraveragescore from './5_Filter_Bar_Acceptratebyscore.svelte'


</script>


<head> 
<title>Reddit college results</title>
</head> 
<body>
<div class = 'introbar'>
	<img class='collegeresultslogo' src='..\college results logo.png' alt= 'logo of r/collegeresults'/>
	<h1>Data from r/collegeresults </h1>	
	<a href='https://github.com/Dinhbaon/webscraping-reddit' target="_blank"><img class='githublogo' src='../repologopic.png' alt="github logo"/></a> 
	<a href='https://docs.google.com/spreadsheets/d/1QrWRTwukQpX-ILexLM83K5buYmx-pwC91ASgcbrvmGg/edit?usp=sharing' target="_blank"><img id='spreadsheeticon' src='../spreadsheet.png' alt="spreadsheet link"></a>
	<img id= 'infobutton'class='info' src='..\info button.png' alt='infobutton' on:click={showInfo}/>
</div> 
<div id='infoscreen'>
	<div id='close' on:click={closeInfo}>&#x2716</div>
	<h2 style="left:50%;transform:translateX(-50%); position: absolute;">General notes on usage</h2>
	<p style="clear: both;text-align: left;margin-left: 3vw">This website displays the results of a web scraping data from the subreddit r/collegeresults - The results are not always accurate so you should use it as a filter of sorts not just as a data visualization tool.  </p>
	<h3 style='float:left; display:block;clear:both; margin-left: 2vw; '>Features </h3> 
	<li style=" display:block;clear:both;  ">
	<ol style="text-align: left"> Click on the checkboxes to enable the filter you want to apply. For filters which can take more than 1 input (Acceptances,Rejections,Majors,Ecs) you can <strong>Ctrl+click</strong> (or <strong>command click </strong> on mac) to choose multiple inputs. 
	</ol> 

	<ol style="text-align: left"> 
		<p>Each filter you click is an AND operator - this means that the filter will show the intersection of your filters. 
		<br> For example: if your inputs are Acceptances: Harvard, Princeton and SAT: 1550-1600. This will only show people who got in to <strong>both</strong> Harvard and Princeton <strong>and</strong> also got an SAT score of 1550 to 1600.  
		<br> Do note that the SAT and ACT filters are inclusive of the tail end values. 
		</p>
	</ol>
	<ol style="text-align: left"> 
		<p>You can click on parts of the graph to bring up a list of links to reddit posts which that part of the graph pertains to. 
		<br> For example, if you applied some filters and click on the Male portion of the first graph it will bring up a list of links to reddit posts where the applicant was a Male and also satisfies the filters you set. 
		<br> Note that on the first launch of the site, sometimes you'll have to click twice for the list to show up - it's just a bit glitchy. 
		 </p>
	</ol>
	</li>

	
</div>
<Filter/>
<Filterhisto/>
<Filtermajorbreakdown/>
<Filteraccept/>
<Filteraveragescore/>
<footer>
	Copyright (c) 2022 Dinhbaon
</footer>
</body>

<script>

		
	function showInfo(){ 
		let info = document.getElementById('infoscreen')
    	info.style.display  = "block";
  		
	}
	function closeInfo(){ 
		let info = document.getElementById('infoscreen')
		info.style.display  = "none";
	}
	</script>
<style>
	@font-face {font-family: "RockoFLF"; src: url("//db.onlinewebfonts.com/t/019989000d415bd433b4074af1e753a5.eot");}
	.introbar{ 
		height: 10vh; 
		background-color: hsl(29, 100%, 60%); 
		font-size: 0.9rem; 
		font-family: 'RockoFLF', Arial, Helvetica, sans-serif; 
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

	}
	.info{ 
		float: right; 
		height: 6vh; 
		margin-right:10vw; 
		margin-top:2vh; 
		cursor: pointer;
	}
	#spreadsheeticon{ 
		float:right; 
		height: 6vh;
		margin-right:10vw; 
		margin-top:2vh; 
		cursor: pointer;  
	}
	
	body {
		text-align: center;
		padding: 0 ;
		overflow-x:hidden; 
	}
	#infoscreen{ 
		display:none;
		position: fixed; 
		height: 80vh; 
		width: 60vw; 
		border-radius: 5px; 
		background-color:white; 
		margin: auto; 
		z-index: 10;
		left:50%;
		transform: translateX(-50%); 
		border : solid black 2px; 
		border-radius:5px; 
	}
	#close{ 
		display: inline-block;
		float: right; 
		font-size: 2.5rem; 
		margin: 1vw; 
		cursor: pointer;
	}

	@media (max-width: 640px) {
		.introbar h1{ 
			font-size: 1rem ; 
		}
		.githublogo{ 
			display: none
	}
	}
	footer{
		height: 3vh; 
		font-size: 2vh; 
		font-family: 'RockoFLF', Arial, Helvetica, sans-serif; 
		background-color:hsl(29, 100%, 60%); 
		color: black; 
		transform: translateY(410vh);
		text-align: left; 
		bottom: 0px; 
		width: 100%; 

	}
</style>