import re
import sys


step = {'supply':'','minutes':'','seconds':'','type':'','item':''}
types = {'structure': 0, 'unit': 1, 'morph': 2, 'upgrade': 3}
#4 is added to the supply number and every character that is decoded has 1 subtracted from it

bo_string = input("enter SALT encoded string: ")

bo_string_lst = bo_string.split('~')[1]

#m1 = input("\n\noptions:\n  0: insert workers manually  1: paste build order with workers included")

print("\n\npaste build order with workers included (press ctrl+D when finished): ")

with_worker = sys.stdin.read()

with_worker.lstrip()

with_worker_lst = with_worker.split('\n')

workers = ("Probe", "SCV", "Drone")

#TODO: round starting supply to 12
for line in with_worker_lst:
    #print(line)
    if any([w in line for w in workers]):
        None
    pattern = re.compile(r'(/s


