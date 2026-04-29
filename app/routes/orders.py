from flask import Blueprint, jsonify, request
from app.controllers.service_controller import (
    listar_ordens,
    criar_ordem
)

orders_bp = Blueprint("orders", __name__)

@orders_bp.route("", methods=["GET"])
def get_orders():
    response, status = listar_ordens()
    return jsonify(response), status

@orders_bp.route("", methods=["POST"])
def post_order():
    data = request.get_json()
    response, status = criar_ordem(data)
    return jsonify(response), status
