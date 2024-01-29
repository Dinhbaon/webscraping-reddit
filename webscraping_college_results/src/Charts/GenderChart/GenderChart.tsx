import { Doughnut, getDatasetAtEvent, getElementAtEvent, getElementsAtEvent } from "react-chartjs-2";
import { Chart as ChartJS, ArcElement, Tooltip, Legend, Title, SubTitle } from 'chart.js';
import ChartDataLabels from 'chartjs-plugin-datalabels';
import Filter from '../../Filters/Filters'
import '../.././App.css'
import { MouseEvent, useContext, useEffect, useMemo, useRef, useState } from "react";

import { DataContext } from "../../context";
import UrlTab from "../../UrlTab/UrlTab";
ChartJS.register(ArcElement, Tooltip, Legend, ChartDataLabels, Title, SubTitle)



const FetchGender = () => { 
    let admissionData = useContext(DataContext)
    const [admissionDataCopy, setAdmissionDataCopy] = useState(admissionData['admissionData'])
    const [loUrl, setLoUrl] = useState<string[]>([])
    const [opened, setOpened] = useState(false)

    const chartRef = useRef();
    useMemo(() => {
        setAdmissionDataCopy(admissionData['admissionData']);
      }, [admissionData]);


    const data = {
        labels: ['Male', 'Female', 'Other/LGBTQ+'], 
        datasets: [
            {
                data:  [Object.values(admissionDataCopy['gender']).filter(gender => gender == 'Male').length, 
                        Object.values(admissionDataCopy['gender']).filter(gender => gender == 'Female').length,
                        Object.values(admissionDataCopy['gender']).filter(gender => gender == 'Other/LGBTQ+').length], 
                        
                backgroundColor: [
                            'rgba(54, 162, 235, 1)', 
                            'rgba(255, 99, 132, 1)',
                            'rgba(255, 206, 86, 1)'
                        ]
            }

        ]
    }

    const options = {
        plugins: {
            customCanvasBackgroundColor: {
                color: 'lightGreen',
              }, 
            datalabels: {
                display: true,
                color: 'white', 
                font: {
                    size: '24px'
                }
             }, 
             title: {
                    display: true,
                    text: 'Demographics - Gender Makeup'
                }, 
            subtitle: {
                    display: true,
                    text: 'n=' + Object.keys(admissionDataCopy['gender']).length
                }

        }, 
        responsive: true
    
    }

    const onClick = (event: MouseEvent<HTMLCanvasElement, MouseEvent>) => {
        console.log(getElementsAtEvent(chartRef.current, event)[0]);
        const datasetIndexNum =  getElementsAtEvent(chartRef.current, event)[0].datasetIndex
        const dataPoint = getElementsAtEvent(chartRef.current, event)[0].index


        let chosenIndex = Object.keys(admissionDataCopy['gender']).filter((id : string) => admissionDataCopy['gender'][id] == data.labels[dataPoint])
        setLoUrl(Object.values(chosenIndex.map(x=> {return admissionDataCopy['url'][x]}).reverse()))
        console.log(Object.values(chosenIndex.map(x=> {return admissionDataCopy['url'][x]}).reverse()))
        setOpened(true)
    }

    return (
        <div className={'container'}>
            <div>
                <Filter chartType={['gender']} admissionData={admissionDataCopy} setAdmissionData={setAdmissionDataCopy}></Filter>
            </div>
            <div className="graph"> 
                <Doughnut data={data}
                    ref={chartRef}
                    options={options}
                    height="500px"
                    width="500px"
                    onClick={onClick}/>
            </div>
            <div className="urlTab" style={{visibility: opened ? 'visible' : 'hidden'}}>
                {opened ? <UrlTab loUrl={loUrl} setOpened={setOpened}></UrlTab>: null}
            </div>
        </div>

            
        )
    

}

export default FetchGender