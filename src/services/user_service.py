from src.repositories.user_repository import UserRepository
from src.services.user import User


class UserService:
    _user_repository: UserRepository

    def __init__(self, user_repository: UserRepository) -> None:
        self._user_repository = user_repository


    def get_user(self, id: int) -> dict: 
        user: User = self._user_repository.find(id)

        if user:
            return user.to_dict
        
        return None
    

    def create(self, user: User) -> dict:
        user = self._user_repository.add(user)

        return user.to_dict()
    

    def update(self, user: User) -> dict:
        user = self._user_repository.update(user)
        return user.to_dict()


    def getAll(self) -> list:
        results = []

        users = self._user_repository.getAll()

        if users:
            for u in users:
                results.append(u.to_dict())
        
        return results
    

    def delete(self, id: int) -> None:
        return self._user_repository.delete(id)