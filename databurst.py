import requests


def generate_name():
    response = requests.get("https://randomuser.me/api/?inc=name")
    data = response.json()
    name = data["results"][0]["name"]
    return f'{name["first"]} {name["last"]}'


def generate_address():
    response = requests.get("https://randomuser.me/api/?inc=location")
    data = response.json()
    location = data["results"][0]["location"]
    street = location["street"]
    city = location["city"]
    return f'{street["number"]} {street["name"]}, {city}'


def generate_phone_number():
    response = requests.get("https://randomuser.me/api/?inc=phone")
    data = response.json()
    phone = data["results"][0]["phone"]
    return phone


def generate_email():
    response = requests.get("https://randomuser.me/api/?inc=email")
    data = response.json()
    email = data["results"][0]["email"]
    return email
