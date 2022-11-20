import requests


api_url = "http://83.222.9.103:8000/api"

             
def auth_user(login, password):
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


def get_user_by_id(user_id):
    json_data = dict(
        authorId=user_id
    )
    url = api_url + '/users/get_by_id'
    result = requests.post(url=url, json=json_data).json()['result']
    return result


def get_complaint_by_id(complaint_id):
    json_data = dict(
        complaintId=complaint_id
    )
    url = api_url + '/complaints/get_by_id'
    result = requests.post(url=url, json=json_data).json()['result']
    return result


def create_mark(longitude, latitude, description):
    json_data = dict(
        longitude=longitude,
        latitude=latitude,
        description=description
    )
    url = api_url + '/marks/create_mark'
    result = requests.post(url=url, json=json_data).json()['result']
    return result


def get_marks():
    json_data = dict()
    url = api_url + '/marks/all_marks'
    result = requests.post(url=url, json=json_data).json()['result']
    return result