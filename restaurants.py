# Import libraries
import requests
import json

api = 'fsq36z4lgdu/IFvT42wpR6TNaN6TODBr5dEHpQILzDUL9lA='


def restaurants_data(zipcode):
    url = "https://api.foursquare.com/v3/places/search?categories={0}&near={1}&limit={2}".format(13065, zipcode, 50)
    headers = {
        "Accept": "application/json",
        "Authorization": "fsq36z4lgdu/IFvT42wpR6TNaN6TODBr5dEHpQILzDUL9lA="
    }
    response = requests.request("GET", url, headers=headers)
    results = json.loads(response.text)
    return len(results['results'])


if __name__ == '__main__':
    restaurants_data(90012)