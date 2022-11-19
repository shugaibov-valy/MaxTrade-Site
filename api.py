import requests


api_url = "http://83.222.9.103:8000/api"

             
def auth_user(login, password):
    json_data = dict()
    url = api_url + '/users/auth'
    json_data = dict(
        login=login,
        password=password
    )
    result = requests.post(url=url, json=json_data).json()
    return result


def get_complaints():
    json_data = dict()
    url = api_url + '/complaints/all_complaints'
    result = requests.post(url=url, json=json_data).json()['result']
    return result
