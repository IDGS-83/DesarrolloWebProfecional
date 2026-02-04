from repository.userRepository import UserRepository

class AuthService:
    @staticmethod
    def register(username):
        return UserRepository.create(username)
