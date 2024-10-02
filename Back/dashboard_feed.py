import requests
import json

class DashFeeder:

    def send_data(self, device, variable, value):
        
        url = f"https://industrial.api.ubidots.com/api/v1.6/devices/{device}/{variable}/values"

        payload = json.dumps({
        "value": value
        })
        
        headers = {
        'Content-Type': 'application/json',
        'X-Auth-Token': 'BBUS-YQtbv7D8F9sUFodo9xhmQ1T4pxdqGi',
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        return response.status_code

if __name__ == '__main__':
    DashFeeder().send_data('rasp', 'last_transaction', 500)