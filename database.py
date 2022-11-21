import pyrebase
import json


class DBhandler:
    def __init__(self):
        with open('./authentication/firebase_auth.json') as f:
            config = json.load(f)
        firebase = pyrebase.initialize_app(config)
        self.db = firebase.database()

    # 가게 등록 화면
    def insert_restaurant(self, name, data, img_path):
        restaurant_info = {
            "store_phoneNum": data['store_phoneNum'],
            "store_addr": data['store_addr'],
            "store_site": data['store_site'],
            "store_open": data['store_open'],
            "store_closed": data['store_close'],
            "store_parking": data['store_parking'],
            "store_reservation": data['store_reservation'],
            "store_reservation_link": data['store_reservation_link'],
            "store_category": data['store_category'],
            "store_cost_min": data['store_cost_min'],
            "store_cost_max": data['store_cost_max'],
            "img_path": img_path
        }
        # self.db.child("restaurant").child(name).set(restaurant_info)
        # return True
        if self.restaurant_duplicate_check(name):
            self.db.child("restaurant").child(
                name).child("info").set(restaurant_info)
            print(data, img_path)
            return True
        else:
            return False

    def restaurant_duplicate_check(self, name):
        restaurants = self.db.child("restaurant").get()
        if restaurants.each() == None:
            return True
        for res in restaurants.each():
            if res.key() == name:
                return False
        return True

    # 메뉴 등록 화면
    def insert_menu(self, name, data, menuImg_path):
        menu_info = {
            "menuImg_path": menuImg_path,
            "menu_name": data['menu_name'],
            "menu_price": data['menu_price'],
            "extra_ve": data['extra_ve'],
            "extra_al": data['extra_al']
        }
        # self.db.child("restaurant").child(name).child("menu").child('menu_name').set(menu_info)
        # return True
        if self.menu_duplicate_check(data['menu_name']):
            self.db.child("restaurant").child(name).child(
                "menu").child(data['menu_name']).set(menu_info)
            print(data, menuImg_path)
            return True
        else:
            return False

    def menu_duplicate_check(self, name):
        menus = self.db.child("restaurant").child(name).child("menu").get()
        if menus.each() == None:
            return True
        for res in menus.each():
            if res.key() == name:
                return False
        return True

    # 리뷰 등록 화면
    def insert_review(self, name, data, reviewImg_path):
        review_info = {
            "review_grade": data['Range'],
            "taste": data['taste'],
            "cost": data['cost'],
            "service": data['service'],
            "cleanliness": data['cleanliness'],
            "atmosphere": data['atmosphere'],
            "revisit": data['revisit'],
            "detail-review": data['detail_review'],
            "reviewImg_path": reviewImg_path
        }
        self.db.child("review").child(name).set(review_info)
        print(data, reviewImg_path)

    # 회원 가입 화면
    def insert_member(self, name, data):  # 회원 가입 페이지
        member_info = {
            "memberInfo_password": data['memberInfo_password'],
            "memberInfo_rePassword": data['memberInfo_rePassword'],
            "memberInfo_birthDate": data['memberInfo_birthDate'],
            "memberInfo_sex": data['memberInfo_sex']
        }
        if self.id_duplicate_check(name):
            if data['memberInfo_password'] == data['memberInfo_rePassword']:
                self.db.child("member").child(name).set(member_info)
                return True
            else:
                return False

    def id_duplicate_check(self, name):
        members = self.db.child("member").get()
        if members.each() == None:
            return True
        for res in members.each():
            if res.key() == name:
                return False
        return True
