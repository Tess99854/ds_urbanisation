import os


class CredentialManager:
    credential_manager = None

    def __init__(self):

        # MySQL Credentials
        self.DB_HOST = 'localhost'
        self.DB_USER = 'root'
        self.DB_PASS = 'password'
        self.DB_NAME = 'employees_db'
        self.DB_PORT = 3308

    @staticmethod
    def get_credential_manager():
        if not CredentialManager.credential_manager:
            CredentialManager.credential_manager = CredentialManager()
        return CredentialManager.credential_manager
