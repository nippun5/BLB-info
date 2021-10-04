import json
 
def el():
    f= open('fixtures/login.json')
    g=open('fixtures/loan_demand_data.json')
    login_data=json.load(f)
    datas=json.load(g)
    
    print(datas['loan_period'])


    # for i in datas['first_name']:
    #     print(i)

el()
    
    # with open("login.json", "r") as read_file:
    #     data=json.load(read_file)
    #     # x= json.loads(data)
    #     # json.dump(data)  
    #     print(data["username"])