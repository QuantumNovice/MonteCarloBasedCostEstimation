from numpy import *
import matplotlib.pyplot as plt

data = [
    # Cost of Tiles
    (200,1000),
    (10, 150)
        ]

def process():
    V = []
    for min_cost, max_cost in data:
        value = random.randint(min_cost, max_cost)
        V.append(value)
    return V

V = []
k = 10000
for i in range(k):
    V.append(process())

plt.hist([sum(i)/len(i) for i in V], 50, color='g')
plt.title('min:{} avg:{} max:{} after {} simulations'.format(min(V)[0], int(sum(V)/len(V)), max(V)[0], k) )
plt.ylabel('Cost')
plt.xlabel('Probability Density')
plt.show()
