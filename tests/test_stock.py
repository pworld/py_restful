import factory
from pytest_factoryboy import register

from myapi.models import Stock


@register
class StockFactory(factory.Factory):

    mean = factory.Sequence(lambda n: 'mean%d' % n)
    median = factory.Sequence(lambda n: 'median%d' % n)
    std = factory.Sequence(lambda n: 'std%d' % n)
    var = factory.Sequence(lambda n: 'var%d' % n)
    average = factory.Sequence(lambda n: 'average%d' % n)
    min = factory.Sequence(lambda n: 'min%d' % n)
    max = factory.Sequence(lambda n: 'max%d' % n)
    symbol = factory.Sequence(lambda n: 'symbol%d' % n)
    analyze = factory.Sequence(lambda n: 'analyze%d' % n)
    function = factory.Sequence(lambda n: 'function%d' % n)
    start_time = factory.Sequence(lambda n: 'start_time%d' % n)
    end_time = factory.Sequence(lambda n: 'end_time%d' % n)
    interval = factory.Sequence(lambda n: 'interval%d' % n)
    user_id = factory.Sequence(lambda n: 'user_id%d' % n)

    class Meta:
        model = Stock

def test_create_stock(client, db, admin_headers):
    # test bad data
    data = {
        "function":"TIME_SERIES_INTRADAY",
        "symbol":"MSFT",
        "interval":"15min",
        "analyze":"open"
    }

    rep = client.post(
        'app/time-series-save',
        json=data,
        headers=admin_headers
    )
    assert rep.status_code == 200

    data = rep.get_json()

    user = db.session.query(Stock).filter_by(user_id=data['user_id']).first()

    assert user.user_id == 'admin'

