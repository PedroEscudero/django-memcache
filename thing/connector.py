import http.client
import json

class Connector(object):
    ENDPOINTS = [
        '/awardees.json',
        '/newspapers.json',
        '/lccn/sn86069873/1900-01-05/ed-1/seq-2.json',
        '/lccn/sn86069873/1900-01-05/ed-1/seq-3.json'
    ]
    DOMAIN = 'chroniclingamerica.loc.gov'

    def __init__(self, endpoints = ENDPOINTS):
        self.endpoints = endpoints

    def call_endpoints(self):
        response = []
        for endpoint in self.endpoints:
            response.append(self.request(endpoint))
        return response

    def request(self, endpoint):
        headers = {
            'content-type': 'application/json',
            'Cache-Control': 'no-cache',
        }
        connection = http.client.HTTPSConnection(self.DOMAIN)
        connection.request('GET', endpoint, '', headers)
        response = connection.getresponse()
        json_string = response.read().decode('utf-8')
        data = json.loads(json_string)
        connection.close()
        return data
