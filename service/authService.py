from repository.userRepository import UserRepository

class authService:
    @staticmethod
    def register(username, email, password):
        user = UserRepository.create(username, email, password)
        return user