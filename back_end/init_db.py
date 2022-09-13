import pandas as pd
from app import attributes, Major, Ecs, Race, Acceptances,Rejections, db 
df = pd.read_csv('.\csvfiles\processeddata.csv')
db.drop_all()
for i in range(len(df.iloc[:,0])): 
    applicant = attributes(Gender = df.iloc[:,0].iloc[i],SAT = df.iloc[:,3].iloc[i], ACT = df.iloc[:,4].iloc[i], URL = df.iloc[:,8].iloc[i])
    db.session.add(applicant)
    for racevalues in eval(df.iloc[:,1].iloc[i]): 
        race = Race(racelist = racevalues, Attributeid = i+1)
        db.session.add(race)
    for majorvalues in eval(df.iloc[:,2].iloc[i]): 
        major = Major(majorlist = majorvalues,Attributeid = i+1 )
        db.session.add(major)
    for ecvalues in eval(df.iloc[:,5].iloc[i]):
        ecs = Ecs(listofecs = ecvalues , Attributeid = i+1)
        db.session.add(ecs)
    for valuesacceptances in eval(df.iloc[:,6].iloc[i]): 
        Accepts = Acceptances(acceptlist = valuesacceptances, Attributeid = i+1)
        db.session.add(Accepts)
    for valuesreject in eval(df.iloc[:,7].iloc[i]): 
        Rejects = Rejections(rejectlist = valuesreject, Attributeid = i+1)
        db.session.add(Rejects)

db.create_all()
db.session.commit()
