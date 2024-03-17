from flask import Blueprint, jsonify, request
from http import HTTPStatus

main = Blueprint('index_blueprint', __name__)

@main.route('/')
def index():
    try:
        return "Ok"
    except Exception as ex:


        response = jsonify({'Mensaje': "Error Interno Del Servidor"})
        return response, HTTPStatus.INTERNAL_SERVER_ERROR