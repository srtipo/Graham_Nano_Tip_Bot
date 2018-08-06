import peewee

from graham.db import BaseModel

class Account(BaseModel):
	user = peewee.ForeignKeyField(User, backref='account',primary_key=True)
	address = peewee.CharField(unique=True)
	pending_receive = peewee.DecimalField(default=0)
	pending_send = peewee.DecimalField(default=0)
	created_at = peewee.DateTimeField()

    class Meta:
        db_table = 'accounts'