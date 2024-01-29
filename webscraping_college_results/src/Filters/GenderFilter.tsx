import { Checkbox, FormControl, InputLabel, MenuItem, Select, SelectChangeEvent, Typography } from "@mui/material"
import { useContext, useEffect, useState } from "react"
import { majorlist } from "./FilterOptions"
import React from "react"
import { AdmissionData } from "../App"
import { DataContext } from "../context"
import useFilter from "./useFilter"
import useApplyFilters from "./useApplyFilters"

const GenderFilter = ({ setApplicableFilters, chartType }: { setApplicableFilters : React.Dispatch<React.SetStateAction<{
  gender: (admissionData: AdmissionData) => AdmissionData;
  sat: (admissionData: AdmissionData) => AdmissionData;
  act: (admissionData: AdmissionData) => AdmissionData;
  major: (admissionData: AdmissionData) => AdmissionData;
  acceptances: (admissionData: AdmissionData) => AdmissionData;
  rejections: (admissionData: AdmissionData) => AdmissionData;
  ecs: (admissionData: AdmissionData) => AdmissionData;
}>>, chartType: string[] }) => {

  let [gender, setGender] = useState<string[]>([])
  let [checkedGender, setCheckedGender] = useState<boolean>(false)




  const handleCheck = (event : React.ChangeEvent<HTMLInputElement>) => {

    setCheckedGender(event.target.checked)


    if (event.target.checked == true) {
      const filter = (admissionDataInput : AdmissionData) => {
        return useFilter(admissionDataInput, chartType, 'gender', gender)
      }
      setApplicableFilters((prevState=>({ ...prevState, 'gender': filter})))
    } else if (event.target.checked == false) {
      const filter = (admissionDataInput : AdmissionData) => {
        return admissionDataInput
      }
      setApplicableFilters((prevState=>({ ...prevState, 'gender': filter})))
    }

  }

  const handleChange = (event: SelectChangeEvent<typeof gender>) => {

    let chosenGender = typeof event.target.value === 'string' ? event.target.value.split(',') : event.target.value

    setGender(chosenGender)

    const filter = (admissionDataInput : AdmissionData) => {
      return useFilter(admissionDataInput, chartType, 'gender', chosenGender)
    }

    setApplicableFilters((prevState) =>({ ...prevState, 'gender': filter}))

  };


  let genderOptions = ['Male', 'Female', 'LGBTQ+/Others'].map(gender => <MenuItem value={gender} key={gender}>{gender}</MenuItem>)
  return (

  <div>
  <div style={{  display: 'flex', justifyContent: 'center', alignContent: 'center',     alignItems: 'center'}}>
    <Checkbox   checked={checkedGender} onChange={handleCheck} />
    <Typography >Gender:</Typography>     
  </div>        
  {checkedGender ? 
      <FormControl fullWidth>
        <InputLabel id="demo-simple-select-label">Gender</InputLabel>
        <Select
          labelId="demo-simple-select-label"
          id="demo-simple-select"
          value={gender}
          label="Gender"
          onChange={handleChange}
          multiple
        >
          {genderOptions}
        </Select>
      </FormControl>
      : null}

    </div>
  )
}
export default GenderFilter