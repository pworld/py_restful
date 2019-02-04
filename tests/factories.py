from myapi.models import User
from myapi.models import Stock


def user_factory(i):
    return User(
        username="user{}".format(i),
        email="user{}@mail.com".format(i)
    )

def stock_factory(i):

    return Stock(
        mean="mean{}".format(i),
        median="median{}".format(i),
        std="std{}".format(i),
        var="var{}".format(i),
        average="average{}".format(i),
        min="min{}".format(i),
        max="max{}".format(i),
        symbol="symbol{}".format(i),
        analyze="analyze{}".format(i),
        function="function{}".format(i),
        start_time="start_time{}".format(i),
        end_time="end_time{}".format(i),
        interval="interval{}".format(i),
        user_id="user_id{}".format(i),
    )
