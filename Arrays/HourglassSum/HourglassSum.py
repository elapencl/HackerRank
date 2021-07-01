def hourglassSum(arr):
  biggest_sum = 0
  lista = []
  for i in range(4):
    for j in range(4):
      hourglass_sum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
      lista.append(hourglass_sum)
  biggest_sum = max(lista)
  return biggest_sum
