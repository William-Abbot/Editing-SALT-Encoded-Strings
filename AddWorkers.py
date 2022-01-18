import re


step = {'supply':'','minutes':'','seconds':'','type':'','item':''}
types = {'structure': 0, 'unit': 1, 'morph': 2, 'upgrade': 3}
#4 is added to the supply number and every character that is decoded has 1 subtracted from it

bo_string = input("enter SALT encoded string: ")

bo_string.split('~')[1]

#m1 = input("\n\noptions:\n  0: insert workers manually  1: paste build order with workers included")

with_worker = input("\n\npaste build order with workers included: \n")

with_worker.lstrip()

with_worker.split('\n')

workers = ("Probe", "SCV", "Drone")

for line in with_worker:
    if any([w in line for w in workers]):
        print("worker detected")


while counter > bo_string.length():
    for i in range(5):
        
    counter += 6
    break