from repository.userRepository import UserRepository

class authService:
    @staticmethod
    def register(username):
        user = UserRepository.create(username)
        return user