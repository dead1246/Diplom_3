import requests

import urls


class UserApi:
    def create_user(self, payload):
        return requests.post(urls.REGISTER_USER, json=payload)

    def delete_user(self, token):
        return requests.delete(urls.DELETE_USER, headers={"Authorization": token})
