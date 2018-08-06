import settings
from playhouse.pool  import PooledPostgresqlExtDatabase

db = PooledPostgresqlExtDatabase(settings.database, user=settings.database_user, password=settings.database_password, host='localhost', port=5432, max_connections=16)

# Base Model
class BaseModel(Model):
	class Meta:
		database = db

# TODO Initialize database somewhere