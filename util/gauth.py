from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
import os

from .config import Config

class GoogleDriveUploader:
    def __init__(self):
        self.gauth = GoogleAuth()

        self.gauth.LoadClientConfigFile(f"{Config.token_path}/{Config.client_secret}")
        self.gauth.LoadCredentialsFile(f"{Config.token_path}/{Config.credentials}")

        if self.gauth.credentials is None:
            self.gauth.LocalWebserverAuth() 
        elif self.gauth.access_token_expired:
            self.gauth.Refresh()
        else:
            self.gauth.Authorize()

        self.gauth.SaveCredentialsFile(f"{Config.token_path}/{Config.credentials}")

        self.drive = GoogleDrive(self.gauth)

    def upload_file(self, filepath: str, folder_id: str = None):
        """
        Uploads a file to Google Drive. If folder_id is provided, uploads into that folder.
        """
        filename = os.path.basename(filepath)

        if Config.backup_reference:
            gfile = self.drive.CreateFile({'id': Config.backup_reference})
        else:
            file_metadata = {"name": filename}
            if folder_id:
                file_metadata["parents"] = [folder_id]
            gfile = self.drive.CreateFile(file_metadata)

        gfile.SetContentFile(filepath)
        gfile.Upload()

        return gfile["id"]
