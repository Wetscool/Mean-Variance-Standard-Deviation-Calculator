import numpy as np

def calculate(list):
    
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    matrix = np.array(list).reshape(3, 3)
    
    operations = [np.mean, np.var, np.std, np.max, np.min, np.sum]
    keys = ['mean', 'variance', 'standard deviation', 'max', 'min', 'sum']
    
    calculations = {}
    
    for number in range(len(operations)):
        calculations[keys[number]] = [
            operations[number](matrix, axis=0).tolist(),
            operations[number](matrix, axis=1).tolist(),
            operations[number](matrix)
        ]
    
    return calculations