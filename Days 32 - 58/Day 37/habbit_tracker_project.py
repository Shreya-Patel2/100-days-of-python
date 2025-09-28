import requests
from datetime import datetime

USERNAME = "###"
TOKEN = "###"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {"token": TOKEN,
               "username": USERNAME,
               "agreeTermsOfService": "yes",
               "notMinor": "yes"}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {"id": "graph1",
                "name": "Walking Graph",
                "unit": "km",
                "type": "float",
                "color": "sora"}

headers = {"X-USER-TOKEN": TOKEN}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

graph_pixel = {"date": "###",
               "quantity": "25"}

response = requests.post(url=pixel_endpoint, json=graph_pixel, headers=headers)
print(response.text)
