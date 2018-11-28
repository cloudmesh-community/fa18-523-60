from pymongo import MongoClient
import pandas as pd
client = MongoClient()
#if you are remote then use appropiate connect string.
# for e.g. client = pymongo.MongoClient("mongodb://nishad:****@159.203.170.43/kickstarter")
# assumes the default port is 27017 else mention the port number.
db=client.kickstarter # -- Name of the database kickstarter
employee = db.projects #--- Name of the collection projects
df = pd.read_csv("kickstarterprojects.csv") #c---sv file which you want to import
records_ = df.to_dict(orient = 'records')
result = db.projects.insert_many(records_ )
