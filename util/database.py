from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base
from util.common import LogData

class DatabaseConnector:
    engine = None
    session = None
    engine_backup = None
    session_backup = None

    @classmethod
    def configure(cls):
        cls.engine = create_engine("sqlite:///data/iskenderiye.db", echo=False)
        Session = sessionmaker(bind=cls.engine)
        cls.session = Session()

        cls.engine_backup = create_engine("sqlite:///data/iskenderiye_backup.db", echo=False)
        BackupSession = sessionmaker(bind=cls.engine_backup)
        cls.session_backup = BackupSession()

        Base.metadata.create_all(cls.engine)
        Base.metadata.create_all(cls.engine_backup)


    @classmethod
    def commit_changes(cls, logger):
        try:
            if not cls.session:
                raise ConnectionError("Database connection is not made yet!")

            cls.session.commit()
            cls.session_backup.commit()

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

