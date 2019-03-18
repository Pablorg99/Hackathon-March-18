import json
import requests

response = requests.request("GET", 'https://transparentia.newtral.es/api/get/byName/marcos-ortuno-soto')
total_salary = 0
politician_json = response.json()
charges_list = politician_json["cargos"]
for charge in charges_list:
    salaries_charge = charge["salarios"]
    for salary in salaries_charge:
        total_salary += salary["salario_mensual"]

print(total_salary)