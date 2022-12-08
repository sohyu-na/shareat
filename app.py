from flask import Flask, render_template, request, flash, redirect, url_for, session
from database import DBhandler
import hashlib
import sys
from urllib import parse
import math

app = Flask(__name__)

DB = DBhandler()


# ===== [페이지 경로 설정] =====


@app.route("/")
def goTo_mainHome():
    return redirect(url_for("list_restaurants"))

# 메인홈(맛집 리스트)
@app.route("/shareat")
def list_restaurants():
    page = request.args.get("page", 0, type=int)
    category = request.args.get("category", "all")  # 선택한 맛집 카테고리 값
    sort = request.args.get("sort", "grade")   # 선택한 목록 정렬 순서 기준

    limit = 9
    start_idx = limit*page
    end_idx = limit*(page+1)

    # 선택한 카테고리 맛집 목록 추출
    if category == "all":
        data = DB.get_restaurants()
    else:
        data = DB.get_restaurants_bycategory(category)

    # 맛집 목록 순서 정렬 (평점순/최신순)
    if sort == "grade":
        data = dict(
            sorted(data.items(), key=lambda x: x[1]['info']['store_grade'], reverse=True))
    else:
        data = dict(
            sorted(data.items(), key=lambda x: x[1]['time']['timestamp'], reverse=True))

    # 평점순 정렬
    # data = dict(
    #     sorted(data.items(), key=lambda x: x[1]['info']['store_grade'], reverse=True))

    # 최신순 정렬
    # data = dict(
    #     sorted(data.items(), key=lambda x: x[1]['time']['timestamp'], reverse=False))

    # 선택한 목록 순서 기준으로 맛집 목록 정렬
    # if sort == "grade":
    #     data = dict(sorted(data.items(), key=lambda x: x[1]['info']['store_grade']))

    if data == None:
        count = 0    # 등록된 맛집 개수
        return render_template("index.html", total=count, page=page)
    else:
        count = len(data)
        data = dict(list(data.items())[start_idx: end_idx])
        page_count = len(data)

        return render_template("index.html", datas=data.items(), total=count, limit=limit, page=page, page_count=math.ceil(count/9), category=category, sort=sort)

#내찜맛 화면 출력
@app.route("/myRestaurantList")
def goTo_myRestaurantList():
    userId=session['id']
    page = request.args.get("page", 0, type=int)
    limit = 9
    
    start_idx = limit*page
    end_idx = limit*(page+1)
    data=[]
    data = DB.get_mylist(userId) # 찜한 맛집 리스트 데이터

    if data == None:
        count = 0    # 등록된 맛집 개수
        return render_template("myRestaurantList.html", datas=data, total=count, limit=limit, page=page, page_count=int((count/9)+1))
    else:
        count = len(data)
        list_data = dict(list(data.items())[start_idx:end_idx])
        return render_template("myRestaurantList.html", datas=list_data.items(), total=count, limit=limit, page=page, page_count=int((count/9)+1))


# 맛집 상세정보 페이지
@app.route("/detail-info/<name>")
def goTo_detailInfo(name):
    data = DB.get_restaurant_byname(str(name))
    return render_template("detailInfo_restaurantInfo.html", data=data, name=name)


#찜하기 버튼누르면 데베에 추가하고 다시 맛집 상세정보 페이지로 이동
@app.route("/submit_like_post", methods=['POST'])
def submit_like_post():
    data = request.form
    name=data["store_name"]
    userId=data["userId"]
    #likechecked=data["likechecked"]
    DB.insert_mylist(name, userId)
    resdata = DB.get_restaurant_byname(name)
    return redirect(url_for("goTo_detailInfo", name=name))


# 메뉴 상세 정보 페이지
@app.route("/detail-menu/<name>")
def goTo_detailMenu(name):
    data = DB.get_restaurant_byname(str(name))
    menu = DB.get_menus_byname(str(name))

    if menu == None:
        count = 0    # 등록된 메뉴 개수
        # total=count
        return render_template("detailInfo_menu.html", data=data, name=name, total=count)

    else:
        menu_data = DB.get_menu_byname(str(name))
        count = len(menu)
        # total=count
        return render_template("detailInfo_menu.html", menu_data=menu_data, data=data, name=name, total=count)


# 리뷰 상세 정보 페이지
@app.route("/detail-review/<name>")
def goTo_detailReiview(name):
    data = DB.get_restaurant_byname(str(name))
    rev = DB.get_reviews_byname(str(name))
    print(rev)

    if rev == None:
        count = 0    # 등록된 리뷰 개수
        return render_template("detailInfo_review.html", data=data, name=name, total=count)  #total=count
    
    else:
        review_data = DB.get_review_byname(str(name))
        count = len(rev)
        # total=count
        return render_template("detailInfo_review.html", review_data=review_data, data=data, name=name, total=count)



# 맛집 등록 페이지
@app.route("/registration-restaurant")
def goTo_registerRestaurant():
    return render_template("registerRestaurantInfo.html")


