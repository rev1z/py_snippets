import os
# replace first occurrence in every file in folder

path = "views"
source_subtr = "SELECT"
desired_substring = f"{source_subtr} DISTINCT"

curpath = os.path.dirname(os.path.realpath(__file__))
abspath = os.path.join(curpath, path)

dirpath, dirnames, filenames = list(os.walk(abspath))[0]

for item in filenames:
    fname = os.path.join(dirpath, item)

    with open(fname, "r") as file:
        data = file.readlines()

    for i, line in enumerate(data):
        if source_subtr in line:
            data[i] = line.rstrip("\n")
            data[i] = desired_substring
            break

    with open(fname, 'w') as file:
        file.writelines(data)

