import yaml
import sys

print(sys.argv)

with open(sys.argv[1], 'r') as file:
    prime_service = yaml.safe_load(file)
