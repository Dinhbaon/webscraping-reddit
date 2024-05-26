import { Checkbox, Slider, Typography } from "@mui/material"
import { useState } from "react"
import React from "react"
import { AdmissionData } from "../App"
import useFilter from "./useFilter"

const SatFilter = ({ setApplicableFilters, chartType }: { setApplicableFilters : React.Dispatch<React.SetStateAction<{
    gender: (admissionData: AdmissionData) => AdmissionData;
    sat: (admissionData: AdmissionData) => AdmissionData;
    act: (admissionData: AdmissionData) => AdmissionData;
    major: (admissionData: AdmissionData) => AdmissionData;
    acceptances: (admissionData: AdmissionData) => AdmissionData;
    rejections: (admissionData: AdmissionData) => AdmissionData;
    ecs: (admissionData: AdmissionData) => AdmissionData;
  }>>, chartType: string[] }) => {

    let [checkedSat, setCheckedSat] = useState<boolean>(false)
    let [satRange, setSatRange] = useState<number[]>([800, 1600])


    const handleCheck = (event : React.ChangeEvent<HTMLInputElement>) =>{ 
        setCheckedSat(event.target.checked)

        if (event.target.checked == true) {
            const filter = (admissionDataInput : AdmissionData) => {
              return useFilter(admissionDataInput, chartType, 'sat', satRange)
            }
            setApplicableFilters((prevState=>({ ...prevState, 'sat': filter})))
        } 
        else if (event.target.checked == false) {
            const filter = (admissionDataInput : AdmissionData) => {
              return admissionDataInput
            }
            setSatRange([800, 1600])
            setApplicableFilters((prevState=>({ ...prevState, 'sat': filter})))
          }
    }

    const handleChange = (_event: Event, newValue: number | number[]) => {
        setSatRange(newValue as number[]);

        const filter = (admissionDataInput : AdmissionData) => {
            return useFilter(admissionDataInput, chartType, 'sat', (newValue as number[]))
          }
      
          setApplicableFilters((prevState) =>({ ...prevState, 'sat': filter}))
      };

    return (
    <div>
        <div style={{  display: 'flex', justifyContent: 'center', alignContent: 'center',     alignItems: 'center'}}>
        <Checkbox   checked={checkedSat} onChange={handleCheck} />
        <Typography >SAT Range:</Typography>     
        </div>        


        {checkedSat ?   <Slider
        getAriaLabel={() => 'SAT range'}
        value={satRange}
        min={800}
        max={1600} 
        step={10}
        onChange={handleChange}
        
      /> : null}
    <div style={{  display: 'flex', justifyContent: 'center', alignContent: 'center'}}>              
        {checkedSat ? <Typography> {satRange[0] + '-' + satRange[1]} </Typography> : null } 
    </div> 



    </div>
    )
}
export default SatFilter