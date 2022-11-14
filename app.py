from flask import Flask, render_template, request
import sys
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
    restaurantData = request.form

    for value in restaurantData.values():
        print(value, end=' ')
    return render_template("submit_restaurant_result.html", data=restaurantData)


# @app.route("/submit_restaurantModificationData_post", methods=['POST'])
# def reg_restaurantModificationData_submit_post():
#     restaurantModificationData = request.form

#     return render_template("submit_restaurant_result.html", data=restaurantModificationData)


# @app.route("/submit_menuData_post", methods=['POST'])
# def reg_menuData_submit_post():
#     menuData = request.form

#     return render_template("submit_restaurant_result.html", data=menuData)


# @app.route("/submit_menuModificationData_post", methods=['POST'])
# def reg_menuModificationData_submit_post():
#     menuModificationData = request.form

#     return render_template("submit_restaurant_result.html", data=menuModificationData)


# @app.route("/submit_signupData_post", methods=['POST'])
# def reg_signupData_submit_post():
#     signupData = request.form

#     return render_template("submit_restaurant_result.html", data=signupData)


# @app.route("/submit_loginData_post", methods=['POST'])
# def reg_loginData_submit_post():
#     loginData = request.form

#     return render_template("submit_restaurant_result.html", data=loginData)


# @app.route("/submit_reviewData_post", methods=['POST'])
# def reg_reviewData_submit_post():
#     reviewData = request.form

#     return render_template("submit_restaurant_result.html", data=reviewData)


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
