from dotenv import load_dotenv
import os


class Config:
    database_url = None
    database_path = None
    database_name = None
    backup_name = None
    token_path = None
    client_secret = None
    credentials = None

    @classmethod
    def set_info(cls):
        load_dotenv(dotenv_path="info.env")

        cls.database_url = os.getenv("DATABASE_URL")
        cls.database_path = os.getenv("DATABASE_PATH")
        cls.database_name = os.getenv("DATABASE_NAME")
        cls.backup_name = os.getenv("BACKUP_NAME")
        cls.token_path = os.getenv("TOKEN_PATH")
        cls.client_secret = os.getenv("CLIENT_SECRET")
        cls.credentials = os.getenv("CREDENTIALS")
        cls.backup_reference = os.getenv("FILE_ID")
        
    def save_file_id(file_id: str, key: str = "FILE_ID", env_file: str = "info.env"):
        lines = []
        if os.path.exists(env_file):
            with open(env_file, "r") as f:
                lines = f.readlines()

        lines = [line for line in lines if not line.startswith(f"{key}=")]
        lines.append(f"\n{key}={file_id}\n")

        with open(env_file, "w") as f:
            f.writelines(lines)