# 메뉴 등록 페이지
@app.route("/registration-menu")
def goTo_registerMenu():
    return render_template("registerMenu.html")


# 맛집 수정 페이지
@app.route("/modify-info/<name>")   
def goTo_modifyInfo(name):
    data = DB.get_restaurant_byname(str(name))
    return render_template("modifyRestaurantInfo.html", data=data, name=name)


 # 메뉴 수정 페이지s
@app.route("/registration-menu")
def goTo_modifyMenu():
    return render_template("modifyMenu.html")


# 메뉴 수정 - 가게 이름 받아오기
@app.route("/modifyMenu_storeName_post", methods=['POST'])
def reg_storeName_modifyMenu_post():
    data = request.form['store_name']
    print(data)
    return render_template("modifyMenu.html", name=data)

# 리뷰 등록 페이지
@app.route("/review")
def goTo_writeReview():
    return render_template("writeReview.html")

# 리뷰 등록 - 가게 이름 받아오기
@app.route("/review_storeName_post", methods=['POST']) 
def reg_storeName_review_post():
    data = request.form['store_name']
    print(data)
    return render_template("writeReview.html", name=data)


# 로그인 페이지
@app.route("/login")
def goTo_login():
    return render_template("login.html")


# 회원가입 페이지
@app.route("/signup")
def goTo_signup():
    return render_template("signup.html")


# ===== [사용자 입력 데이터 받아오기] =====

#가게정보 삽입
@app.route("/submit_restaurantData_post", methods=['POST'])
def reg_restaurantData_submit_post():
    global idx
    image_file = request.files["file"]
    if image_file.filename != '':
        image_file.save("./static/image/{}".format(image_file.filename))
        image_path = "./static/image/{}".format(image_file.filename)
        print(image_path)
    else:
        image_path = "./static/image/grey.png"
        image_file.filename = "grey.png"
        print(image_path)

    data = request.form

    if DB.insert_restaurant(data['store_name'], data, image_path):
        return render_template("result_맛집등록.html", data=data, image_path=image_path)
    else:
        return "Restaurant name already exists!"


@app.route("/submit_storeName_post", methods=['POST'])  # 가게 이름
def reg_storeName_submit_post():
    data = request.form['store_name']
    print(data)
    return render_template("registerMenu.html", name=data)


# 데이터베이스에 회원정보 넣기
@app.route("/submit_signupData_post", methods=['POST'])
def reg_signupData_submit_post():
    data = request.form
    pw = request.form['memberInfo_password']
    rePw = request.form['memberInfo_rePassword']
    pw_hash = hashlib.sha256(pw.encode('utf-8')).hexdigest()
    rePw_hash = hashlib.sha256(rePw.encode('utf-8')).hexdigest()

    if pw_hash == rePw_hash:
        if DB.insert_member(name=data['memberInfo_id'], data=data, pw_hash=pw_hash):
            return render_template("login.html")
        else:
            flash("이미 가입된 아이디이거나 비밀번호가 일치하지 않습니다.")
            return render_template("signup.html")
    else:
        flash("비밀번호 재확인이 비밀번호와 일치하지 않습니다.")
        return render_template("signup.html")


@ app.route("/submit_loginData_post", methods=['POST'])
def reg_loginData_submit_post():
    id_ = request.form['input_id']
    pw = request.form['input_password']
    pw_hash = hashlib.sha256(pw.encode('utf-8')).hexdigest()

    if DB.find_user(id_, pw_hash):
        session['id'] = id_
        return redirect(url_for("list_restaurants"))
    else:
        flash("Wrong ID or PW!")
        return render_template("login.html")


# 로그아웃
@app.route("/logout")
def logout_user():
    session.clear()
    return redirect(url_for("list_restaurants"))


# [사용자 입력 데이터 받아오기] - 메뉴
@ app.route("/submit_menuData_post", methods=['POST'])
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

# [사용자 입력 데이터 받아오기] - 리뷰


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
    name = data['store_name']

    DB.insert_review(name, data, reviewImg_path, userID)

    return redirect(url_for("goTo_detailReiview", name=name))


@app.route("/submit_review_agree_userId", methods=['POST'])
def submit_review_agree_userId():
    data = request.form
    name = data['store_name']
    userID = data['userID']
    review_agree_userId = data['review_agree_userId']
    DB.insert_review_agree_userId(name, userID, review_agree_userId)
    
    return redirect(url_for("goTo_detailReiview", name=name))

@app.route("/submit_review_userID", methods=['POST'])  # 리뷰 작성한 유저의 userID 넘겨줌
def submit_review_userID():
    data = request.form
    name = data['store_name']
    userID = data['userID']
    # agreeUsers_num = DB.get_agreeNum_byname(name, userID)
    return redirect(url_for("goTo_detailReiview", name=name))
    
# #동의 버튼 누를 시에 동의한 사람 수 새로고침
# @app.route("/", methods=['POST'])  
# def submit_review_userID():

#     return redirect(url_for("goTo_detailReiview", name=name))



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

if __name__ == "__main__":
    # app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
