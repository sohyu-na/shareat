from flask import Flask, render_template, request
import sys
from urllib import parse
app = Flask(__name__)

# 메인홈


@app.route("/")
def goTo_mainHome():
    return render_template("index.html")

# 맛집 등록


@app.route("/registration")
def goTo_registerRestaurant():
    return render_template("registerRestaurantInfo.html")

# 내가 찜한 밋집


@app.route("/mylist")
def goTo_myRestaurantList():
    return render_template("myRestaurantList.html")

# 로그인


@app.route("/login")
def goTo_login():
    return render_template("login.html")

# 회원가입


@app.route("/signup")
def goTo_signup():
    return render_template("signup.html")


# 입력 데이터 받아오기


@app.route("/submit_restaurantData_post", methods=['POST'])
def reg_restaurantData_submit_post():
    data = request.form

    for value in data.values():
        print(value, end=' ')

    return render_template("result_맛집등록.html", data=data)


@app.route("/submit_menuData_post", methods=['POST'])
def reg_menuData_submit_post():
    data = request.form

    for value in data.values():
        print(value, end=' ')

    return render_template("result_메뉴등록.html", data=data)


@app.route("/submit_signupData_post", methods=['POST'])
def reg_signupData_submit_post():
    data = request.form

    for value in data.values():
        print(value, end=' ')

    return render_template("result_회원가입.html", data=data)


@app.route("/submit_loginData_post", methods=['POST'])
def reg_loginData_submit_post():
    data = request.form

    for value in data.values():
        print(value, end=' ')

    return render_template("result_로그인.html", data=data)


@app.route("/submit_reviewData_post", methods=['POST'])
def reg_reviewData_submit_post():
    data = request.form

    for value in data.values():
        print(value, end=' ')

    return render_template("result_리뷰등록.html", data=data)


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
