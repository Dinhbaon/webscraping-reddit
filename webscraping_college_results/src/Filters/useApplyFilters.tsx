import { AdmissionData } from "../App";
import { FilterFunction } from "./Filters";

const useApplyFilters = (admissionData: AdmissionData, setAdmissionData : React.Dispatch<React.SetStateAction<AdmissionData>>, lofilters: FilterFunction[]) => {
    
    setAdmissionData(lofilters.reduce((acc, curval) => curval(acc), admissionData));
}
export default useApplyFilters