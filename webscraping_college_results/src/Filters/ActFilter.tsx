import { Checkbox, FormControl, InputLabel, MenuItem, Select, SelectChangeEvent, Slider, Typography } from "@mui/material"
import { useContext, useState } from "react"
import { majorlist } from "./FilterOptions"
import React from "react"
import { AdmissionData } from "../App"
import { DataContext } from "../context"
import useFilter from "./useFilter"

const ActFilter = ({ setApplicableFilters, chartType }: { setApplicableFilters : React.Dispatch<React.SetStateAction<{
    gender: (admissionData: AdmissionData) => AdmissionData;
    sat: (admissionData: AdmissionData) => AdmissionData;
    act: (admissionData: AdmissionData) => AdmissionData;
    major: (admissionData: AdmissionData) => AdmissionData;
    acceptances: (admissionData: AdmissionData) => AdmissionData;
    rejections: (admissionData: AdmissionData) => AdmissionData;
    ecs: (admissionData: AdmissionData) => AdmissionData;
  }>>, chartType: string[] }) => {

    let [checkedAct, setCheckedAct] = useState<boolean>(false)
    let [actRange, setActRange] = useState<number[]>([18, 36])


    const handleCheck = (event : React.ChangeEvent<HTMLInputElement>) =>{ 
        setCheckedAct(event.target.checked)

        if (event.target.checked == true) {
            const filter = (admissionDataInput : AdmissionData) => {
              return useFilter(admissionDataInput, chartType, 'act', actRange)
            }
            setApplicableFilters((prevState=>({ ...prevState, 'act': filter})))
        } 
        else if (event.target.checked == false) {
            const filter = (admissionDataInput : AdmissionData) => {
              return admissionDataInput
            }
            setActRange([18, 36])
            setApplicableFilters((prevState=>({ ...prevState, 'act': filter})))
          }
    }

    const handleChange = (event: Event, newValue: number | number[]) => {
        setActRange(newValue as number[]);

        const filter = (admissionDataInput : AdmissionData) => {
            return useFilter(admissionDataInput, chartType, 'act', (newValue as number[]))
          }
      
          setApplicableFilters((prevState) =>({ ...prevState, 'act': filter}))
      };

    return (
    <div>
        <div style={{  display: 'flex', justifyContent: 'center', alignContent: 'center',     alignItems: 'center'}}>
        <Checkbox   checked={checkedAct} onChange={handleCheck} />
        <Typography >ACT Range:</Typography>     
        </div>        


        {checkedAct ?   <Slider
        getAriaLabel={() => 'ACT range'}
        value={actRange}
        min={18}
        max={36} 
        step={1}
        onChange={handleChange}
        
      /> : null}
    <div style={{  display: 'flex', justifyContent: 'center', alignContent: 'center'}}>              
        {checkedAct ? <Typography> {actRange[0] + '-' + actRange[1]} </Typography> : null } 
    </div> 



    </div>
    )
}
export default ActFilter