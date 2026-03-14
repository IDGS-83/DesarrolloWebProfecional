from repository.userRepository import UserRepository

class authService:

    @staticmethod
    def sync_user(cognito_sub, email):
        user = UserRepository.find_by_cognito_sub(cognito_sub)
        if not user:
            user = UserRepository.create(cognito_sub, email)
        return user

    @staticmethod
    def find_by_id(id):
        return UserRepository.find_by_id(id)

    @staticmethod
    def get_all():
        return UserRepository.get_all()
