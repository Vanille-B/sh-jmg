import requests

headers = {
    'Authorization': 'Bearer YOUR_API_TOKEN',
}



# List schedules // GET
list_schedules = requests.get('https://shiftheroes.fr/api/v1/plannings', headers=headers)
print(list_schedules.json())


# List slots // GET
list_slots = requests.get('https://shiftheroes.fr/api/v1/plannings/JefZ2o/shifts', headers=headers)
print(list_slots.json())
json_data = list_slots.json()

for item in json_data:
    print("Nouvel élément:")
    for key, value in item.items():
        print(f"{key}: {value}")
    print()


# Allows to book a slot // POST
booking_slot = requests.post('https://shiftheroes.fr/api/v1/plannings/JefZ2o/shifts/bXF4w06/reservations', headers=headers)  