from abc import ABC, abstractmethod

class AuthStrategy(ABC):
    @abstractmethod
    def authenticate(self, email, password):
        pass

class BasicAuthStrategy(AuthStrategy):
    def authenticate(self, email, password):
        # Lógica para autenticación básica
        pass

class OAuthStrategy(AuthStrategy):
    def authenticate(self, token):
        # Lógica para autenticación OAuth
        pass
