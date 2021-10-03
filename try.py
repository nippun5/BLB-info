import json
 
def el():
    f= open('login.json')
    data=json.load(f)
    
    for i in data['password']:
        print(i)

el()
    
    # with open("login.json", "r") as read_file:
    #     data=json.load(read_file)
    #     # x= json.loads(data)
    #     # json.dump(data)  
    #     print(data["username"])