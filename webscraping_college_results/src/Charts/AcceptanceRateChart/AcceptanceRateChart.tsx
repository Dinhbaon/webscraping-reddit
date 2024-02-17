import { Bar, getElementsAtEvent } from "react-chartjs-2";
import { Chart as ChartJS, ArcElement, Tooltip, Legend, Title, SubTitle, CategoryScale, registerables } from 'chart.js';
import ChartDataLabels from 'chartjs-plugin-datalabels';
import Filter from '../../Filters/Filters'
import '../.././App.css'
import { MouseEvent, useContext, useEffect, useMemo, useRef, useState } from "react";

import { DataContext } from "../../context";
import UrlTab from "../../UrlTab/UrlTab";
import { FormControl, FormControlLabel, FormGroup, InputLabel, MenuItem, Radio, RadioGroup, Select, Slider, Typography } from "@mui/material";
import AcceptanceFilter from "../../Filters/AcceptanceFilter";
import { unilist } from "../../Filters/FilterOptions";
ChartJS.register(ArcElement, Tooltip, Legend, ChartDataLabels, Title, SubTitle, CategoryScale, ...registerables )

const AcceptanceRateChart = () => {
    let admissionData = useContext(DataContext)
    const [admissionDataCopy, setAdmissionDataCopy] = useState(admissionData['admissionData'])
    const [acceptanceRate, setAcceptanceRate] = useState<number[]>()
    const [selectedUnis, setSelectedUnis] = useState<string[]>(['Harvard', 'Princeton'])
    const [loUrl, setLoUrl] = useState<string[]>([])
    const [opened, setOpened] = useState(false)
    const [testScoreType, setTestScoreType] = useState<string>('sat')
    const [scoreRange, setScoreRange] = useState<number[]>([800, 1600])
    const chartRef = useRef();
    useMemo(() => {
        setAdmissionDataCopy(admissionData['admissionData']);
      }, [admissionData]);

    useEffect(()=>{
        let acceptcount = selectedUnis.map((x : string)=>Object.values(admissionDataCopy['acceptances']).filter((i)=>i.includes(x.toLowerCase())).length)
        let rejectcount = selectedUnis.map((x : string) =>Object.values(admissionDataCopy['rejections']).filter((i)=>i.includes(x.toLowerCase())).length)        
        setAcceptanceRate(acceptcount.map((x,i)=>Math.round(x/(x+rejectcount[i])*100)))
    }, [selectedUnis, admissionDataCopy])

    useEffect(()=>{
    }, [acceptanceRate])
    
    let uniOptions = unilist.map(acceptances => <MenuItem value={acceptances} key={acceptances}>{acceptances}</MenuItem>)

    const data = {
        labels: selectedUnis, 
        datasets: [
            {
                data: acceptanceRate, 
                        
                backgroundColor: [
                    'rgba(54, 162, 235, 1)', 
                    'rgba(255, 99, 132, 1)',
                    'rgba(255, 206, 86, 1)'
                ]
            }

        ],
        borderWidth: 1,
        barPercentage: 1,
        categoryPercentage:1
    }

    const options = {
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
                    // text: 'n=' + Object.values(countMap).reduce((partialSum, acc)=> partialSum + acc, 0)
                }

        }, 
        responsive: true
    
    }

    const onClick = (event: MouseEvent<HTMLCanvasElement, MouseEvent>) => {
        const datasetIndexNum =  getElementsAtEvent(chartRef.current, event)[0].datasetIndex
        const dataPoint = getElementsAtEvent(chartRef.current, event)[0].index
        let chosenIndex = Object.keys(admissionDataCopy['acceptances']).filter((id : string) => 
            admissionDataCopy['acceptances'][id].includes(data.labels[dataPoint].toLowerCase()))
        setLoUrl(Object.values(chosenIndex.map(x=> {return admissionDataCopy['url'][x]}).reverse()))
        setOpened(true)
    }

    const handleChange = (event: Event, newValue: string | string[]) => {
        let chosenMajor = typeof event.target.value === 'string' ? event.target.value.split(',') : event.target.value

        setSelectedUnis(chosenMajor);

    }
    return (
        <div>
            <div className={'container'}>
                <div>
                    <Filter chartType={['acceptances', testScoreType]} admissionData={admissionDataCopy} setAdmissionData={setAdmissionDataCopy}></Filter>
                </div>
                <div className="graph"> 
                        <Bar data={data}
                            ref={chartRef}
                            options={options}
                            height="500px"
                            width="500px"
                            onClick={onClick}
                        />
                </div>
                <div className="urlTab" style={{visibility: opened ? 'visible' : 'hidden'}}>
                    {opened ? <UrlTab loUrl={loUrl} setOpened={setOpened}></UrlTab>: null}
                </div>
            </div>

            <div>
            <div style={{display: 'flex', justifyContent: 'center', alignContent: 'center', alignItems: 'center', position: 'relative'}}>
                <Typography >Acceptances:</Typography>     
            </div>
            <div style={{width: '400px', transform: 'translateX(-50%)', left: '50%', position: 'relative'}}>
            <FormControl fullWidth>
                <InputLabel id="demo-simple-select-label">Acceptances</InputLabel>
                <Select
                    labelId="demo-simple-select-label"
                    id="demo-simple-select"
                    value={selectedUnis}
                    label="acceptance"
                    onChange={handleChange} 
                    multiple
                >
                    {uniOptions}
                </Select>
            </FormControl>
            </div>
            </div>

        </div>

    )
}

export default AcceptanceRateChart