import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base
from util.common import LogData
from .gauth import GoogleDriveUploader
from .config import Config

class DatabaseConnector:
    engine = None
    session = None

    @classmethod
    def configure(cls):
        cls.engine = create_engine(Config.database_url, echo=False)
        Session = sessionmaker(bind=cls.engine)
        cls.session = Session()

        Base.metadata.create_all(cls.engine)

    @classmethod
    def commit_changes(cls, logger):
        try:
            if not cls.session:
                raise ConnectionError("Database connection is not made yet!")

            cls.session.commit()

            logger.log(LogData(
                message="Changes added successfully to both DBs.",
                source="controller",
                level="info"
            ))

        except Exception as e:
            cls.session.rollback()
            cls.session_backup.rollback()
            logger.log(LogData(
                message=f"Error occurred: {e}",
                source="controller",
                level="error"
            ))

    @classmethod
    def upload_backup(cls, logger):
        try:
            uploader = GoogleDriveUploader()
            folder_id = None

            src = sqlite3.connect(f"{Config.database_path}/{Config.database_name}")
            dst = sqlite3.connect(f"{Config.database_path}/{Config.backup_name}") 

            with dst:
                src.backup(dst) 

            file_id = uploader.upload_file(f"{Config.database_path}/{Config.backup_name}", folder_id=folder_id)
            Config.save_file_id(file_id)
            logger.log(LogData(
                message="Backup uploaded successfully to Google Drive. File ID: {id}",
                source="controller",
                level="info",
                kwargs={"id": file_id}
            ))

        except Exception as e:
            logger.log(LogData(
                message="Google Drive upload failed: {}",
                source="controller",
                level="error",
                args=(e, )
            ))