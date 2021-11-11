from conduit.database import (db, Model)


class Tags(Model):
    __tablename__ = 'my_tags'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))

    def __init__(self, title):
        db.Model.__init__(self, title=title)


class Tag_Relation(Model):
    __tablename__ = 'tag_relation'

    entity = db.Column(db.String(100))
    eid = db.Column(db.Integer)
    tid = db.Column(db.Integer)

    def __init__(self, entity, eid, tid):
        db.Model.__init__(self, entity=entity, eid=eid, tid=tid)
