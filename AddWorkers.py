import re
import sys

#step = {'placement': 0,'supply':'12','minutes':'','seconds':'','type':'','item':''}
#types = {'structure': 0, 'unit': 1, 'morph': 2, 'upgrade': 3}

#NOTE: before encoding, 4 is added to the supply number and then 32 is added to every number being encoded

#bo = build order
bo_string = input("enter SALT encoded string: ")

#default bo_string
if len(bo_string) == 0:
    bo_string = '$158739|spawningtool.com||~* 0 /+ H !, K ,/!:" /!:!(0!H #0!O /1!Z!%3"+ %3"4 )5"H #6"S" 7"[ !7#" 07#(!#7#(!#>#5 ,>#9!%?#<#+A#M!%D#P .D#T" D#U *D#W!%D#W!%H$# /H$%!%K$+!%L$4!%L$4!%Q$>!%R$C !R$C ,R$C!&R$C 1R$C!&Z$O $Z$O $]$W" _%"!*_%" ,e%-#0i%= )i%B#"l%E +l%H#!p%R!*v%Y !v%Y !'


print("\n\npaste build order with workers included (press ctrl+D when finished. You may have to press enter first): ")

with_worker = sys.stdin.read()

with_worker.lstrip()

#default with_worker
if not any([w in list(map(chr, range(97, 123))) for w in with_worker]):
    f = open(r'E://Documents//Programming//repos//GitHub//Editing-SALT-Encoded-Strings//build orders.txt', 'r')
    with_worker = f.read()
    f.close()

with_worker_lst = with_worker.split('\n')

workers = ("Probe", "SCV", "Drone")
worker_encode = {"SCV":'9',"Drone":'28',"Probe":'22'}

counter = 0
step_str = ''
updated = bo_string.split('~')[1]

#this section iterates through the build order line by line and inserts workers into SALT encoded string where need be
#learning string comprehension and regular expressions
for line in with_worker_lst:
    if line == '':
        continue
    if any([w in line for w in workers]):
        mo = re.search('(\s+)(\d+)(\s+)(\d+)(:)(\d\d)(\s+)(\w+)', line)
        worker = worker_encode[mo.group(8)]
        arr = [str(int(mo.group(2))-4), mo.group(4), mo.group(6),'1',worker]
        step_str = ''.join(list(map(lambda s : chr(int(s)+32),arr)))
        updated = updated[:counter*5] + step_str + updated[counter*5:]
        #counter += 1
    counter += 1
print(bo_string.split('~')[0]+'~'+updated)

