import requests
import datetime as dt

pixela_endpoints = "https://pixe.la/v1/users"
USERNAME = "cocheche"
TOKEN = "helo38470nha654371cac75474ban"

user_params = {
    "token" : "helo38470nha654371cac75474ban",
    "username" : "cocheche",
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}

# # 1. set up user account
# response = requests.post(url=pixela_endpoints,json=user_params)
# # {"message":"Success. Let's visit https://pixe.la/@cocheche , it is your profile page!","isSuccess":true}
# # print(response.text)

# 2. create a graph definition
graph_endpoint = f"{pixela_endpoints}/{USERNAME}/graphs"

headers = {
    "X-USER-TOKEN" : TOKEN
}
graph_params = {
    "id" : "graph1",
    "name" : "amount of hour learning track",
    "unit" : "hours",
    "type" : "float",
    "color" : "ajisai"
}
# response = requests.post(url=graph_endpoint,json=graph_params,headers=headers)
# print(response.text)

# 3. get the graph!
# Browse https://pixe.la/v1/users/a-know/graphs/test-graph ! This is also /v1/users/<username>/graphs/<graphID> API

# 4. post value to the graph
today = dt.datetime.now()

square_endpoints = f"{pixela_endpoints}/{USERNAME}/graphs/{graph_params['id']}"

pixel_params = {
    "date" : today.strftime("%Y%m%d"),
    "quantity" : "4"
}

# response = requests.post(url=square_endpoints,json=pixel_params,headers=headers)
# print(response.text)

update_url = f"{pixela_endpoints}/{USERNAME}/graphs/graph1/20240705"
update_params = {
    "quantity" : "1"
}
response = requests.put(update_url,json=update_params,headers=headers)
print(response.text)