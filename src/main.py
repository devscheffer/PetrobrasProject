# %%
import re
import os
from pathlib import Path
from tracemalloc import start
#%%
check =re.findall("\w+",str(os.getcwd()))[-1]
if check=="src":
    os.chdir(Path(__file__).parents[1])
#%%

from extract.extract import extract
import pandas as pd
#%%
e_lst = []
with open("src/conf/official_dates.txt","r") as f:
    for line in f.read().splitlines():
        line_v1=line.split(",")
        line_v2 = {"start":line_v1[0],"end":line_v1[1]}
        e =extract(line_v2)
        e_lst.append(e)
for i in e_lst:
    data = i
    print(data.get("name"))
    df = pd.read_csv(data.get("path"))
#%%
df.head()
#%%



