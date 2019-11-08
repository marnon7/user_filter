import os

targets = ['data','data/input','data/input/datavisor', 'data/input/af', 'data/output']

for target in targets:
    try:
        os.mkdir(target)
    except FileExistsError:
        print("{} exist!".format(target))
