class AuthService:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def login(self, email, password):
        user = self.user_repository.find_by_email(email)
        if not user or not user.check_password(password):
            raise Exception("Invalid credentials")
        return self.generate_token(user)

    def generate_token(self, user):
        # Lógica para generar un token (e.g., JWT)
        return f"token-for-{user.email}"
