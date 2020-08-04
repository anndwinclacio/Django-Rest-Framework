# FOR LOG IN - existing user

import requests

def client():
    token_h = "Token eaf02e210e35e48ce5e1938170dbef50e0f5dbad"
    # credentials = {"username" : "admin", "password" : "123" }

    # response = requests.post("http://127.0.0.1:8000/api/rest-auth/login/", 
    #                          data=credentials)

    headers = {"Authorization" : token_h}
    response = requests.get("http://127.0.0.1:8000/api/profiles/",
                             headers=headers)

    print("Status Code: ", response.status_code)
    response_data = response.json()
    print(response_data)


if __name__ == "__main__":
    client()