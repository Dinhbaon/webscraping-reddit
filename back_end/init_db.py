import pandas as pd
from app import attributes, Major, Ecs, Race, Acceptances,Rejections, db 
from ast import literal_eval
df = pd.read_csv('.\csvfiles\processeddata.csv')
db.drop_all()
for i in range(len(df['Gender'])): 
    applicant = attributes(Gender = df['Gender'].iloc[i],SAT = df['SAT'].iloc[i], ACT = df['ACT'].iloc[i])
    db.session.add(applicant)
    for racevalues in eval(df['Race'].iloc[i]): 
        race = Race(racelist = racevalues, Attributeid = i+1)
        db.session.add(race)
    for majorvalues in eval(df['Major'].iloc[i]): 
        major = Major(majorlist = majorvalues,Attributeid = i+1 )
        db.session.add(major)
    for ecvalues in eval(df['Extracurriculars'].iloc[i]):
        ecs = Ecs(listofecs = ecvalues , Attributeid = i+1)
        db.session.add(ecs)
    for valuesacceptances in eval(df["Acceptances"].iloc[i]): 
        Accepts = Acceptances(acceptlist = valuesacceptances, Attributeid = i+1)
        db.session.add(Accepts)
    for valuesreject in eval(df["Rejections"].iloc[i]): 
        Rejects = Rejections(rejectlist = valuesreject, Attributeid = i+1)
        db.session.add(Rejects)

db.create_all()
db.session.commit()
