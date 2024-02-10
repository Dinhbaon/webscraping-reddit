import * as React from 'react';
import './Filters.css'
import GenderFilter from './GenderFilter';
import MajorFilter from './MajorFilter';
import { AdmissionData } from '../App';
import SatFilter from './SatFilter';
import AcceptanceFilter from './AcceptanceFilter';
import { useContext, useEffect, useState } from 'react';
import { DataContext } from '../context';
import useApplyFilters from './useApplyFilters';
import ActFilter from './ActFilter';
import RejectionFilter from './RejectionFilter';
import ExtracurricularFilter from './ExtracurricularsFilter';
import { isMobile } from 'react-device-detect';

const Filter = ({ chartType, admissionData, setAdmissionData }: { chartType: string[], admissionData: AdmissionData, setAdmissionData: React.Dispatch<React.SetStateAction<AdmissionData>> }) => {
    let filters = ['gender', 'sat', 'act', 'major', 'acceptances', 'rejections', 'ecs']

    const [applicableFilters, setApplicableFilters] = useState({
        'gender': (admissionData: AdmissionData) => { return admissionData },
        'sat': (admissionData: AdmissionData) => { return admissionData },
        'act': (admissionData: AdmissionData) => { return admissionData },
        'major': (admissionData: AdmissionData) => { return admissionData },
        'acceptances': (admissionData: AdmissionData) => { return admissionData },
        'rejections': (admissionData: AdmissionData) => { return admissionData },
        'ecs': (admissionData: AdmissionData) => { return admissionData }

    })

    const admissionDataConstant = useContext(DataContext)

    useEffect(() => {
        useApplyFilters(admissionDataConstant['admissionData'], setAdmissionData, (Object.values(applicableFilters) as FilterFunction[]))
    }, [applicableFilters])

    let filtersComponent = []

    filters = filters.filter((filter) => !chartType.includes(filter))
    if (filters.includes('gender')) {
        filtersComponent.push(<div className='filter'><GenderFilter
            setApplicableFilters={setApplicableFilters}
            chartType={chartType} ></GenderFilter></div>)

    }

    if (filters.includes('major')) {
        filtersComponent.push(<div className='filter'><MajorFilter
            setApplicableFilters={setApplicableFilters}
            chartType={chartType} ></MajorFilter></div>)
    }

    if (filters.includes('rejections') && filters.includes('acceptances')) {
        filtersComponent.push(<div className='filter'><RejectionFilter
            setApplicableFilters={setApplicableFilters}
            chartType={chartType}></RejectionFilter></div>)
        filtersComponent.push(<div className='filter'><AcceptanceFilter
            setApplicableFilters={setApplicableFilters}
            chartType={chartType}></AcceptanceFilter></div>)
    }

    if (filters.includes('sat') && filters.includes('act')) {
        filtersComponent.push(<div className='filter'>
            <SatFilter setApplicableFilters={setApplicableFilters}
                chartType={chartType}></SatFilter></div>
            , <div className='filter'>
                <ActFilter setApplicableFilters={setApplicableFilters}
                    chartType={chartType}></ActFilter></div>)
    }

    if (filters.includes('ecs')) {
        filtersComponent.push(<div className='filter'><ExtracurricularFilter
            setApplicableFilters={setApplicableFilters}
            chartType={chartType}></ExtracurricularFilter></div>)

    }




    return (
        <div>
            {isMobile ?
                null
                : <div className='filterContainer'>
                    {filtersComponent}
                </div>
            }
        </div>

    )

}
export default Filter
export type FilterFunction = (admissionData: AdmissionData) => AdmissionData;