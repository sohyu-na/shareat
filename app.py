from flask import Flask, render_template, request, redirect, url_for
from database import DBhandler
import sys
from urllib import parse

app = Flask(__name__)

DB = DBhandler()


# [페이지 경로 설정]


@app.route("/")   # 메인홈
def goTo_mainHome():
    return redirect(url_for("list_restaurants"))


@app.route("/list")
def list_restaurants():
    page = request.args.get("page", 0, type=int)
    limit = 9

    start_idx = limit*page
    end_idx = limit*(page+1)

    data = DB.get_restaurants()  # 맛집 리스트 데이터
    count = len(data)  # 등록된 맛집 개수
    data = dict(list(data.items())[start_idx:end_idx])

    print(data, count)
    return render_template("index.html", datas=data.items(), total=count, limit=limit, page=page, page_count=int((count/9)+1))


@app.route("/detail-info/<name>/")   # 맛집 상세 정보 페이지
def goTo_detailInfo(name):
    data = DB.get_restaurant_byname(str(name))
    return render_template("detailInfo_restaurantInfo.html", data=data, name=name)


@app.route("/detail-menu/<name>/")   # 메뉴 상세 정보 페이지
def goTo_detailMenu(name):
    data = DB.get_restaurant_byname(str(name))
    return render_template("detailInfo_menu.html", data=data, name=name)


@app.route("/detail-reiview/<name>/")   # 리뷰 상세 정보 페이지
def goTo_detailReiview(name):
    data = DB.get_restaurant_byname(str(name))
    return render_template("detailInfo_review.html", data=data, name=name)


@app.route("/registration-restaurant")   # 맛집 등록 페이지
def goTo_registerRestaurant():
    return render_template("registerRestaurantInfo.html")


@app.route("/registration-menu")   # 메뉴 등록 페이지
def goTo_registerMenu():
    return render_template("registerMenu.html")


@app.route("/modification-restaurant")   # 맛집 수정 페이지
def goTo_modifyRestaurantInfo():
    return render_template("modifyRestaurantInfo.html")


@app.route("/registration-menu")   # 메뉴 수정 페이지
def goTo_modifyMenu():
    return render_template("modifyMenu.html")


@app.route("/review")   # 리뷰 등록 페이지
def goTo_writeReview():
    return render_template("writeReview.html")


@app.route("/mylist")   # 내가 찜한 맛집 페이지
def goTo_myRestaurantList():
    return render_template("myRestaurantList.html")


@app.route("/login")   # 로그인 페이지
def goTo_login():
    return render_template("login.html")


@app.route("/signup")    # 회원가입 페이지
def goTo_signup():
    return render_template("signup.html")


# [사용자 입력 데이터 받아오기]


@app.route("/submit_restaurantData_post", methods=['POST'])
def reg_restaurantData_submit_post():
    global idx
    image_file = request.files["file"]
    if image_file.filename != '':
        image_file.save("static/image/"+image_file.filename)
        image_path = "static/image/"+image_file.filename
        print(image_path)
    else:
        image_path = "./static/image/grey.png"
        print(image_path)

    data = request.form

    if DB.insert_restaurant(data['store_name'], data, image_file.filename):
        return render_template("result_맛집등록.html", data=data, image_path=image_path)
    else:
        return "Restaurant name already exist!"


@app.route("/submit_storeName_post", methods=['POST'])  # 가게 이름
def reg_storeName_submit_post():
    data = request.form['store_name']
    print(data)
    return render_template("registerMenu.html", name=data)


@app.route("/submit_menuData_post", methods=['POST'])
def reg_menuData_submit_post():
    global idx
    image_file = request.files["menu_pic"]
    if image_file.filename != '':
        image_file.save("static/image/"+image_file.filename)
        menuImg_path = "static/image/"+image_file.filename
    else:
        menuImg_path = "./static/image/grey.png"

    data = request.form
    name = data['store_name']

    if DB.insert_menu(name, data, image_file.filename):
        return render_template("result_메뉴등록.html", data=data, menuImg_path=menuImg_path)
    else:
        return "menu name already exist!"


@app.route("/submit_signupData_post", methods=['POST'])
def reg_signupData_submit_post():
    data = request.form
    if DB.insert_member(name=data['memberInfo_id'], data=data):
        return render_template("result_회원가입.html", data=data)
    else:
        return "이미 가입된 아이디이거나 비밀번호가 일치하지 않습니다."


@app.route("/submit_loginData_post", methods=['POST'])
def reg_loginData_submit_post():
    data = request.form

    for value in data.values():
        print(value, end=' ')

    return render_template("result_로그인.html", data=data)


@app.route("/submit_reviewData_post", methods=['POST'])
def reg_reviewData_submit_post():
    global idx
    image_file = request.files["picture"]
    if image_file.filename != '':
        image_file.save("static/image/"+image_file.filename)
        reviewImg_path = "static/image/"+image_file.filename
    else:
        reviewImg_path = "./static/image/grey.png"
    data = request.form

    DB.insert_review(data=data,
                     reviewImg_path=reviewImg_path)

    return render_template("result_리뷰등록.html", data=data, reviewImg_path=reviewImg_path)


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
