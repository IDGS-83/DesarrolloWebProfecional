from repository.userRepository import UserRepository

class authService:

    @staticmethod
    def register(username, email, password):
        return UserRepository.create(username, email, password)

    @staticmethod
    def find_by_id(id):
        return UserRepository.find_by_id(id)
