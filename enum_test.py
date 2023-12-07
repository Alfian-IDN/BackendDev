from enum import Enum
import json

with open("datas.json", "r") as file:
    datas = json.load(file)

class DBData(dict, Enum):
      DATA = datas 

def get_product(product_id):
     data = DBData.DATA.value[product_id]
     return data

"""
def cooking(nama_masakan):
     masakan_yg_harus_dimasak = nama_masakan
     if chef mempunyai bahan baku yg dibutuhkan:
        cook()
        food = True
     else:
        improvise()
        food = False
     return food
def cook():
    pass
    
def improvise():
    pass
"""
     
if __name__ == "__main__":
     data = get_product("502.611.51")
     print(data)