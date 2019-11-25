dic = {
    "city": "Москва", 
    "temperature": "20"
}
print(dic["city"])
p= int(dic["temperature"])
c = p-5 
dic["temperature"] = c
print(dic)
print(dic.get("country"))
print(dic.get("country", "Россия"))
dic['date'] = '27.05.2019'
print(len(dic))





