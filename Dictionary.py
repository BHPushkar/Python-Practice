d1={"Pushkar":"GECA","Paresh":"VIIT","Soham":"KKW"}
print(d1["Pushkar"])

d1["Tanmay"]="MET"   #To add an item
print(d1)
d1.update({"Tamnay":"Chocolate"})
print(d1)

del d1["Soham"]     #To remove an item
print(d1)

print(d1.keys())    #prints only keys
print(d1.items())   #prints only items

