import requests

headers = {
    'Authorization': 'Bearer YOUR_API_TOKEN',
}

# Allows to book a slot
response = requests.post('https://shiftheroes.fr/api/v1/plannings/rwf5Gy/shifts/VVFzyYD/reservations', headers=headers)


# TODO: List schedules
# TODO: List slots
