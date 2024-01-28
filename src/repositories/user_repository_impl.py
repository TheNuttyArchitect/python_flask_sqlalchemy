from .user_repository import UserRepository
from src.models.user_model import UserModel
from src.services.user import User
from db import db


class UserRepositoryImpl(UserRepository):
    def find(self, id: int) -> User:
       return self.__get_model_by_id(id)


    def getAll(self) -> list[User]:
        return db.session.query(UserModel).all()


    def add(self, user: User) -> User:
        userModel = UserModel(user)

        db.session.add(userModel)
        db.session.commit()

        return userModel
    

    def update(self, user: User) -> User:
        userModel = self.__get_model_by_id(user.id)

        userModel.map_fields(user)

        # db.session.add(userModel)
        # db.session.flush()
        db.session.commit()
        
        return userModel
    

    def delete(self, id: int) -> None:
        userModel = self.__get_model_by_id(id)
        db.session.delete(userModel)
        db.session.commit()

        return None;

    def __get_model_by_id(self, id: int) -> UserModel:
        return db.session.query(UserModel).filter_by(id = id).first()