from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
import os

class GoogleDriveUploader:
    def __init__(self):
        self.gauth = GoogleAuth()

        # Use the client_secrets.json for first login
        self.gauth.LoadClientConfigFile("client_secrets.json")

        # Try to load saved credentials
        self.gauth.LoadCredentialsFile("credentials.json")

        if self.gauth.credentials is None:
            self.gauth.LocalWebserverAuth()  # first time, will open browser
        elif self.gauth.access_token_expired:
            self.gauth.Refresh()
        else:
            self.gauth.Authorize()

        # Save for next time
        self.gauth.SaveCredentialsFile("credentials.json")

        self.drive = GoogleDrive(self.gauth)

    def upload_file(self, filepath: str, folder_id: str = None):
        """
        Uploads a file to Google Drive. If folder_id is provided, uploads into that folder.
        """
        filename = os.path.basename(filepath)

        file_metadata = {"name": filename}
        if folder_id:
            file_metadata["parents"] = [folder_id]

        gfile = self.drive.CreateFile(file_metadata)
        gfile.SetContentFile(filepath)
        gfile.Upload()

        return gfile["id"]
