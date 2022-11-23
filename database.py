import pyrebase
import json


class DBhandler:
    def __init__(self):
        with open('./authentication/firebase_auth.json') as f:
            config = json.load(f)
        firebase = pyrebase.initialize_app(config)
        self.db = firebase.database()

    # ===== 1) 맛집 data =====

    # DB에 저장
    def insert_restaurant(self, name, data, img_path):
        restaurant_info = {
            "store_phoneNum": data['store_phoneNum'],
            "store_addr": data['store_addr'],
            "store_site": data['store_site'],
            "store_open": data['store_open'],
            "store_close": data['store_close'],
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

    # 맛집 등록 시 중복 체크
    def restaurant_duplicate_check(self, name):
        restaurants = self.db.child("restaurant").get()
        if restaurants.each() == None:
            return True
        for res in restaurants.each():
            if res.key() == name:
                return False
        return True

    # DB 데이터 읽어오기
    def get_restaurants(self):
        restaurants = self.db.child("restaurant").get().val()

        return restaurants

    # 가게 이름으로 특정 가게 정보 가져오기
    def get_restaurant_byname(self, name):
        restaurants = self.db.child("restaurant").get()
        target_value = ""
        for res in restaurants.each():
            value = res.val()

            if res == name:
                target_value = value
            return target_value

    # ===== 2) 메뉴 data ======

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

    # ===== 3) 리뷰 데이터 ======
    def insert_review(self, data, reviewImg_path):
        review_info = {
            "nickname": data['nickname'],
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
        if data['nickname'] == "":
            review_info['nickname'] = "익명"
        self.db.child("review").push(review_info)

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
