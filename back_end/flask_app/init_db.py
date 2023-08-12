import pandas as pd
from app import attributes, Major, Ecs, Race, Acceptances,Rejections, db 

def get_last_index():
    return db.session.query(attributes).order_by(attributes.id.desc()).first().id

df = pd.read_csv('..\csvfiles/newprocesseddata.csv', index_col=False)

# Get the last inserted index
last_index = get_last_index() if db.session.query(attributes).count() > 0 else 0

for i in range(len(df)):
    index = last_index + i + 1  # Calculate the new index
    applicant = attributes(Gender=df.iloc[i, 0], SAT=df.iloc[i, 3], ACT=df.iloc[i, 4], URL=df.iloc[i, 8], id=index)
    db.session.add(applicant)

    for racevalues in eval(df.iloc[i, 1]):
        race = Race(racelist=racevalues, Attributeid=index)
        db.session.add(race)

    for majorvalues in eval(df.iloc[i, 2]):
        major = Major(majorlist=majorvalues, Attributeid=index)
        db.session.add(major)

    for ecvalues in eval(df.iloc[i, 5]):
        ecs = Ecs(listofecs=ecvalues, Attributeid=index)
        db.session.add(ecs)

    for valuesacceptances in eval(df.iloc[i, 6]):
        accepts = Acceptances(acceptlist=valuesacceptances, Attributeid=index)
        db.session.add(accepts)

    for valuesreject in eval(df.iloc[i, 7]):
        rejects = Rejections(rejectlist=valuesreject, Attributeid=index)
        db.session.add(rejects)

db.session.commit()
print('done')
