from peewee import *

mysql_db = MySQLDatabase("open_exchange",
                         user="rate_service",
                         password="toto",
                         host="localhost",
                         autoconnect=True,
                         )


class Rate(Model):
    id = AutoField(primary_key=True)
    source = DateField(null=False)
    name = TextField(null=False)
    val = DecimalField(10, 5, null=False)

    class Meta:
        database = mysql_db
        indexes = (
            (('source', 'name'), True),
        )

    def serialize(self):
        return {
            'date': self.source.strftime('%Y-%m-%d'),
            'name': self.name,
            'value': self.val
        }


Rate.create_table()
