def buscaMenor(array):

  menor = array[0]
  ind_menor = 0

  for i in range(1, len(array)):
    if array[i] < menor:
      menor = array[i]
      ind_menor = i
  return ind_menor

def ordPorSel(array):
  
  novoArray = []

  for i in range(len(array)):
    menor = buscaMenor(array)
    novoArray.append(array.pop(menor))
  return novoArray

aux = ordPorSel("Digite aqui o array para ordenar de forma crescente")

print (aux)
