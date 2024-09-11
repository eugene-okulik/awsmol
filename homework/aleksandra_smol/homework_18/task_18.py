import requests

base_url = "https://api.restful-api.dev/objects"


def new_post():
    body = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    response = requests.post(url=base_url, json=body)
    return response.json()['id']


def clear(post_id):
    url = f'{base_url}/{post_id}'
    requests.delete(url=url)


def get_list_of_all_objects():
    response = requests.get(base_url)
    assert response.status_code == 200, "Status code is not correct"
    assert len(response.json()) == 13, f"The request length is {len(response.json())}"


def get_list_of_objects_by_ids():
    response = requests.get(f"{base_url}?id=3&id=5&id=10")
    assert response.status_code == 200, f"Status code == {response.status_code}"


def get_single_object():
    post_id = new_post()
    response = requests.get(f"{base_url}/{post_id}")
    assert response.json()['id'] == post_id
    clear(post_id)


def add_object():
    body = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    response = requests.post(url=base_url, json=body)
    assert response.status_code == 200, f"Status code is {response.status_code}"
    assert response.json()['name'] == "Apple MacBook Pro 16", "Name is not correct"


def update_object():
    post_id = new_post()
    url = f"{base_url}/{post_id}"
    body = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 2049.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB",
            "color": "silver"
        }
    }
    response = requests.put(url=url, json=body)
    assert response.status_code == 200, f"Status code is {response.status_code}"
    assert response.json()["data"]["price"] == 2049.99, f"Price is {response.json()['data']['price']}"
    clear(post_id)


def partially_update_object():
    post_id = new_post()
    url = f"{base_url}/{post_id}"
    body = {
        "name": "Apple MacBook Pro 16 (Updated Name)"
    }
    response = requests.patch(url=url, json=body)

    assert response.status_code == 200, f"Status code is {response.status_code}"
    assert response.json()["name"] == "Apple MacBook Pro 16 (Updated Name)", f"Name is {response.json()['name']}"
    clear(post_id)


def delete_object():
    post_id = new_post()
    url = f'{base_url}/{post_id}'

    response = requests.delete(url=url)
    assert response.status_code == 200, f"Status code is {response.status_code}"
    assert response.json()["message"] == f"Object with id = {post_id} has been deleted.", 'Message is not correct'


get_list_of_all_objects()
get_list_of_objects_by_ids()
get_single_object()
add_object()
update_object()
partially_update_object()
delete_object()
