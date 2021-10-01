name = input ('Vvedite imya studenta: ')
secondname = input ('Vvedite familiu studenta: ')
birthyear = int (input('Vvedite god rozhdeniya studenta: '))

print (name, secondname, birthyear, sep = "_")

name, secondname = secondname, name 
print (name, secondname, birthyear+60, sep = "_")
