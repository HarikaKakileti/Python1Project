from winreg import HKEYType

name =("harika")
print(type(name))
print(name.upper())
print(name.lower())
print(len(name))

a = "90"
age =23
print(type(a))
print(type(age))


name ="H"
print(type(name))
name =name+str(9)
print(name)



firstname= "Harika"
lastname="kakileti"
fullname= firstname+lastname #concatenation
print(fullname)
# null concept is not present in python

h_k= None
print(type(h_k))  # None type


#id

age = 23
age2 = 23
print(id(age))
print(id(age2))     # 140718806666360 id means where location/address is stored