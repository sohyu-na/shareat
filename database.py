import pyrebase
import json


class DBhandler:
    def __init__(self):
        with open('./authentication/firebase_auth.json') as f:
            config = json.load(f)
        firebase = pyrebase.initialize_app(config)
        self.db = firebase.database()

    def insert_restaurant(self, name, data, img_path):
        restaurant_info = {
            "store_phoneNum": data['store_phoneNum'],
            "store_addr": data['store_addr'],
            "store_site": data['store_site'],
            "store_hours": data['store_hours'],
            "store_parking": data['store_parking'],
            "store_reservation": data['store_reservation'],
            "store_reservation_link": data['store_reservation_link'],
            "store_category": data['store_category'],
            "store_cost_min": data['store_cost_min'],
            "store_cost_max": data['store_cost_max'],
            "img_path": img_path
        }

        if self.restaurant_duplicate_check(name):
            self.db.child("restaurant").child(name).set(restaurant_info)
            print(data, img_path)
            return True
        else:
            return False

    def restaurant_duplicate_check(self, name):
        restaurants = self.db.child("restaurant").get()
        for res in restaurants.each():
            if res.key() == name:
                return False
        return True
