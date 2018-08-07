import datetime
import peewee
from enum import IntEnum

from genesis.db import BaseModel

class User(BaseModel):
	id = peewee.BigIntegerField(primary_key=True)
	username = peewee.CharField(unique=True)
	created_at = peewee.DateTimeField()

	class Meta:
		db_table = 'users'

    @classmethod
    def exists(self, user_id):
        return self.select().where(id == user_id).count() > 0

    @classmethod
    def create(self, user_id, username):
        if self.exists():
            return None
        user = User(id=user_id, username=username, created_at=datetime.datetime.utcnow())
        if user.save() > 0:
            return user
        return None

    @classmethod
    # To find user by id
    def get_user_by_id(id):
	try:
               user = User.get(id==id)
                return user
        except User.DoesNotExist:
                return None
	
    @classmethod
    # To find user by name
    def get_user_by_name(user_name):
        try:
            user = User.get(user_name=user_name)
            return user
        except User.DoesNotExist:
            return None

    @classmethod
     # To find user by name wallet address
    def get_user_by_wallet_address(address):
        try:
            user = User.select().join(Account).where(Account.wallet_address == address)
            return user
    except User.DoesNotExist:
        return None

    @classmethod
    # To find wallet address by user
    def get_address(user_id):
        query=Account.select().join(User).where(User.id == user_id)
        for account in query:
            address=account.wallet_address
            return address

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
