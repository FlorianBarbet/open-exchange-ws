from flask import request, Blueprint, Response

from database import Rate, mysql_db

rate_bp = Blueprint('rates', __name__)


@rate_bp.route('/', methods=['GET'])
def get_all_rates():
    args = request.args
    index_start = args.get("next", type=int, default=0)
    limit = min(args.get("limit", type=int, default=15), 50)

    with mysql_db.atomic():
        result = Rate.select().order_by(Rate.name).limit(limit).offset(index_start).execute(database=mysql_db)
        return [rate.serialize() for rate in result]


@rate_bp.route('/<date>', methods=['GET'])
def get_specific_rate(date):
    with mysql_db.atomic():
        result = Rate.select().where(Rate.source == date).execute(database=mysql_db)
        return [rate.serialize() for rate in result]
