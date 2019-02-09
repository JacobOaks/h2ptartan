from app import db, search

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(120), index=True)
    model = db.Column(db.String(120), index=True, unique=True)

    def __repr__(self):
        return '<Car {} {}>'.format(self.make, self.model)

class SearchableMixin(object):
    @classmethod
    def search(cls, expression, page, per_page):
        ids, total = query_index(cls.__tablename__, expression, page, per_page)
        if total == 0:
            return cls.query.filter_by(id=0), 0
        when = []
        for i in range(len(ids)):
            when.append((ids[i], i))
        return cls.query.filter(cls.id.in)
