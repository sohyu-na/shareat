import pyrebase
import json

class DBhandler:
    def __init__(self ):
        with open('./authentication/firebase_auth.json') as f:
            config=json.load(f )
        firebase = pyrebase.initialize_app(config)
        self.db = firebase.database()
        
    def insert_restaurant(self, name, data, img_path):
        restaurant_info ={
            "store-phoneNum":data['store-phoneNum'],
            "store-addr":data['store-addr'],
            "store-site":data['store-site'],
            "store-hours":data['store-hours'],
            "store-parking":data['store-parking'],
            "store-reservation":data['store-reservation'],
            "store-category":data['store-category'],
            "store-cost-min":data['store-cost-min'],
            "store-cost-max":data['storecost-max'],
            "img_path": img_path
        }
        if self.restaurant_duplicate_check(name):
            self.db.child("restaurant").child(name).set(restaurant_info)
            print(data,img_path)
            return True
        else:
            return False
        
    def restaurant_duplicate_check(self, name):
        restaurants = self.db.child("restaurant").get()
        for res in restaurants.each():
            if res.key() == name:
                return False
        return True    
    
    
    
    

    