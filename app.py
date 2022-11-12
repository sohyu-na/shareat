from flask import Flask, render_template, request
import sys
app = Flask(__name__)

# 메인홈
@app.route("/")
def main_home():
    return render_template("index.html")

# 맛집 등록
@app.route("../templates/registerRestaurantInfo.html")
def register_restaurant():
    return render_template("registerRestaurant.html")

# 내가 찜한 밋집
@app.route("/mylist")
def register_restaurant():
    return render_template("myRestaurantList.html")

# 로그인
@app.route("../templates/login.html")
def register_restaurant():
    return render_template("login.html")

# 회원가입
@app.route("../templates/signup.html")
def register_restaurant():
    return render_template("signup.html")


# if __name__ == '__main__':
#     app.run('0.0.0.0', port=5000, debug=True)
