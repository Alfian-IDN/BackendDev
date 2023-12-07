import pandas as pd
import json
#item/3
# message : 3

#IKEA /Item/510.21.32
#muncul item data tadi sepenuhnya, nama, harga, link, jumlah penjualan lain

# 1.Bikin program yg ngebaca xlsxnya 
# 1a. hasilnya mungkin ke bentuk list of dictionaries karena mereka konsisten
# harus ngerubah list of dictionary

def read_excel_to_list_of_dicts(file_path, sheet_name=0):
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        # Convert the DataFrame to a list of dictionaries
        records = df.to_dict(orient='records')
        return records


def transform_data(datas : list):
    hasil = {}

    for data in datas:
        hasil[data["Product Code"]] = data
    return hasil

# Example usage:
file_path = 'projectscraping.xlsx'
datas = read_excel_to_list_of_dicts(file_path)
final_data = transform_data(datas)
with open("datas.json", "w") as json_file:
    json.dump(final_data, json_file)
print(final_data)
















#tes_data = [{"nama_product" : "Gitar", "Model_ID" : 532214}, {"nama_product" : "Bass", "Model_ID" : 532200}, {"nama_product" : "Drum", "Model_ID" : 21500}]
#hasil = {}
#
#for data in tes_data:
#    hasil[data["Model_ID"]] = data
#
#print(hasil)
"""
target = {532214 : {"nama_product" : "Gitar", "Model_ID" : 532214}, 532200 : {"nama_product" : "Bass", "Model_ID" : 532200}, 21500 : {"nama_product" : "Drum", "Model_ID" : 21500}}
print(target[532200])
"""