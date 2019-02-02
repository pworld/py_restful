from myapi.extensions import db, pwd_context


class Stock(db.Model):
    """Basic user model
    """
    __tablename__ = "stock"
    id = db.Column(db.Integer, primary_key=True)
    mean = db.Column(db.Float, nullable=True)
    median = db.Column(db.Float, nullable=True)
    std = db.Column(db.Float, nullable=True)
    var = db.Column(db.Float, nullable=True)
    average = db.Column(db.Float, nullable=True)
    min = db.Column(db.Float, nullable=True)
    max = db.Column(db.Float, nullable=True)
    symbol = db.Column(db.String(25), nullable=False)
    analyze = db.Column(db.String(25), nullable=False)
    function = db.Column(db.String(25), nullable=False)
    start_time = db.Column(db.String(25), nullable=False)
    end_time = db.Column(db.String(25), nullable=False)
    interval = db.Column(db.String(25), nullable=False)
    user_id = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return "<Stock %s>" % self.id
