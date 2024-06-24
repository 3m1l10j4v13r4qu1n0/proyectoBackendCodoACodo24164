import requests
import pprint

#consulta = requests.get('https://jsonplaceholder.typicode.com/users')
consulta = requests.get('https://chtolecac.pythonanywhere.com/api/test')
pp = pprint.PrettyPrinter(indent=4)

print(consulta.status_code)

pp.pprint(consulta.json())
