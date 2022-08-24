import pandas as pd
from app import attributes, Major, Ecs, Race, Acceptances,Rejections, db, df 
from ast import literal_eval

for i in range(len(df['Gender'])): 
    applicant = attributes(Gender = df['Gender'].iloc[i],SAT = df['SAT'].iloc[i], ACT = df['ACT'].iloc[i] )
    db.session.add(applicant)
    for racevalues in df['Race'].apply(literal_eval).iloc[i]: 
        race = Race(racelist = racevalues, Attributeid = i)
        db.session.add(race)
    for majorvalues in df['Major'].apply(literal_eval).iloc[i]: 
        major = Major(majorlist = majorvalues,Attributeid = i )
        db.session.add(major)
    for ecvalues in df['Extracurriculars'].apply(literal_eval).iloc[i]:
        ecs = Ecs(listofecs = ecvalues , Attributeid = i)
        db.session.add(ecs)
    for valuesacceptances in df["Acceptances"].apply(literal_eval).iloc[i]: 
        Accepts = Acceptances(acceptlist = valuesacceptances, Attributeid = i)
        db.session.add(Accepts)
    for valuesreject in df["Rejections"].apply(literal_eval).iloc[i]: 
        Rejects = Rejections(rejectlist = valuesreject, Attributeid = i)
        db.session.add(Rejects)






db.session.commit()