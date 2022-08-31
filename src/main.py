from src.util import download_xls, generate_csv_file

date_download_lst = [{"start":"2022-08-07","end":"2022-08-13"}]


for i in date_download_lst:
    file_full_path = download_xls(output_dir="src/dataset",file_name="petrobras",date=i)
    generate_csv_file(file_full_path=file_full_path,date=i,output_dir="src/dataset")



