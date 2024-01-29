import { Checkbox, FormControl, InputLabel, MenuItem, Select, SelectChangeEvent, Typography } from "@mui/material"
import { useContext, useEffect, useState } from "react"
import { unilist } from "./FilterOptions"
import React from "react"
import { AdmissionData } from "../App"
import { DataContext } from "../context"
import useFilter from "./useFilter"

const AcceptanceFilter =({ setApplicableFilters, chartType }: { setApplicableFilters : React.Dispatch<React.SetStateAction<{
  gender: (admissionData: AdmissionData) => AdmissionData;
  sat: (admissionData: AdmissionData) => AdmissionData;
  act: (admissionData: AdmissionData) => AdmissionData;
  major: (admissionData: AdmissionData) => AdmissionData;
  acceptances: (admissionData: AdmissionData) => AdmissionData;
  rejections: (admissionData: AdmissionData) => AdmissionData;
  ecs: (admissionData: AdmissionData) => AdmissionData;
}>>, chartType: string[] }) => {

  let [acceptances, setAcceptances] = useState<string[]>([])
  let [checkedAcceptances, setCheckedAcceptances] = useState<boolean>(false)




  const handleCheck = (event : React.ChangeEvent<HTMLInputElement>) => {

    setCheckedAcceptances(event.target.checked)


    if (event.target.checked == true) {
      const filter = (admissionDataInput : AdmissionData) => {
        return useFilter(admissionDataInput, chartType, 'acceptances', acceptances)
      }
      setApplicableFilters((prevState=>({ ...prevState, 'acceptances': filter})))
    } else if (event.target.checked == false) {
      const filter = (admissionDataInput : AdmissionData) => {
        return admissionDataInput
      }
      setApplicableFilters((prevState=>({ ...prevState, 'acceptances': filter})))
    }

  }

  const handleChange = (event: SelectChangeEvent<typeof acceptances>) => {

    let chosenMajor = typeof event.target.value === 'string' ? event.target.value.split(',') : event.target.value

    setAcceptances(chosenMajor)

    const filter = (admissionDataInput : AdmissionData) => {
      return useFilter(admissionDataInput, chartType, 'acceptances', chosenMajor)
    }

    setApplicableFilters((prevState) =>({ ...prevState, 'acceptances': filter}))

  };


    let uniOptions = unilist.map(acceptances => <MenuItem value={acceptances} key={acceptances}>{acceptances}</MenuItem>)
    return (
        <div>
        <div style={{  display: 'flex', justifyContent: 'center', alignContent: 'center',     alignItems: 'center'}}>
            <Checkbox   checked={checkedAcceptances} onChange={handleCheck} />
            <Typography >Acceptances:</Typography>  
        </div>
            {checkedAcceptances ? 
            <FormControl fullWidth>
                <InputLabel id="demo-simple-select-label">Acceptances</InputLabel>
                <Select
                    labelId="demo-simple-select-label"
                    id="demo-simple-select"
                    value={acceptances}
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
export default AcceptanceFilter