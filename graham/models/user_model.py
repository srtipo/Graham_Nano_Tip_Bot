import peewee
from enum import IntEnum

from genesis.db import BaseModel

class User(BaseModel):
	id = peewee.BigIntegerField(primary_key=True)
	username = peewee.CharField(unique=True)
	created_at = peewee.DateTimeField()

	class Meta:
		db_table = 'users'

class UserRelationshipType(IntEnum):
    Favorites = 1
    Muted = 2

class UserRelationship(BaseModel):
    source_user = peewee.ForeignKeyField(User, backref='relationships')
    target_user = peewee.ForeignKeyField(User)
    relationship_type = peewee.IntegerField()
    created_at = peewee.DateTimeField()

    class Meta:
        db_table = 'user_relationships'