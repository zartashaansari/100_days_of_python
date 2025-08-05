import requests
from datetime import datetime
pixela_endpoint="https://pixe.la/v1/users"
TOKEN="ndomksdjioejmsk3"
USER="zartasha"
parameters={
    "token":TOKEN,
    "username":USER,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"

}
# response=requests.post(url=pixela_endpoint,json=parameters)
# print(response.text)
graph_endpoint=f"{pixela_endpoint}/{USER}/graphs"
GRAPHID="mygraph16"
graph_parameters={
    "id":GRAPHID,
    "name":"coding",
    "type":"float",
    "unit": "hours",
    "color":"shibafu"


}
headers={
    "X-USER-TOKEN":TOKEN
}
# response=requests.post(url=graph_endpoint,json=graph_parameters,headers=headers)
# print(response.text)
today=datetime.now()
DATE=today.strftime("%Y%m%d")
pixel_endpoint=f"{pixela_endpoint}/{USER}/graphs/{GRAPHID}"
pixel_parameters={
    "date":DATE,
    "quantity":input("how many hours did u code today?"),
 }
response=requests.post(url=pixel_endpoint,json=pixel_parameters,headers=headers)
print(response.text)

pixel_update_endpoint=f" {pixela_endpoint}/{USER}/graphs/{GRAPHID}/{DATE}"
update_parameters={
    "quantity":"3.0"
}
# response=requests.put(url=pixel_update_endpoint,json=update_parameters,headers=headers)
# print(response.text)
delete_endpoint=f" {pixela_endpoint}/{USER}/graphs/{GRAPHID}/{DATE}"
delete_parameters={

}
# response=requests.delete(url=delete_endpoint,json=delete_parameters,headers=headers)