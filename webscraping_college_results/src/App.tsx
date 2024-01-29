import { Suspense, useEffect, useState } from 'react'
import './App.css'
import GenderChart from './Charts/GenderChart/GenderChart'
import Navbar from './Navbar/Navbar'
import AdmissionDataProvider from './context'
import MajorChart from './Charts/MajorChart/MajorChart'
import AcceptanceRateChart from './Charts/AcceptanceRateChart/AcceptanceRateChart'
import TestScoreHistogramChart from './Charts/TestScoreHistogramChart/TestScoreHistogramChart'
import AverageTestScoreChart from './Charts/AverageTestScoreChart/AverageTestScoreChart'

type AdmissionData = {
  gender :  { [key: string]: any }; 
  act:  { [key: string]: any }; 
  sat:  { [key: string]: any }; 
  major:  { [key: string]: any }; 
  acceptances:  { [key: string]: any }; 
  rejections:  { [key: string]: any };
  ecs: { [key: string]: any };
  url:  { [key: string]: any } 
}

function App() {

  return (

    <div>
      <div>
        <Navbar></Navbar>
      </div >
    <AdmissionDataProvider>
      <div >  
          <Suspense fallback={<div></div>}>
            <GenderChart></GenderChart>
          </Suspense>
      </div>
      <div >  
          <Suspense fallback={<div></div>}>
            <MajorChart></MajorChart>
          </Suspense>
      </div>
      <div >  
          <Suspense fallback={<div></div>}>
            <TestScoreHistogramChart></TestScoreHistogramChart>
          </Suspense>
      </div>
      <div >  
          <Suspense fallback={<div></div>}>
            <AcceptanceRateChart></AcceptanceRateChart>
          </Suspense>
      </div>
      <div >  
          <Suspense fallback={<div></div>}>
            <AverageTestScoreChart></AverageTestScoreChart>
          </Suspense>
      </div>
    </AdmissionDataProvider>

    </div>
  )
  
}
export type { AdmissionData }
export default App; 

