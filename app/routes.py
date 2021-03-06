import json

from flask import jsonify, request
from app import utils
from flask import current_app as app
from .models import db, RequestsModel


@app.route("/")
def index():
    response = jsonify(
        message=(
            "Available routes are: / ; /get_requests , /fibonacci/<int> ; /power/<x>/<y> ; /factorial/<int:n>"
        )
    )
    response.status_code = 200

    db.session.add(
        RequestsModel(request.url, str(json.loads(response.get_data().decode("utf-8"))))
    )
    db.session.commit()

    return response


@app.route("/get_requests")
def get_requests():
    all_data = RequestsModel.query.all()
    print(all_data)
    response = jsonify(all_requests=(str(all_data)))
    response.status_code = 200

    return response


@app.route("/fibonacci/<int:n>")
def fibonacci(n):
    response = jsonify(fibonacci=utils.nth_fibonacci(n))
    response.status_code = 200

    db.session.add(
        RequestsModel(request.url, str(json.loads(response.get_data().decode("utf-8"))))
    )
    db.session.commit()

    return response


@app.route("/fibonacci/<invalid_path_parameter>")
def fibonacci_invalid_path(invalid_path_parameter):
    response = jsonify(
        message=(
            "Size must be a positive integer. Actual {}".format(invalid_path_parameter)
        )
    )
    response.status_code = 400

    db.session.add(
        RequestsModel(request.url, str(json.loads(response.get_data().decode("utf-8"))))
    )
    db.session.commit()

    return response


@app.route("/power/<x>/<y>")
def power(x, y):
    try:
        x = float(x)
        y = float(y)
    except ValueError:
        response = jsonify(
            message=(
                "Both numbers must be float or integer. Now x is {}, and y is {}".format(
                    type(x), type(y)
                )
            )
        )
        response.status_code = 400

        db.session.add(
            RequestsModel(
                request.url, str(json.loads(response.get_data().decode("utf-8")))
            )
        )
        db.session.commit()

        return response

    response = jsonify(power=pow(x, y))
    response.status_code = 200

    db.session.add(
        RequestsModel(request.url, str(json.loads(response.get_data().decode("utf-8"))))
    )
    db.session.commit()

    return response


@app.route("/factorial/<int:n>")
def factorial(n):

    response = jsonify(factorial=utils.factorial(n))
    response.status_code = 200

    db.session.add(
        RequestsModel(request.url, str(json.loads(response.get_data().decode("utf-8"))))
    )
    db.session.commit()
    return response


@app.route("/factorial/<invalid_path_parameter>")
def factorial_invalid_path(invalid_path_parameter):
    response = jsonify(
        message=(
            "Parameter need to be integer. Now is {}".format(
                type(invalid_path_parameter)
            )
        )
    )
    response.status_code = 400

    db.session.add(
        RequestsModel(request.url, str(json.loads(response.get_data().decode("utf-8"))))
    )
    db.session.commit()

    return response
