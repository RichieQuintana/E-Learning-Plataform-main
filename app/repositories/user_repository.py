from models.user import User

class UserRepository:
    def find_by_email(self, email):
        return User.query.filter_by(email=email).first()
