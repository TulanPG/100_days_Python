import requests

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "testtoken1994"
USERNAME= "tulan"
GRAPH_ID= "graph0001"

user_param = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
#part1 Create your user account
#response = requests.post(url=pixela_endpoint, json=user_param)
#print(response.text)


#part2 Create a graph definition
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph0001",
    "name": "Programing Graph",
    "unit": "hours",
    "type": "int",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN" : TOKEN
}

#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(response.text)

#part3 Post value to the graph

graph_data_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

update_data = {
    "date": "20220407",
    "quantity": "2",
    "optionalData": "",
}

response = requests.post(url=graph_data_endpoint, json=update_data, headers=headers)
print(response.text)