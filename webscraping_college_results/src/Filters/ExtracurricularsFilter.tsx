import { Checkbox, FormControl, InputLabel, MenuItem, Select, SelectChangeEvent, Typography } from "@mui/material"
import { useContext, useEffect, useState } from "react"
import { eclist } from "./FilterOptions"
import React from "react"
import { AdmissionData } from "../App"
import { DataContext } from "../context"
import useFilter from "./useFilter"

const ExtracurricularFilter =({ setApplicableFilters, chartType }: { setApplicableFilters : React.Dispatch<React.SetStateAction<{
  gender: (admissionData: AdmissionData) => AdmissionData;
  sat: (admissionData: AdmissionData) => AdmissionData;
  act: (admissionData: AdmissionData) => AdmissionData;
  major: (admissionData: AdmissionData) => AdmissionData;
  acceptances: (admissionData: AdmissionData) => AdmissionData;
  rejections: (admissionData: AdmissionData) => AdmissionData;
  ecs: (admissionData: AdmissionData) => AdmissionData;
}>>, chartType: string[] }) => {

  let [extracurriculars, setExtracurriculars] = useState<string[]>([])
  let [checkedExtracurriculars, setCheckedExtracurriculars] = useState<boolean>(false)




  const handleCheck = (event : React.ChangeEvent<HTMLInputElement>) => {

    setCheckedExtracurriculars(event.target.checked)


    if (event.target.checked == true) {
      const filter = (admissionDataInput : AdmissionData) => {
        return useFilter(admissionDataInput, chartType, 'ecs', extracurriculars)
      }
      setApplicableFilters((prevState=>({ ...prevState, 'ecs': filter})))
    } else if (event.target.checked == false) {
      const filter = (admissionDataInput : AdmissionData) => {
        return admissionDataInput
      }
      setApplicableFilters((prevState=>({ ...prevState, 'ecs': filter})))
    }

  }

  const handleChange = (event: SelectChangeEvent<typeof extracurriculars>) => {

    let chosenMajor = typeof event.target.value === 'string' ? event.target.value.split(',') : event.target.value

    setExtracurriculars(chosenMajor)

    const filter = (admissionDataInput : AdmissionData) => {
      return useFilter(admissionDataInput, chartType, 'ecs', chosenMajor)
    }

    setApplicableFilters((prevState) =>({ ...prevState, 'ecs': filter}))

  };


    let uniOptions = eclist.map(extracurriculars => <MenuItem value={extracurriculars} key={extracurriculars}>{extracurriculars}</MenuItem>)
    return (
        <div>
        <div style={{  display: 'flex', justifyContent: 'center', alignContent: 'center',     alignItems: 'center'}}>
            <Checkbox   checked={checkedExtracurriculars} onChange={handleCheck} />
            <Typography >Extracurriculars:</Typography>  
        </div>
            {checkedExtracurriculars ? 
            <FormControl fullWidth>
                <InputLabel id="demo-simple-select-label">Extracurriculars</InputLabel>
                <Select
                    labelId="demo-simple-select-label"
                    id="demo-simple-select"
                    value={extracurriculars}
                    label="extracurriculars"
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
export default ExtracurricularFilter