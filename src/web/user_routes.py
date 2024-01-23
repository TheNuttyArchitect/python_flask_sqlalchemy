from flask import Blueprint, jsonify, request
from dependency_injector.wiring import inject, Provide
from src.di.di_container import DI
from src.services.user_service import UserService, User


api = Blueprint('user_api', __name__)


@api.route('/', methods=('GET',))
def get_all(user_service: UserService = Provide[DI.userService]):
    users = user_service.getAll();

    return jsonify(users), 200