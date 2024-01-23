from ..services.user import User

class UserRepository:
    def find(self, id:int) -> User:
        raise NotImplementedError
    
    
    def getAll(self) -> list[User]:
        raise NotImplementedError
    

    def add(self, user: User) -> User:
        raise NotImplementedError
    

    def update(self, user: User) -> User:
        raise NotImplementedError
    

    def delete(self, id: int) -> None:
        raise NotImplementedError