import json
import requests

response = requests.request("GET", 'https://transparentia.newtral.es/api/get/byName/marcos-ortuno-soto')
<<<<<<< HEAD

total_salary = 0

politician_json = response.json()

charges_list = politician_json["cargos"]


=======
total_salary = 0
politician_json = response.json()
charges_list = politician_json["cargos"]
>>>>>>> 0d8f7d9ed5a34d0b78da10dee49c686bb029f42a
for charge in charges_list:
    salaries_charge = charge["salarios"]
    for salary in salaries_charge:
        total_salary += salary["salario_mensual"]

print(total_salary)