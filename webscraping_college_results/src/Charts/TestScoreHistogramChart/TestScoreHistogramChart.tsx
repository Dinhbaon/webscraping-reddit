import { Bar, getElementsAtEvent } from "react-chartjs-2";
import { Chart as ChartJS, ArcElement, Tooltip, Legend, Title, SubTitle, CategoryScale, registerables } from 'chart.js';
import ChartDataLabels from 'chartjs-plugin-datalabels';
import Filter from '../../Filters/Filters'
import '../.././App.css'
import { MouseEvent, useContext, useEffect, useMemo, useRef, useState } from "react";

import { DataContext } from "../../context";
import UrlTab from "../../UrlTab/UrlTab";
import { FormControlLabel, FormGroup, Radio, RadioGroup, Slider, Typography } from "@mui/material";
ChartJS.register(ArcElement, Tooltip, Legend, ChartDataLabels, Title, SubTitle, CategoryScale, ...registerables)


const TestScoreHistogramChart = () => {
    let admissionData = useContext(DataContext)
    const [testScoreType, setTestScoreType] = useState<string>('sat')
    const [scoreRange, setScoreRange] = useState<number[]>([800, 1600])
    const [admissionDataCopy, setAdmissionDataCopy] = useState(admissionData['admissionData'])
    const [loUrl, setLoUrl] = useState<string[]>([])
    const [opened, setOpened] = useState(false)
    const [countMap, setCountMap] = useState<CountMap>({})
    const [initialMap, setInitialMap] = useState<CountMap>({})


    const chartRef = useRef();
    useMemo(() => {
        setAdmissionDataCopy(admissionData['admissionData']);
        const valuesArray: string[] = Object.values(admissionData['admissionData'][testScoreType]).map((score)=>score.replace(/\D/g, "")).filter((score)=> score!='');
        let tempMap: CountMap = {}
        valuesArray.forEach((value) => {
            if (typeof value === 'string' && value !== "[]") {
                if (tempMap[value]) {
                    tempMap[value] += 1;
                } else {
                    tempMap[value] = 1;
                }
            }
        });
        setInitialMap(tempMap)
        setCountMap(tempMap)
    }, [admissionData, testScoreType]);
    let scoreData: any = admissionDataCopy[testScoreType]

    type CountMap = { [key: string]: number };


    useEffect(() => {
        if (testScoreType == 'sat') {
            setScoreRange([800, 1600])
        } else if (testScoreType == 'act') {
            setScoreRange([18, 36])
        }
    }, [testScoreType])




    const data = {
        labels: Object.keys(countMap).map((score)=>score.replace(/\D/g, "")),
        datasets: [
            {
                data: Object.values(countMap),

                backgroundColor: [
                    'rgba(54, 162, 235, 0.8)',
                ]
            }

        ],
        borderWidth: 1,
        barPercentage: 1,
        categoryPercentage: 1
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
                text: 'n=' + Object.values(countMap).reduce((partialSum, acc) => partialSum + acc, 0)
            }

        },
        responsive: true

    }

    const onClick = (event: MouseEvent<HTMLCanvasElement, MouseEvent>) => {
        const datasetIndexNum = getElementsAtEvent(chartRef.current, event)[0].datasetIndex
        const dataPoint = getElementsAtEvent(chartRef.current, event)[0].index


        let chosenIndex = Object.keys(admissionDataCopy[testScoreType]).filter((id: string) => admissionDataCopy[testScoreType][id] == data.labels[dataPoint])
        setLoUrl(Object.values(chosenIndex.map(x => { return admissionDataCopy['url'][x] }).reverse()))
        setOpened(true)
    }

    const handleChange = (event: Event, newValue: number | number[]) => {
        setCountMap(initialMap)
        setScoreRange(newValue as number[]);

    };

    useEffect(() => {
        setCountMap(Object.fromEntries(Object.entries(countMap).filter((entries) => {
            return scoreRange[0] <= Number(entries[0]) && Number(entries[0]) <= scoreRange[1]
        }
        )))
    }, [scoreRange])

    return (
        <div>
            <div className={'container'}>
                <div>
                    <Filter chartType={[testScoreType]} admissionData={admissionDataCopy} setAdmissionData={setAdmissionDataCopy}></Filter>
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
                <div className="urlTab" style={{ visibility: opened ? 'visible' : 'hidden' }}>
                    {opened ? <UrlTab loUrl={loUrl} setOpened={setOpened}></UrlTab> : null}
                </div>
            </div>
            <div>
                {{
                    ...testScoreType == 'sat' ?
                        <div>
                            <div style={{ display: 'flex', justifyContent: 'center', alignContent: 'center', alignItems: 'center' }}>
                                <Typography >SAT Range:</Typography>
                            </div>
                            <div style={{ transform: 'translateX(-50%)', left: '50%', width: '400px', position: "relative" }}>
                                <Slider
                                    getAriaLabel={() => 'SAT range'}
                                    display="flex"
                                    direction="row"
                                    alignItems="center"
                                    justifyContent="center"
                                    value={scoreRange}
                                    min={800}
                                    max={1600}
                                    step={10}
                                    onChange={handleChange}
                                />
                            </div>

                            <div style={{ display: 'flex', justifyContent: 'center', alignContent: 'center' }}>
                                <Typography> {scoreRange[0] + '-' + scoreRange[1]} </Typography>
                            </div>
                        </div> :
                        <div>
                            <div style={{ display: 'flex', justifyContent: 'center', alignContent: 'center', alignItems: 'center' }}>
                                <Typography >ACT Range:</Typography>
                            </div>
                            <div style={{ transform: 'translateX(-50%)', left: '50%', width: '400px', position: "relative" }}>
                                <Slider
                                    getAriaLabel={() => 'SAT range'}
                                    display="flex"
                                    direction="row"
                                    alignItems="center"
                                    justifyContent="center"
                                    value={scoreRange}
                                    min={18}
                                    max={36}
                                    step={10}
                                    onChange={handleChange}
                                />
                            </div>

                            <div style={{ display: 'flex', justifyContent: 'center', alignContent: 'center' }}>
                                <Typography> {scoreRange[0] + '-' + scoreRange[1]} </Typography>
                            </div>
                        </div>
                }}
            </div >
            <div style={{ display: 'flex', justifyContent: 'center', alignContent: 'center', alignItems: 'center' }}>
                <RadioGroup defaultValue={'sat'} row onChange={(event) => setTestScoreType(event.target.value)}>
                    <FormControlLabel  value='sat' control={<Radio onClick={() => setTestScoreType('sat')}  />} label="SAT" />
                    <FormControlLabel value='act' control={<Radio onClick={() => setTestScoreType('act')} />} label="ACT" />
                </RadioGroup>
            </div>
        </div>


    )


}

export default TestScoreHistogramChart