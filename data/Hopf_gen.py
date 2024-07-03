import numpy as np
from Hopf_solv import hopf_bifurcation, mu_value, solve
from tqdm import tqdm 
import pandas as pd

numICs = 1000
filenamePrefix = 'data/Hopf'
xrange = [-1, 1]
yrange = [-1, 1]

T = 51
t_span = (0, T)
dt = 0.01
lenT = int(T/dt)
t_eval = np.linspace(*t_span, lenT)


def create_dataset(numICs):
    numICs = int(numICs)
    arr = np.zeros(shape=(numICs*lenT, 2))
    for count in tqdm(range(0, numICs)):
        x1 = (xrange[1]-xrange[0])*np.random.random() + xrange[0]
        y1 = (yrange[1]-yrange[0])*np.random.random() + yrange[0]
        ic = [x1, y1]

        x, y = solve(hopf_bifurcation, t_span, ic, t_eval)
        arr[count*lenT:lenT*(1+count), 0] = x
        arr[count*lenT:lenT*(1+count), 1] = y
    return arr

np.random.seed = 0
X_test = create_dataset(numICs=numICs*0.1)
pd.DataFrame(X_test).to_csv(f'{filenamePrefix}_test_x.csv', index=False, header=None, float_format='%.14f')
print('Test dataset created!')


np.random.seed = 1
X_val = create_dataset(numICs=numICs*0.2)
pd.DataFrame(X_val).to_csv(f'{filenamePrefix}_val_x.csv', index=False, header=None, float_format='%.14f')
print('Validation dataset created!')

for j in range(1, 7):
    np.random.seed = 1+j
    X_train = create_dataset(numICs=numICs*0.7)
    pd.DataFrame(X_train).to_csv(f'{filenamePrefix}_train{j}_x.csv', index=False, header=None, float_format='%.14f')
    print(f'{j}th Train datasets created!')
    