import requests
import datetime as dt
import os

# # Generate user token
# import secrets  # using env vars instead
# user_token = secrets.token_urlsafe(20)  # using env vars instead
# print(user_token)

USERNAME = os.environ['PIXELA_USERNAME']
TOKEN = os.environ['PIXELA_TOKEN']

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
journaling_endpoint = f"{graph_endpoint}/graph1"

header = {
    "X-USER-TOKEN": TOKEN
}

# # Account Create POST
# user_params = {
#     "token": USERNAME,
#     "username": TOKEN,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }
# response = requests.post(pixela_endpoint, json=user_params)
# print(response.text)

# # Create a new graph
# header = {
#     "X-USER-TOKEN": TOKEN
# }
#
# graph_config = {
#     "id": "graph1",
#     "name": "Journaling Graph",
#     "unit": "pages",
#     "type": "float",
#     "color": "shibafu"
# }
#
# response = requests.post(url=graph_endpoint, headers=header, json=graph_config)
# print(response.text)


# # Update a graph
def update_pixel(quant:float, date_yyyymmdd=None):
    if date_yyyymmdd is None:
        entry_date = dt.datetime.now().strftime('%Y%m%d')
    else:
        entry_date = date_yyyymmdd

    body = {
        "date": entry_date,
        "quantity": str(quant)
    }

    response = requests.post(url=journaling_endpoint, headers=header, json=body)
    print(response.text)


# update_pixel(5, date_yyyymmdd='20220610')

def update_pixel(quant: float, entry_date: str):
    pixel_update_endpoint = f"{journaling_endpoint}/{entry_date}"
    body = {
        "quantity": str(quant)
    }
    response = requests.put(url=pixel_update_endpoint, headers=header, json=body)
    print(response.text)


# update_pixel(quant=3, entry_date="20220610")

def delete_pixel(entry_date: str):
    pixel_delete_endpoint = f"{journaling_endpoint}/{entry_date}"
    response = requests.delete(url=pixel_delete_endpoint, headers=header)
    print(response.text)


delete_pixel(entry_date='20220610')