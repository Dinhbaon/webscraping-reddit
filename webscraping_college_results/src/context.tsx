import React, { useEffect, useState } from 'react';

type AdmissionData = {
    gender : {}; 
    act: {}; 
    sat: {}; 
    major: {}; 
    acceptances: {}; 
    rejections: {};
    ecs: {};
    url: {} 
}

interface DataContextProps{ 
    readonly admissionData: AdmissionData; 
    readonly setAdmissionData : (admissionData : AdmissionData) => void; 
    readonly applicableFilters : {}

}

const DataContext = React.createContext<DataContextProps>({
    admissionData : {
      gender : {}, 
      act: {}, 
      sat: {}, 
      major: {},  
      acceptances: {},  
      rejections: {}, 
      ecs: {}, 
      url: {}
    }, 
    setAdmissionData : () => {},
    applicableFilters: 
    {
      'gender': (admissionData : AdmissionData)=> { return admissionData} , 
      'sat': (admissionData : AdmissionData)=> { return admissionData}, 
      'act': (admissionData : AdmissionData)=> {return admissionData}, 
      'major': (admissionData : AdmissionData)=> {return admissionData}, 
      'acceptances': (admissionData : AdmissionData)=> {return admissionData}, 
      'rejections': (admissionData : AdmissionData)=> {return admissionData}, 
      'ecs': (admissionData : AdmissionData)=> {return admissionData}

  }

})

const AdmissionDataProvider = ({children} : {children : React.ReactNode}) => {
    const [admissionData, setAdmissionData] = useState<AdmissionData>({
      gender : {}, 
      act: {}, 
      sat: {}, 
      major: {},  
      acceptances: {},  
      rejections: {}, 
      ecs: {}, 
      url: {}
    });

    const applicableFilters =
    {
      'gender': (admissionData : AdmissionData)=> { return admissionData} , 
      'sat': (admissionData : AdmissionData)=> { return admissionData}, 
      'act': (admissionData : AdmissionData)=> {return admissionData}, 
      'major': (admissionData : AdmissionData)=> {return admissionData}, 
      'acceptances': (admissionData : AdmissionData)=> {return admissionData}, 
      'rejections': (admissionData : AdmissionData)=> {return admissionData}, 
      'ecs': (admissionData : AdmissionData)=> {return admissionData}

  }

     useEffect(()=>{
      Promise.all([ fetch('http://ec2-3-20-42-127.us-east-2.compute.amazonaws.com:8080/api/Gender'), 
                    fetch('http://ec2-3-20-42-127.us-east-2.compute.amazonaws.com:8080/api/Major'), 
                    fetch('http://ec2-3-20-42-127.us-east-2.compute.amazonaws.com:8080/api/SAT'), 
                    fetch('http://ec2-3-20-42-127.us-east-2.compute.amazonaws.com:8080/api/ACT'), 
                    fetch('http://ec2-3-20-42-127.us-east-2.compute.amazonaws.com:8080/api/Acceptances'), 
                    fetch('http://ec2-3-20-42-127.us-east-2.compute.amazonaws.com:8080/api/Rejections'), 
                    fetch('http://ec2-3-20-42-127.us-east-2.compute.amazonaws.com:8080/api/Extracurriculars'),
                    fetch('http://ec2-3-20-42-127.us-east-2.compute.amazonaws.com:8080/api/URL')
                  ]).then((value) => Promise.all(value.map(r => r.json()))
                  ).then((value) => {
                    setAdmissionData({
                      gender: value[0],
                      major: value[1], 
                      sat: value[2], 
                      act: value[3], 
                      acceptances: value[4], 
                      rejections: value[5], 
                      ecs: value[6],
                      url: value[7]
                    })
                  })}, [])
  const value = {
    admissionData, 
    setAdmissionData, 
    applicableFilters
  };

  return (
    <DataContext.Provider value={value}>
      {children}
    </DataContext.Provider>
  );
}

export default AdmissionDataProvider
export {DataContext}; 