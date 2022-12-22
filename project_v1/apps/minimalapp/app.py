import os

from flask import Flask, flash, redirect, render_template, request, url_for

from apps.Module import PythonApplication1 as PA1

# 建立 Flask 類別的實體 (instance)
app = Flask(__name__)

# 增加 SECRET_KEY
app.config["SECRET_KEY"] = os.urandom(12).hex()


@app.route("/")
def index():
    print("測試一下拉")
    print(PA1.cnt[0])
    return render_template("index.html")


@app.route("/result", methods=["GET", "POST"])
# @app.route("/result")
def result():

    data = [{"name": "綜合信用分數", "value": PA1.ratio}]

    # dataset = {
    #     "source": [
    #         ["score", "amount", "product"],
    #         [1, 58, "Matcha Latte"],
    #         [2, 78, "Milk Tea"],
    #         [1, 41, "Cheese Cocoa"],
    #         [3, 12, "Cheese Brownie"],
    #         [1, 20, "Matcha Cocoa"],
    #         [3, 79, "Tea"],
    #         [1, 91, "Orange Juice"],
    #         [2, 10, "Lemon Juice"],
    #         [3, 20, "Waalnut Brownie"],
    #     ]
    # }

    # [分數, 次數, words]
    dataset_p = PA1.positive_dataset
    dataset_n = PA1.negative_dataset
    dataset_b = PA1.bad_dataset

    if request.method == "POST":
        url = request.form["url"]

        # 重新導向
        return redirect(
            url_for("result"),
            data=data,
            details=PA1.data_details,
            dataset_p=dataset_p,
            dataset_n=dataset_n,
            dataset_b=dataset_b,
        )

    return render_template(
        "result.html",
        data=data,
        details=PA1.data_details,
        dataset_p=dataset_p,
        dataset_n=dataset_n,
        dataset_b=dataset_b,
    )
    # 不是 result.html ，應該是要傳到 爬蟲程式
    # return py?
