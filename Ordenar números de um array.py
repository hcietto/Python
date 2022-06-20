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

#-------------------------------
#Ou com quicksort
#-------------------------------

def quicksort(array):

  #arrays com menos de 2 elementos sempre estão organizados
  if len(array) < 2:
    return array

  else:
    #a base para organizar será o índice 0
    pivo = array[0]

    #elementos menores ou iguais ao pivo serão movidos para o array "menores"
    menores = [i for i in array[1:] if i <= pivo]

    #e os maiores para o "maiores"
    maiores = [i for i in array[1:] if i > pivo]

    #retorna os arrays como um só
    return (quicksort(menores) + [pivo] + quicksort(maiores))
  
print(quicksort("Digite aqui o array para ser organizado de forma crescente"))
