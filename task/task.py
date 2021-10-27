from conduit.database import db, Model
from datetime import datetime


class Task(Model):
    __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60), nullable=False)
    body: db.Column(db.Text, nullable=False)
    is_done: db.Column(db.Boolean, default=False)
    is_deleted: db.Column(db.Boolean, default=False)
    created_at: db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at: db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, title: str = 'Заголовок', body: str = ''):
        db.Model.__init__(self, title=title, body=body)
