#item/3
# message : 3

#IKEA /Item/510.21.32
#muncul item data tadi sepenuhnya, nama, harga, link, jumlah penjualan lain

# 1.Bikin program yg ngebaca xlsxnya 
# 1a. hasilnya mungkin ke bentuk list of dictionaries karena mereka konsisten
# harus ngerubah list of dictionary

buah = ["apple", "semangka", "pisang"]
print(buah[0]) #apple
print(buah[1]) #semangka
print(buah[2]) #pisang

dataxlsx = [421,422,423,424]
print(dataxlsx[0]) #421 -> item/0/
#enaknya aksesnya item/421 -> munculkan data 421

datates = [0,1,2,3,4,5]
print(datates[2]) 
#delete angka 1
datates = [0,2,3,4,5]
print(datates[2]) 
#nested dictionaries
dictionary = {"item_id1" : "Valuedisini1", "item_id2" : "Valuedisini2", "item_id3" : "Valuedisini3"}
print(dictionary["item_id2"])
del dictionary["item_id2"]
print(dictionary)
print(dictionary["item_id3"])