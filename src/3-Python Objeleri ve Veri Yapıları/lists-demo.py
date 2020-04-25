# 1-  "Bmw, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.
# arabalar = ['Bmw','Mercedes','Opel','Mazda']
cars=['Bmw','Mercedes','Opel','Mazda']

# 2-  Liste Kaç elemanlıdır ?
# result = len(arabalar)
result=len(cars)

# 3-  Listenin ilk ve son elemanı nedir ?
# result = arabalar[0]
# result = arabalar[3]
# result = arabalar[-1]
result=cars[0]
result=cars[-1]
# 4-  Mazda değerini Toyota ile değiştirin.
# arabalar[-1]= 'Toyota'
# result = arabalar
# cars[3]='Toyota'
result=cars
# 5-  Mercedes listenin bir elemanı mıdır ?
# result = 'Mercedes' in arabalar
result='Mercedes' in cars
# 6-  Listenin -2 indeksindeki değer nedir ?
# result = arabalar[-2]
result=cars[-2]
# 7-  Listenin ilk 3 elemanını alın.
# result = arabalar[0:3]
# result = arabalar[:3]
# result = arabalar[-2:]
result=cars[:3]

# 8-  Listenin son 2 elemanı yerine "Totoya" ve "Renault" değerlerini ekleyin.
# arabalar[-2:] = ['Toyota','Renault']
# result = arabalar
cars[-2:]=['Toyota','Renault']
result=cars
# 9-  Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin.
# result = arabalar + ['Audi','Nissan']
cars.append('Audi')
cars.append('Nissan')
result=cars
# 10- Listenin son elemanını silin.
# del arabalar[-1]
# result = arabalar
cars.pop()
result=cars
# 11- Liste elemanlarını tersten yazdırınız.
# result = arabalar[::-1]
result=cars[::-1]
# 12- Aşağıdaki verileri bir liste içinde saklayınız. 

#       studentA: Yiğit Bilgi 2010, (70,60,70)
#       studentB: Sena Turan  1999, (80,80,70)
#       studentC: Ahmet Turan 1998, (80,70,90) 
sA=['Yiğit','Bilgi',2010,[70,60,70]]
sB=['Sena','Turan',1999,[80,80,70]]
sC=['Ahmet','Turan',1998,[80,70,90]]
# studentA = ['Yiğit','Bilgi',2010,[70,60,70]]
# studentB = ['Sena','Turan',1999,[80,80,70]]
# studentC = ['Ahmet','Turan',1998,[80,70,90]]

# 13- Liste elemanlarını ekrana yazdırınız.
result=sA
result=sB
result=sC
# result = studentA[0]
# result = studentB[1]
# result = studentC[3][1]

result = f"{sA[0]} {sA[1]} {2019-sA[2]} yaşında ve not ortalaması {(sA[3][0] + sA[3][1] + sA[3][2])/3}"

print(result)