from dataclasses import dataclass

import requests


@dataclass
class Service:
    def __post_init__(self):
        self.service_endpoint = "https://jsonplaceholder.typicode.com/todos"

    def create_user(self, payload):
        r = requests.post(self.service_endpoint, json=payload)
        return r

    def get_user_by_id(self, user_id: str):
        r = requests.get(f"{self.service_endpoint}/{user_id}")
        return r

    def get_users(self):
        r = requests.get(self.service_endpoint)
        return r
