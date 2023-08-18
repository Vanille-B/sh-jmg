import requests

headers = {
    'Authorization': 'Bearer YOUR_API_TOKEN',
}



# TODO: List schedules // GET
response = requests.get('https://shiftheroes.fr/api/v1/plannings', headers=headers)


# TODO: List slots // GET
response = requests.get('https://shiftheroes.fr/api/v1/plannings/JefZ2o/shifts', headers=headers)
# print(response.text)

# Allows to book a slot // POST
response = requests.post('https://shiftheroes.fr/api/v1/plannings/JefZ2o/shifts/bXF4w06/reservations', headers=headers)