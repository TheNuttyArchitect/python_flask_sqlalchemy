from dependency_injector import containers, providers
from ..repositories.user_repository_impl import UserRepositoryImpl
from ..services.user_service import UserService


class DI(containers.DeclarativeContainer):
    userRepository = providers.Factory(UserRepositoryImpl)
    userService = providers.Factory(UserService, user_repository = userRepository)