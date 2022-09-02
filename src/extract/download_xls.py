import requests

def download_xls(*,output_dir,file_name,date):
    date_start =date.get("start")
    date_end =date.get("end")
    file_full_path = f'{output_dir}/{file_name}-{date_start}-{date_end}.xlsx'

    file_url = f'https://www.gov.br/anp/pt-br/assuntos/precos-e-defesa-da-concorrencia/precos/arquivos-lpc/resumo-semanal-lpc-{date_start}-{date_end}.xlsx'

    r = requests.get(file_url, stream = True)
    if r.status_code != 200:
        return None

    with open(file_full_path,"wb") as f1:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f1.write(chunk)
    return file_full_path
