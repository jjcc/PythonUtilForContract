import pandas as pd

datafile = "Data//updated_sharepoint.xlsm"


df = pd.read_excel(datafile)

dse = df["Data Steward Email"]
df["Data Steward Email"] = dse.str.replace(r';#\d+',"")
df.to_excel("Data//new_updated_sp.xlsx")

pass