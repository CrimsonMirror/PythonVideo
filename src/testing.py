


dictionary = {
    1 : 'Nani',
    2 : 'No Nani',
    3: 'Otro Nani',
    4 : 'ultimo Nani'
}

lista = [2,3]

newDict = { key:value for (key,value) in dictionary.items() if key in lista  }

print(newDict)