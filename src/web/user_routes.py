from flask import Blueprint, jsonify, request
from dependency_injector.wiring import inject, Provide
from src.di.di_container import DI
from src.services.user_service import UserService, User


api = Blueprint('user_api', __name__)


@api.route('/', methods=('GET',))
@inject
def get_all(user_service: UserService = Provide[DI.userService]):
    users = user_service.getAll();

    return jsonify(users), 200


@api.route('/<id>', methods=('GET',))
@inject
def get(id:str, user_service: UserService = Provide[DI.userService]):
    userDetails: dict = user_service.get_user(int(id))

    if not(userDetails):
        return jsonify({"message": f"Can't find requested user id: {id}"}), 404
    
    return jsonify(userDetails), 200


@api.route('/', methods=('POST',))
@inject
def create(user: User, user_service: UserService = Provide[DI.userService]):
    try:
        createdUser: dict = user_service.create(user)

        if not(createdUser):
            return jsonify({"message": "Could not successfully create user"}), 500
        
        return jsonify(createdUser), 201
    except Exception as e:
        return jsonify({"message": "Failed to create user", "details": e}), 500
    

@api.route('/', methods=('PUT',))
@inject
def put(user: User, user_service: UserService = Provide[DI.userService]):
    try:
        updatedUser: dict = user_service.update(user)

        if not(updatedUser):
            return jsonify({"message": "Could not successfully update user"}), 500
        
        return jsonify(updatedUser), 200
    except Exception as e:
        return jsonify({"message": "Failed to update user", "details": e}), 500


@api.route('/<id>', methods=('DELETE',))
@inject
def delete(id: str, user_service: UserService = Provide[DI.userService]):
    try:
        user_service.delete(int(id))

        return jsonify({"message": f"Successfully deleted user id: {id}"}), 200
    except Exception as e:
        return jsonify({"message": f"Failed to delete user id: {id}", "details": e}), 500