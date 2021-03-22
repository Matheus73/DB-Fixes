from dataManip import *

#--------------VARS--------------#
pkConstraints=''
fkConstraints=''
#--------------------------------#

#--------------MAIN--------------#
try:
  pkConstraints, fkConstraints = getData(input("Insert File Name\n"))
except:
  print("Couldn't Find The File\n")
  exit(0)

fkConstraints =  formatAlter(fkConstraints)

pkConstraints = formatCreate(pkConstraints)

print('\nPRIMARY KEYS')
for const in pkConstraints:
  print('Tabela: {}\n{}\n'.format(const[0], const[1]))
print('\nFOREING KEYS')
for const in fkConstraints:
  print('Tabela: {}\n{}\n'.format(const[0], const[1]))
