import { Checkbox, FormControl, InputLabel, MenuItem, Select, SelectChangeEvent, Typography } from "@mui/material"
import { useContext, useEffect, useState } from "react"
import { unilist } from "./FilterOptions"
import React from "react"
import { AdmissionData } from "../App"
import { DataContext } from "../context"
import useFilter from "./useFilter"

const RejectionFilter =({ setApplicableFilters, chartType }: { setApplicableFilters : React.Dispatch<React.SetStateAction<{
  gender: (admissionData: AdmissionData) => AdmissionData;
  sat: (admissionData: AdmissionData) => AdmissionData;
  act: (admissionData: AdmissionData) => AdmissionData;
  major: (admissionData: AdmissionData) => AdmissionData;
  acceptances: (admissionData: AdmissionData) => AdmissionData;
  rejections: (admissionData: AdmissionData) => AdmissionData;
  ecs: (admissionData: AdmissionData) => AdmissionData;
}>>, chartType: string[] }) => {

  let [rejections, setRejections] = useState<string[]>([])
  let [checkedRejections, setCheckedRejections] = useState<boolean>(false)




  const handleCheck = (event : React.ChangeEvent<HTMLInputElement>) => {

    setCheckedRejections(event.target.checked)


    if (event.target.checked == true) {
      const filter = (admissionDataInput : AdmissionData) => {
        return useFilter(admissionDataInput, chartType, 'rejections', rejections)
      }
      
      setApplicableFilters((prevState=>({ ...prevState, 'rejections': filter})))
    } else if (event.target.checked == false) {
      const filter = (admissionDataInput : AdmissionData) => {
        return admissionDataInput
      }
      setApplicableFilters((prevState=>({ ...prevState, 'rejections': filter})))
    }

  }

  const handleChange = (event: SelectChangeEvent<typeof rejections>) => {

    let chosenUni = typeof event.target.value === 'string' ? event.target.value.split(',') : event.target.value

    setRejections(chosenUni)

    const filter = (admissionDataInput : AdmissionData) => {
      return useFilter(admissionDataInput, chartType, 'rejections', chosenUni)
    }

    setApplicableFilters((prevState) =>({ ...prevState, 'rejections': filter}))

  };


    let uniOptions = unilist.map(acceptances => <MenuItem value={acceptances} key={acceptances}>{acceptances}</MenuItem>)
    return (
        <div>
        <div style={{  display: 'flex', justifyContent: 'center', alignContent: 'center',     alignItems: 'center'}}>
            <Checkbox   checked={checkedRejections} onChange={handleCheck} />
            <Typography >Rejections:</Typography>  
        </div>
            {checkedRejections ? 
            <FormControl fullWidth>
                <InputLabel id="demo-simple-select-label">Rejections</InputLabel>
                <Select
                    labelId="demo-simple-select-label"
                    id="demo-simple-select"
                    value={rejections}
                    label="acceptance"
                    onChange={handleChange}
                    multiple
                >
                    {uniOptions}
                </Select>
            </FormControl>
            : null }
        </div>
    )
}
export default RejectionFilter