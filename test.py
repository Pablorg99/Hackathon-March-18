import json
import requests

politician_json = requests.request("GET", 'https://transparentia.newtral.es/api/get/byName/marcos-ortuno-soto')
total_salary = 0
charges_list = politician_json.text["cargos"]
for charge in charges_list:
    salaries_charge = charge["salarios"]
    for salary in salaries_charge:
        total_salary += salary["salario_mensual"]
print(total_salary)