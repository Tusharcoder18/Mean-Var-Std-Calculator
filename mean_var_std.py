import numpy as np


def calculate(input: list):
    if len(input) < 9:
        raise ValueError('List must contain nine numbers.')
    matrix = np.reshape(input, (3,3))
    # print(matrix)
    calculations = {
        'mean': [lambda x: list(x.mean(axis=0)), lambda x: list(x.mean(axis=1)), lambda x: np.mean(input)],
        'variance': [lambda x: list(x.var(axis=0)), lambda x: list(x.var(axis=1)), lambda x: np.var(input)],
        'standard deviation': [lambda x: list(x.std(axis=0)), lambda x: list(x.std(axis=1)), lambda x: np.std(input)],
        'max': [lambda x: list(x.max(axis=0)), lambda x: list(x.max(axis=1)), lambda x: np.max(input)],
        'min': [lambda x: list(x.min(axis=0)), lambda x: list(x.min(axis=1)), lambda x: np.min(input)],
        'sum': [lambda x: list(x.sum(axis=0)), lambda x: list(x.sum(axis=1)), lambda x: np.sum(input)],
    }

    for key, value in calculations.items():
        calculations[key] = [calc(matrix) for calc in value]


    return calculations


# result = calculate([0,1,2,3,4,5,6,7])

# # for key, value in result.items():
# #     print(key, value)