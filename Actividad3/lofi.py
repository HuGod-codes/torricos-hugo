import yaml

file = open("inputs.yaml", "r")

yml = yaml.safe_load(file)

file.close()

print(yml)