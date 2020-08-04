import requests

def main():
    response = requests.get("http://api.exchangeratesapi.io/latest")

    if response.status_code != 200:
        print("Status Code: ", response.status_code)
        raise Exception("There was an error!")

    # print("Content-Type: ", response.headers['Content-Type'])

    data = response.json() # returns the json-encoded content of a response (if any)
    print("JSON data: ", data)

if __name__ == "__main__":
    main()