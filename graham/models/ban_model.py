import peewee

from enum import IntEnum

from genesis.db import BaseModel
from genesis.models.user_model import User

class BanType(IntEnum):
    STATS_BAN = 1
    FROZEN = 2
    TIP_BAN = 3

class Ban(BaseModel):
    user = peewee.ForeignKeyField(User, backref='bans')
    ban_type = peewee.IntegerField()
    created_at = peewee.DateTimeField()

    class Meta:
        db_table='user_bans'