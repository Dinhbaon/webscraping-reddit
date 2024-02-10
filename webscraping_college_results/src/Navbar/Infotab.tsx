import { isMobile } from 'react-device-detect'
import './Infotab.css'

const Infotab = (setIsInfoOpened: { setIsInfoOpened: (isOpen: boolean) => void }) => {

    const closeInfoTab = () => {
        setIsInfoOpened.setIsInfoOpened(false)
    }
    return (
        <div className='infoscreen'>
            <div className='close' onClick={closeInfoTab} dangerouslySetInnerHTML={{ __html: '&#x2716' }}></div>
            {isMobile ? <h2 style={{ left: "50%", transform: "translateX(-50%)", position: "absolute", fontSize: "1rem"}}>General notes on usage</h2> : 
            <h2 style={{ left: "50%", transform: "translateX(-50%)", position: "absolute", fontSize: "2rem"}}>General notes on usage</h2>}
            
            <p style={{ clear: "both", textAlign: "left", marginLeft: "3vw" }}>This website displays the results of a web scraping data from the subreddit r/collegeresults - The results are not always accurate so you should use it as a filter of sorts not just as a data visualization tool.  </p>
            <h3 style={{ float: "left", display: "block", clear: "both", marginLeft: "2vw" }}>Features </h3>
            <li style={{ display: "block", clear: "both" }}>
                <ol style={{ textAlign: "left" }}> Click on the checkboxes to enable the filter you want to apply. For filters which can take more than 1 input (Acceptances,Rejections,Majors,Ecs) you can <strong>Ctrl+click</strong> (or <strong>command click </strong> on mac) to choose multiple inputs.
                </ol>

                <ol style={{ textAlign: "left" }}>
                    <p>Each filter you click is an AND operator - this means that the filter will show the intersection of your filters.
                        <br /> For example: if your inputs are Acceptances: Harvard, Princeton and SAT: 1550-1600. This will only show people who got in to <strong>both</strong> Harvard and Princeton <strong>and</strong> also got an SAT score of 1550 to 1600.
                        <br /> Do note that the SAT and ACT filters are inclusive of the tail end values.
                    </p>
                </ol>
                <ol style={{ textAlign: "left" }}>
                    <p>You can click on parts of the graph to bring up a list of links to reddit posts which that part of the graph pertains to.
                        <br /> For example, if you applied some filters and click on the Male portion of the first graph it will bring up a list of links to reddit posts where the applicant was a Male and also satisfies the filters you set.
                        <br /> Note that on the first launch of the site, sometimes you'll have to click twice for the list to show up - it's just a bit glitchy.
                    </p>
                </ol>
            </li>
        </div>

    )
}

export default Infotab