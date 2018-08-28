#!/usr/bin/python3
import geocoder
import requests


class OneBite:
    def __init__(self):
        self.token = None
        self.user_id = None
        self.session = requests.session()

    def register(self, first_name, last_name, email, password):
        headers = {
            'Host': 'one-bite-api.barstoolsports.com',
            'Content-Type': 'application/json',
            'User-Agent': 'One%20Bite/420 CFNetwork/808.2.16 Darwin/16.3.0',
            'Connection': 'keep-alive',
            'X-App-Build': '420',
            'Accept': '*/*',
            'Accept-Language': 'en-us',
            'X-App-Id': 'ios',
            'Accept-Encoding': 'gzip, deflate'
        }
        payload = {
            'email': email,
            'firstName': first_name,
            'lastName': last_name,
            'password': password
        }
        # ['token']
        # ['user']['id']
        response = self.session.post('https://one-bite-api.barstoolsports.com/auth/register', json=payload, headers=headers)
        self.token = response.json()['token']
        self.user_id = response.json()['user']['id']
        return response.json()

    def get_feed(self):
        # make sure user_id is not None
        headers = {
            'Host': 'one-bite-api.barstoolsports.com',
            'User-Agent': 'One%20Bite/420 CFNetwork/808.2.16 Darwin/16.3.0',
            'Connection': 'keep-alive',
            'X-App-Build': '420',
            'Accept': '*/*',
            'Accept-Language': 'en-us',
            'Authorization': f'Bearer {self.token}',
            'X-App-Id': 'ios',
            'Accept-Encoding': 'gzip, deflate'
        }
        return self.session.get(f'https://one-bite-api.barstoolsports.com/user/{self.user_id}/review-feed', headers=headers)

    def check_username_exists_already(self, username):
        headers = {
            'Host': 'one-bite-api.barstoolsports.com',
            'User-Agent': 'One%20Bite/420 CFNetwork/808.2.16 Darwin/16.3.0',
            'Connection': 'keep-alive',
            'X-App-Build': '420',
            'Accept': '*/*',
            'Accept-Language': 'en-us',
            'Authorization': f'Bearer {self.token}',
            'X-App-Id': 'ios',
            'Accept-Encoding': 'gzip, deflate'
        }
        return self.session.get(f'https://one-bite-api.barstoolsports.com/username/{username}', headers=headers).json()['exists']

    def change_username(self, new_username):
        headers = {
            'Host': 'one-bite-api.barstoolsports.com',
            'Content-Type': 'application/json',
            'User-Agent': 'One%20Bite/420 CFNetwork/808.2.16 Darwin/16.3.0',
            'Connection': 'keep-alive',
            'X-App-Build': '420',
            'Accept': '*/*',
            'Accept-Language': 'en-us',
            'X-App-Id': 'ios',
            'Accept-Encoding': 'gzip, deflate',
            'Authorization': f'Bearer {self.token}'
        }
        payload = {
            'username': new_username
        }
        # assert response.json()['username'] == new_username
        response = self.session.put('https://one-bite-api.barstoolsports.com/user/me', json=payload, headers=headers)
        return response

    def get_venues_near_me(self):
        [lat, lng] = geocoder.ip('me').latlng
        headers = {
            'Host': 'one-bite-api.barstoolsports.com',
            'User-Agent': 'One%20Bite/420 CFNetwork/808.2.16 Darwin/16.3.0',
            'Connection': 'keep-alive',
            'X-App-Build': '420',
            'Accept': '*/*',
            'Accept-Language': 'en-us',
            'Authorization': f'Bearer {self.token}',
            'X-App-Id': 'ios',
            'Accept-Encoding': 'gzip, deflate'
        }
        query_string_parameters = {
            'lat': lat,
            'long': lng
        }
        # response.json() # type: list # distance, address venue id, review stats, etc.
        response = self.session.get('https://one-bite-api.barstoolsports.com/venue', params=query_string_parameters, headers=headers)
        return response

    def put_me_elsewhere(self, latitude, longitude):
        headers = {
            'Host': 'one-bite-api.barstoolsports.com',
            'Content-Type': 'application/json',
            'User-Agent': 'One%20Bite/420 CFNetwork/808.2.16 Darwin/16.3.0',
            'Connection': 'keep-alive',
            'X-App-Build': '420',
            'Accept': '*/*',
            'Accept-Language': 'en-us',
            'X-App-Id': 'ios',
            'Accept-Encoding': 'gzip, deflate',
            'Authorization': f'Bearer {self.token}'
        }
        payload = {
            'loc': {
                'coordinates': [
                    longitude,
                    latitude
                ],
                'type': 'Point'
            }
        }
        # response.json()
        response = self.session.put('https://one-bite-api.barstoolsports.com/user/me', json=payload, headers=headers)
        return response

    def get_me(self):
        headers = {
            'Host': 'one-bite-api.barstoolsports.com',
            'User-Agent': 'One%20Bite/420 CFNetwork/808.2.16 Darwin/16.3.0',
            'Connection': 'keep-alive',
            'X-App-Build': '420',
            'Accept': '*/*',
            'Accept-Language': 'en-us',
            'Authorization': f'Bearer {self.token}',
            'X-App-Id': 'ios',
            'Accept-Encoding': 'gzip, deflate'
        }
        # response.json()
        response = self.session.get(f'https://one-bite-api.barstoolsports.com/user/{self.user_id}', headers=headers)
        return response

    def get_venue_by_id(self, venue_id):
        headers = {
            'Host': 'one-bite-api.barstoolsports.com',
            'User-Agent': 'One%20Bite/420 CFNetwork/808.2.16 Darwin/16.3.0',
            'Connection': 'keep-alive',
            'X-App-Build': '420',
            'Accept': '*/*',
            'Accept-Language': 'en-us',
            'Authorization': f'Bearer {self.token}',
            'X-App-Id': 'ios',
            'Accept-Encoding': 'gzip, deflate'
        }
        # response.json()
        response = self.session.get(f'https://one-bite-api.barstoolsports.com/venue/{venue_id}', headers=headers)
        return response

    def get_my_reviews(self):
        headers = {
            'Host': 'one-bite-api.barstoolsports.com',
            'User-Agent': 'One%20Bite/420 CFNetwork/808.2.16 Darwin/16.3.0',
            'Connection': 'keep-alive',
            'X-App-Build': '420',
            'Accept': '*/*',
            'Accept-Language': 'en-us',
            'Authorization': f'Bearer {self.token}',
            'X-App-Id': 'ios',
            'Accept-Encoding': 'gzip, deflate'
        }
        query_string_parameters = {
            'limit': 10,
            'sort': '-date'
        }
        # response.json()
        response = self.session.get(f'https://one-bite-api.barstoolsports.com/user/{self.user_id}', params=query_string_parameters, headers=headers)
