# initial solution

lista = []
def rotLeft(a, d):
  global lista
  if type(a) == int:
    a = [int(i) for i in str(a)]
  if d == 0:
    return a
  elif d > 0:
    g = a[0]
    a = a[1:]
    a.append(g)
    d = d - 1
    rotLeft(a,d)
  lista.append(a)
  return lista[0]

# optimized solution

def rotLeft(a, d):
  for i in range(0,d):
    first = a.pop(0)
    a.append(first)
  return a
