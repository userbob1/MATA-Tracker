import requests
import sqlite3
import time

con = sqlite3.connect("cars.db")
cur = con.cursor()

def init_cars() -> dict:
    cars = {}
    r = cur.execute("SELECT name FROM sqlit_schema WHERE type ='table'")
    for car_name in r.fetchall():
        cars[car_name[0]] = [] # list of tuples
    return cars

def start():
    cars_map = init_cars()
    while True:
        r = requests.get('https://track.mata.org:7170/allCars')
        r_data = r.json()
        r_data.pop('32768', None)
        now = int(time.time())
        for car_data in r_data.items():
            name = car_data[0]
            location = (car_data[1][0], car_data[1][1], now)
            if name not in cars_map:
                cars_map[name] = []
            cars_map[car_data[0]].append(location)