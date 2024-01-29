import './Navbar.css'

const Navbar = () => {
    return(
        <div>
        <div className = {'introbar'}>
            <img className={'collegeresultslogo'} src='\college results logo.png' alt= 'logo of r/collegeresults'/>
            <h1>Data from r/collegeresults </h1>	
            <a href='https://github.com/Dinhbaon/webscraping-reddit' target="_blank">
                <img className='githublogo' src='/repologopic.png' alt="github logo"/>
            </a> 
            <a href='https://docs.google.com/spreadsheets/d/1QrWRTwukQpX-ILexLM83K5buYmx-pwC91ASgcbrvmGg/edit?usp=sharing' target="_blank">
                <img id='spreadsheeticon' src='/spreadsheet.png' alt="spreadsheet link"/>
            </a>
            <img id= 'infobutton'className='info' src='\info button.png' alt='infobutton' />
        </div> 
    </div>
    )
}

export default Navbar