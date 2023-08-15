import pandas as pd
from app import attributes, Major, Ecs, Race, Acceptances,Rejections, db 

df = pd.read_csv('back_end/csvfiles/processeddata.csv', index_col=False)

db.drop_all()
for i in range(len(df)):
    applicant = attributes(Gender=df.iloc[i, 0], SAT=df.iloc[i, 3], ACT=df.iloc[i, 4], URL=df.iloc[i, 8], timestamp = df.iloc[i, 9])
    db.session.add(applicant)
    time_stamps_value =applicant.timestamp
    for racevalues in eval(df.iloc[i, 1]):

        race = Race(racelist=racevalues, Attributeid=time_stamps_value)
        db.session.add(race)

    for majorvalues in eval(df.iloc[i, 2]):
        major = Major(majorlist=majorvalues, Attributeid=time_stamps_value)
        db.session.add(major)

    for ecvalues in eval(df.iloc[i, 5]):
        ecs = Ecs(listofecs=ecvalues, Attributeid=time_stamps_value)
        db.session.add(ecs)

    for valuesacceptances in eval(df.iloc[i, 6]):
        accepts = Acceptances(acceptlist=valuesacceptances, Attributeid=time_stamps_value)
        db.session.add(accepts)

    for valuesreject in eval(df.iloc[i, 7]):
        rejects = Rejections(rejectlist=valuesreject, Attributeid=time_stamps_value)
        db.session.add(rejects)

db.create_all()
db.session.commit()
print('done')
