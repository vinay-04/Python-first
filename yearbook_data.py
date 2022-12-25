import pyrebase
from collections import OrderedDict


config = {
    "apiKey": "AIzaSyBExCSlSR3EerK0A3vkrFkmnIEXX4VyL-E",
    "authDomain": "yearbook2021-a04e4.firebaseapp.com",
    "databaseURL": "https://yearbook2021-a04e4-default-rtdb.firebaseio.com",
    "projectId": "yearbook2021-a04e4",
    "storageBucket": "yearbook2021-a04e4.appspot.com",
    "messagingSenderId": "421060020052",
    "appId": "1:421060020052:web:bd4ed7c19bdbf31f31eac1",
    "measurementId": "G-3NXDEJDPZX"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
t_dict={}
p_dict={}
j_dict={}
main_str=""

cls = 'SS2D'

users = db.child(cls).get()
u = users.val()
dict1 = dict(u)

l = []

def rep(l):
    l = set(l)
    l = list(set(l))
    seen = set()
    result = []
    for item in l:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

with open(cls,'w', encoding='utf-8') as f:
        
    for i in dict1.keys():
        #print(i)
        f.write(i+"\n")
        t_dict = dict1[i]
        for j in t_dict.keys():
            # if j[-1] == ' ':
            #     j = j[:-1]
            # #     # print("     " + j)
            l.append(j)
            f.write("     " + j + "\n")
            # else:
            #     # print("     " + j)
            # l.append(j)
            # f.write("     " + j + "\n")
            p_dict=t_dict[j]
            for k in p_dict.keys():
                j_dict=p_dict[k]
                for about in j_dict.keys():
                    # print("          " + j_dict[about])
                    f.write("          " + j_dict[about]+"\n")
                    f.write("\n")


f.close()

# w = 
# a = 
# b = 
# c = 
# d = 

# l = w+a+b+c+d

# result=rep(l)
# for i result:
#     print(result)