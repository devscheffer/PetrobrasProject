from extract.extract import extract
import pandas as pd

date_download_lst = [{"start":"2022-08-07","end":"2022-08-13"}]

for i in extract(date_download_lst):
    data =i
    print(data.get("name"))
    print(pd.read_csv(data.get("path")).head(2))



