from src.config.db import engine, SQLModel
from src.entities.models.tracking_model import *

# create the database and tables
SQLModel.metadata.create_all(engine)


