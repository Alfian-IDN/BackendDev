from fastapi import FastAPI
from enum import Enum
import json


app = FastAPI()

with open("datas.json", "r") as file:
    datas = json.load(file)


class DBData(dict, Enum):
      DATA = datas 

    
@app.get("/") #path operation
async def root():
        return "Hello World"


@app.get("/product/my_product") #/product/my-product -> this is my product
async def say():
      return "This is my Product"

@app.get("/product/{product_name:path}-{product_code:path}") #"/product/3" MARKUS-product_code
async def read_item(product_code: str, product_name : str, skip: int = 2, limit: int=10 ):# masih disini
        data = DBData.DATA.value[product_code]
        if data["Product Name"] == product_name and data["Product Code"] == product_code:
            return datas[product_code]
        else:
            return "not a valid data"


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": str(file_path)}






"""
data = datas[product_code] -> 502.611.51
{"Product Name": "MARKUS", "Urls": "https://www.ikea.co.id/in/produk/ruang-kerja-kantor/kursi-kantor/markus-art-50261151", 
"Price": 2999000, "Sold": 883.0, 
"Description": " Kursi kantor ergonomis ini membuat Anda tetap nyaman dan fokus dengan fitur-fitur seperti ketegangan kemiringan yang dapat diatur secara manual, dan sandaran kepala/lengan untuk membantu mengendurkan otot-otot di leher dan punggung. Garansi 10 tahun.", 
"Product Code": "502.611.51"}
"""