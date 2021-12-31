#Dump:-    used to convert from python object to json file
# 
# ex:-

# import json
# a={"name": "David", "class": "I", "age": 6}
# b=open("amol_json.json","w")
# json.dump(a,b,indent=1)
# b.close()
# print(type(a))
# print(type(b))



#Dumps :-  to covert from python object to json file string format

# import json 
# a={"name": "David", "class": "I", "age": 6}
# b=json.dumps(a)
# print(type(b))
# print(type(a))



# Load :- use to convert from json object or json file to python object


# Loads :- use to convert from json string to json objects

import json
a='{"name": "David", "class": "I", "age": 6}'
b=json.loads(a)
print(type(a))
print(type(b))



# meraki questions


#Q1
# import json
# a='{"Name":"Ram","Class":"IV","Age":9 }'
# b=json.loads(a)
# print(type(a))
# print(type(b))



# #Q2
# import json
# a={"Name":"Ram","Class":"IV","Age":9}
# b=json.dumps(a)
# print(a)
# print(b)
# print(type(a))
# print(type(b))



#Q3
# import json
# a={"Name":"Ram","Class":"IV","Age":9}
# b=json.dumps(a)
# print(a)
# print(b)
# print(type(a))
# print(type(b))



#Q4
# import json
# a={'4':5,'6':7,'1':3,'2':4}
# b={}
# for i in sorted(a):
#     b[i]=a[i]
# c=json.dumps(b)
# print(type(c))
# print(c)


# Q6
# import json
# a='{"a":1,"a":2,"a":3,"a":4,"b":1,"b":2}'
# b=json.loads(a)
# print(b)






# Q8
# import json
# 'emp1':
#    {'name':'neelam',
#    'designation':'programer',
#    'age':24,
#    'salary':24000
#    },

# 'emp2':
#   {'name':'komal',
#   'designation':'trainer',
#   'age':24,
#   'salary':20000
#   },

# 'emp3':
#   {'name':'anuradha',
#   'designation':'HR',
#   'age':25,
#   'salary':40000
#   },

# 'emp4':
#   {'name':'Abhishek',
#   'designation':'manager',
#   'age':29,
#   'salary':63000
#   }
# }
# b=open("/home/ng/Desktop/Amol D.M/json_file/amol_maraki_company_data.json","w")
# json.dump(a,b,indent=7)
# print(a["emp1"])
# b.close()




# file handling:-
# Q4
# a=['rishabh - meerut','imtiyaz - delhi','nilima - cochin','rati - shimla','ayishah - delhi',
# 'raghu - shimla','naseer - kanpur','karthikeyan - delhi','salma - jaipur','pankaj - delhi',
# 'brijesh - delhi','govind - delhi','puneet - shimla','siddhi - delhi','suman - jaipur','rajeev - shimla',
# 'mohinder - delhi','rajendra - jaipur','priyanka - shimla','neela - delhi','sashi - jaipur',
# 'sarika - delhi','deepti - shimla','harshad - delhi','trishna - raipur','pradeep - jaipur',
# 'sekhar - delhi','nand - delhi','anoop - delhi','balwinder - tokyo']
# b=open("/home/ng/Desktop/Amol D.M/json_file/Question3.txt","w")
# for i in a:
#     b.writelines(i)
#     b.writelines("\n")
# b.close()

# a=open("/home/ng/Desktop/Amol D.M/json_file/Question3.txt","r")
# b=open("/home/ng/Desktop/Amol D.M/json_file/delhi.txt","w")
# c=open("/home/ng/Desktop/Amol D.M/json_file/shimla.txt","w")
# d=open("/home/ng/Desktop/Amol D.M/json_file/others.txt","w")
# for i in a:
#     if "delhi" in i:
#         b.write(i)
#     elif "shimla" in i:
#         c.write(i)
#     else:
#         d.write(i)
# a.close()
# b.close()
# c.close()
# d.close()