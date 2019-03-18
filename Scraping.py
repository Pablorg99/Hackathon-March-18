# -*- coding: utf-8 -*-
import requests
import json


url = "https://transparentia.newtral.es/api/get/byName/pedro-sanchez-calderon"

parametros = {
    'api_key':"eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJwZXBlbWFycXVlem9mQGdtYWlsLmNvbSIsImp0aSI6IjVmMzI4ZTVlLTVkZDctNDIzYy1hYzg2LTE2MjcyMTdkYTUyMyIsImlzcyI6IkFFTUVUIiwiaWF0IjoxNTUyMzI1NTI1LCJ1c2VySWQiOiI1ZjMyOGU1ZS01ZGQ3LTQyM2MtYWM4Ni0xNjI3MjE3ZGE1MjMiLCJyb2xlIjoiIn0.b3O8zc1a1tHQER9_F7xrkw-X8_pHzlzJGFhA_j2f8Uc"
}

headers = {
        'cache-control': "no-cache"
}

response = requests.request("GET", url)

print (response.text)