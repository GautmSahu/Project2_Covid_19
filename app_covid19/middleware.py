import json
import requests
from Project2_Covid_19.settings import Covid_19_file
class COVID19Middleware:
    def __init__(self,get_response):
        self.get_response=get_response
        res = requests.get("https://api.covid19india.org/state_district_wise.json")
        str_data = json.loads(res.text)
        dict_data = json.dumps(str_data)
        file = open(Covid_19_file, "w")
        file.write(dict_data)

    def __call__(self,request, *args, **kwargs):
        response=self.get_response(request)
        return response




