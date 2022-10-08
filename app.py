import requests
import sqlite3

con = sqlite3.connect("cars.db")
r = requests.get('https://track.mata.org:7170/allCars')
cars = r.json()
cars.pop('32768', None)
for i in cars.items():
    print(f"car: {i[0]}, location: {i[1]}")
