from datetime import datetime

from core import open_exchange_singleton
from database import Rate, mysql_db


def job():
    today = datetime.today().strftime('%Y-%m-%d')
    print("Scheduled job started - {}.json".format(today), flush=True)
    # call open-exchange
    rates_of_day = open_exchange_singleton.get_rates_of_day(today)['rates']
    # mapping data to store
    data = [(today, name, float(rates_of_day[name])) for name in rates_of_day]
    # open the transaction
    with (mysql_db.atomic()):
        # we want to prevent re-insertion
        query = Rate.insert_many(data, fields=[Rate.source, Rate.name, Rate.val]).on_conflict_ignore()
        query.as_rowcount().returning().execute(database=mysql_db)
    print("Scheduled job terminated - {}.json".format(today))
    return rates_of_day
