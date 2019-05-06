from numpy import *
import matplotlib.pyplot as plt
import xlrd



def sanitize(data):
    '''
    Makes sure the data list is a float.
    '''
    refined = []
    for i in data:
        if type(i) == float:
            refined.append(i)
        else:
            pass
    return refined


def process(data):
    '''
    Simulate the construction
    '''
    V = []
    for min_cost, max_cost in data:
        value = random.randint(min_cost, max_cost)
        V.append(value)
    return sum(V)
    V = []
    for min_cost, max_cost in data:
        value = random.randint(min_cost, max_cost)
        V.append(value)
    return sum(V)

################################################
################################################
wb = xlrd.open_workbook('cost.xlsx')
sheet1 = wb.sheet_by_index(0)

min_costs =  sanitize(
    sheet1.col_values(1)
    )
max_costs = sanitize(
    sheet1.col_values(2)
    )

data = list(zip(min_costs, max_costs))
event = []
k = 1000
for i in range(k):
    event.append(process(data))

plt.hist(event, 50,
         color='g'
         )
plt.title('min:{} avg:{} max:{} after {} simulations'.format(min(event),
                                                             int(sum(event)/len(event)),
                                                             max(event), k)
          )
plt.xlabel('Cost')
plt.ylabel('Probability Density')
plt.show()
