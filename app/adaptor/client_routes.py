from app.application import client_service
from app.domain.model import Client
from flask import Flask, jsonify, request
from flask_restful import reqparse, abort, Api, Resource


class clientRoutes(Resource):
    # http://127.0.0.1:5000/1
    def get(self, cif):
        print("client_routes.get")
        result = client_service.get(cif=cif)
        return jsonify(result)

    # http://127.0.0.1:5000/1
    def post(self, cif):
        print("client_routes.post")
        json_data = request.get_json(force=True)
        client = Client()
        client.CIF = json_data["CIF"]
        client.Name = json_data["Name"]
        client.LastName = json_data["LastName"]
        client.age = json_data["age"]
        client.Link = json_data["link"]
        result = client_service.post(client)
        return jsonify(result)
