n_set = set()

while len(n_set) < 25:
  import random
  n = random.randint(1, 60)
  n_set.add(n)

n2_set = set()

while len(n2_set) < 5:
  import random
  n2 = random.randint(1, 60)
  n2_set.add(n2)
  
sorteio_verificacao = n_set | n2_set

if len(sorteio_verificacao) == 25:
  print('Parabens, voce foi sorteado!')
else:
  print('Nao foi desta vez que voce conseguiu.')