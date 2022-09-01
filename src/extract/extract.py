from extract.break_xls_to_csv import break_xls_to_csv
from extract.download_xls import download_xls


def extract(date_download_lst):
    for i in date_download_lst:
        file_full_path = download_xls(output_dir="src/dataset",file_name="petrobras",date=i,)
        csv_list = break_xls_to_csv(file_full_path=file_full_path,date=i,output_dir="src/dataset",)
        return csv_list
