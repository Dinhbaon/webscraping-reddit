import { Checkbox, FormControl, InputLabel, MenuItem, Select, SelectChangeEvent, Typography } from "@mui/material"
import { useState } from "react"
import { majorlist } from "./FilterOptions"
import React from "react"
import { AdmissionData } from "../App"
import useFilter from "./useFilter"

const MajorFilter = ({ setApplicableFilters, chartType }: { setApplicableFilters : React.Dispatch<React.SetStateAction<{
  gender: (admissionData: AdmissionData) => AdmissionData;
  sat: (admissionData: AdmissionData) => AdmissionData;
  act: (admissionData: AdmissionData) => AdmissionData;
  major: (admissionData: AdmissionData) => AdmissionData;
  acceptances: (admissionData: AdmissionData) => AdmissionData;
  rejections: (admissionData: AdmissionData) => AdmissionData;
  ecs: (admissionData: AdmissionData) => AdmissionData;
}>>, chartType: string[] }) => {

  let [major, setMajor] = useState<string[]>([])
  let [checkedMajor, setCheckedMajor] = useState<boolean>(false)




  const handleCheck = (event : React.ChangeEvent<HTMLInputElement>) => {

    setCheckedMajor(event.target.checked)


    if (event.target.checked == true) {
      const filter = (admissionDataInput : AdmissionData) => {
        return useFilter(admissionDataInput, chartType, 'major', major)
      }
      setApplicableFilters((prevState=>({ ...prevState, 'major': filter})))
    } else if (event.target.checked == false) {
      const filter = (admissionDataInput : AdmissionData) => {
        return admissionDataInput
      }
      setApplicableFilters((prevState=>({ ...prevState, 'major': filter})))
    }

  }

  const handleChange = (event: SelectChangeEvent<typeof major>) => {

    let chosenMajor = typeof event.target.value === 'string' ? event.target.value.split(',') : event.target.value

    setMajor(chosenMajor)

    const filter = (admissionDataInput : AdmissionData) => {
      return useFilter(admissionDataInput, chartType, 'major', chosenMajor)
    }

    setApplicableFilters((prevState) =>({ ...prevState, 'major': filter}))

  };


  let majorOptions = majorlist.map(major => <MenuItem value={major} key={major}>{major}</MenuItem>)
  return (

  <div>
  <div style={{  display: 'flex', justifyContent: 'center', alignContent: 'center',     alignItems: 'center'}}>
    <Checkbox   checked={checkedMajor} onChange={handleCheck} />
    <Typography >Major:</Typography>     
  </div>        
  {checkedMajor ? 
      <FormControl fullWidth>
        <InputLabel id="demo-simple-select-label">Major</InputLabel>
        <Select
          labelId="demo-simple-select-label"
          id="demo-simple-select"
          value={major}
          label="Major"
          onChange={handleChange}
          multiple
        >
          {majorOptions}
        </Select>
      </FormControl>
      : null}

    </div>
  )
}
export default MajorFilter