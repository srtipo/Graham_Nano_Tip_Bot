import peewee

from enum import IntEnum

from graham.db import BaseModel

class TransactionStatus(IntEnum):
	PENDING = 1
	PROCESSED = 2
	FAILED = 3

class TransactionType(IntEnum):
	TIP = 1
	WITHDRAW = 2
	GIVEAWAY_QUEUED = 3
	GIVEAWAY_ACTIVE = 4

class Transaction(BaseModel):
	id = peewee.UUIDField(primary_key=True)
	source_user = peewee.ForeignKeyField(User, backref='sent_transactions')
	amount = peewee.DecimalField(max_digits=20, decimal_places=6)
	target_user = peewee.ForeignKeyField(User, backref='received_transactions',null=True)
	destination = peewee.CharField(null=True) 
	transaction_type = peewee.IntegerField()
	block_hash = peewee.CharField(null=True)
	status = peewee.IntegerField()
	created_at = peewee.DateTimeField()

	class Meta:
		db_table='transactions'
