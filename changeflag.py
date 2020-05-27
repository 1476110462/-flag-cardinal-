##limu
import json

with open("./1.asc",'r') as load_f:
    load_dict = json.load(load_f)
#    print(load_dict)
now_id = 4 
##now_round = 1000
with open('./round','rw') as f:
   now_round = int(f.read())
   print now_round

with open('./round','w')  as g:  
   now_round = str(now_round + 1)
   g.write(now_round)

for dict_data in load_dict:
    if dict_data['Round'] == (int(now_round) - 1):
        print dict_data['Round']
        if dict_data['TeamID'] == now_id:
            print dict_data['TeamID']
            now_flag = dict_data['Flag']
            print now_flag
            with open('flag', 'w') as p:
             p.write(now_flag)
