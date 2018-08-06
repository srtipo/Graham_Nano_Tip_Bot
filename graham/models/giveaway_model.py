import peewee

from graham.db import BaseModel

from graham.models.user_model import User

class Giveaway(BaseModel):
	started_by = peewee.ForeignKeyField(User, backref='started_giveaways')
	giveway_amount = peewee.DecimalField(max_digits=20, decimal_places=6)
	tip_amount = peewee.DecimalField(max_digits=20, decimal_places=6)
	end_time = peewee.DateTimeField(null=True)
	channel_id = peewee.BigIntegerField() 
	winner = peewee.ForeignKeyField(User, backref='won_giveaways', null=True)
	entry_fee = peewee.DecimalField(max_digits=20, decimal_places=6)

    class Meta:
        db_table = 'giveaways'

class Entry(BaseModel):
	giveaway_id = peewee.ForeignKeyField(Giveaway, backref='entries')
	user = peewee.ForeignKeyField(User, backref='entered_giveaways')
	created_at = peewee.DateTimeField(default=datetime.datetime.utcnow())

    class Meta:
        db_table = 'giveaway_entries'