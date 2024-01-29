import { AdmissionData } from "../App";

const useFilter = (admissionData : AdmissionData, loChartType : string[], filterType : string, filterBoundary : string[] | number[]) => {

  if (filterType != 'sat' && filterType != 'act') {
    let retval = admissionData
    loChartType.forEach((chartType)=>{
      let index = Object.entries(admissionData[filterType as keyof AdmissionData]).filter(([ , lofilterBoundary ]) =>
          filterBoundary.map(x => (x as string).toLowerCase()).every(chosenBounds =>
              (lofilterBoundary as string[]).includes(chosenBounds.toLowerCase())
          )
      ).map(([ k ]) => k);

      let filtered = Object.fromEntries(
          Object.entries(admissionData[chartType as keyof AdmissionData]).filter(([ key ]) => index.includes(key))
      );
      retval = {...retval, [chartType as keyof AdmissionData]: filtered }
    })



      return retval;
  } else {
    let retval = admissionData
    loChartType.forEach((chartType)=>{
      let index = Object.entries(admissionData[filterType as keyof AdmissionData]).filter(([, i]) => i < filterBoundary[0] || i> filterBoundary[1] || i == "[]" ).map(([k]) => k);
      let filtered = Object.fromEntries(
          Object.entries(admissionData[(chartType as keyof AdmissionData)]).filter(
              ([key,])=> !index.includes(key)
          )
      )
      retval = {...retval, [chartType as keyof AdmissionData]: filtered}
    })


    return retval;
  }

}


export default useFilter