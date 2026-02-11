from repository.userRepository import UserRepository

class authService:
    @staticmethod
    def register(username, email, password):
        user = UserRepository.create(username, email, password)
        return user

    @staticmethod
    def get_user_by_id(user_id):
        return UserRepository.get_by_id(user_id)