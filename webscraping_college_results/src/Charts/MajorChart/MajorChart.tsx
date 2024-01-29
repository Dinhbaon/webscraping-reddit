// @ts-nocheck

import { Bar, getElementsAtEvent } from "react-chartjs-2";
import { Chart as ChartJS, ArcElement, Tooltip, Legend, Title, SubTitle, CategoryScale, registerables } from 'chart.js';
import ChartDataLabels from 'chartjs-plugin-datalabels';
import Filter from '../../Filters/Filters'
import '../.././App.css'
import { MouseEvent, useContext, useEffect, useMemo, useRef, useState } from "react";

import { DataContext } from "../../context";
import UrlTab from "../../UrlTab/UrlTab";
ChartJS.register(ArcElement, Tooltip, Legend, ChartDataLabels, Title, SubTitle, CategoryScale, ...registerables )



const MajorChart = () => { 
    let admissionData = useContext(DataContext)
    const [admissionDataCopy, setAdmissionDataCopy] = useState(admissionData['admissionData'])
    const [loUrl, setLoUrl] = useState<string[]>([])
    const [opened, setOpened] = useState(false)

    const chartRef = useRef();
    useMemo(() => {
        setAdmissionDataCopy(admissionData['admissionData']);
      }, [admissionData]);

      const majorCount: { [key: string]: number } = {};
      const majorList: { [key: string]: string } = admissionDataCopy['major'];
      
      Object.values(majorList).forEach(function (x: string) {
        majorCount[x] = (majorCount[x] || 0) + 1;
      });
      
    //   const number: number = Object.values(majorCount).reduce((a, b) => a + b);
      
      const sortedMajorCount: { [key: string]: number } = Object.fromEntries(
        Object.entries(majorCount).sort(([, a], [, b]) => b - a)
      );
    const data = {
        labels: Object.keys(sortedMajorCount), 
        datasets: [
            {
                data: Object.values(sortedMajorCount), 
                        
                backgroundColor: [
                            'rgba(54, 162, 235, 1)', 
                            'rgba(255, 99, 132, 1)',
                            'rgba(255, 206, 86, 1)'
                        ]
            }

        ]
    }

    const options = {
        indexAxis: 'y' as const,
        plugins: {
            legend: {
                display: false
              }, 
            customCanvasBackgroundColor: {
                color: 'lightGreen',
              }, 
            datalabels: {
                display: true,
                color: 'white', 
                font: {
                    size: '12px'
                }
             }, 
             title: {
                    display: true,
                    text: 'Demographics - Major Makeup'
                }, 
            subtitle: {
                    display: true,
                    text: 'n=' + Object.keys(admissionDataCopy['major']).length
                }

        }, 
        responsive: true
    
    }

    const onClick = (event: MouseEvent<HTMLCanvasElement, MouseEvent>) => {
        console.log(getElementsAtEvent(chartRef.current, event)[0]);
        const datasetIndexNum =  getElementsAtEvent(chartRef.current, event)[0].datasetIndex
        const dataPoint = getElementsAtEvent(chartRef.current, event)[0].index


        let chosenIndex = Object.keys(admissionDataCopy['major']).filter((id : string) => admissionDataCopy['major'][id] == data.labels[dataPoint])
        setLoUrl(Object.values(chosenIndex.map(x=> {return admissionDataCopy['url'][x]}).reverse()))
        console.log(Object.values(chosenIndex.map(x=> {return admissionDataCopy['url'][x]}).reverse()))
        setOpened(true)
    }

    return (
        <div className={'container'}>
            <div>
                <Filter chartType={['major']} admissionData={admissionDataCopy} setAdmissionData={setAdmissionDataCopy}></Filter>
            </div>
            <div className="graph"  style={{overflow: 'scroll'}}> 
                <div style={{height: '5000px'}}>
                    <Bar data={data}
                        ref={chartRef}
                        options={options}
                        height="5000px"
                        width="500px"
                        onClick={onClick}
                        />
                </div>
            </div>
            <div className="urlTab" style={{visibility: opened ? 'visible' : 'hidden'}}>
                {opened ? <UrlTab loUrl={loUrl} setOpened={setOpened}></UrlTab>: null}
            </div>
        </div>

            
        )
    

}

export default MajorChart