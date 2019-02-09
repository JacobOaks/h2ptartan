from app import db
from app.search import *

class SearchableMixin(object):
    @classmethod
    def search(cls, expression, page, per_page):
        ids, total = query_index(cls.__tablename__, expression, page, per_page)
        if total == 0:
            return cls.query.filter_by(id=0), 0
        when = []
        for i in range(len(ids)):
            when.append((ids[i], i))
        return cls.query.filter(cls.id.in_(ids)),order_by(
            db.case(when, value=cls.id)), total

    @classmethod
    def before_commit(cls, session):
        session._changes = {
            'add': list(session.new),
            'update': list(session.dirty),
            'delete': list(session.deleted)
        }

    @classmethod
    def after_commit(cls, session):
        for obj in session._changes['add']:
            if isinstance(obj, SearchableMixin):
                add_to_index(obj.__tablename__, obj)
        for obj in session._changes['update']:
            if isinstance(obj, SearchableMixin):
                add_to_index(obj.__tablename__, obj)
        for obj in session._changes['delete']:
            if isinstance(obj, SearchableMixin):
                remove_from_index(obj.__tablename__, obj)
        session._changes =  None

    @classmethod
    def reindex(cls):
        for obj in cls.query:
            add_to_index(cls.__tablename__, obj)

db.event.listen(db.session, 'before_commit', SearchableMixin.before_commit)
db.event.listen(db.session, 'after_commit', SearchableMixin.after_commit)

class Car(SearchableMixin, db.Model):
    __searchable__ = ['make', 'model', ]
    id = db.Column(db.Integer, primary_key=True) #unique id
    cMake = db.Column(db.String(128), index=True) #make
    cModel = db.Column(db.String(128), index=True, unique=True) #model
    cYear = db.Column(db.Integer, index=True) #year
    fCost = db.Column(db.Integer, index=True) #cost per year
    fType = db.Column(db.String(32), index=True) #either regular, premium, or diesel
    hMpg = db.Column(db.Integer, index=True) #highway hMpg
    cMpg = db.Column(db.Integer, index=True) #city hMPG
    comboMpg = db.Column(db.Integer, index=True) #combined
    transType = db.Column(db.String(32), index=True) #how many gears and manual/automatic
    coTwo = db.Column(db.Float, index=True) #in grams per mile
    saveSpend = db.Column(db.Integer, index=True) #fuel cost over five years averaged against the normal car

    def __repr__(self):
        return '<Car {} {}>'.format(self.cMake, self.cModel)

    def to_dict(self):
        data = {
            'id': self.id,
            'cMake': self.cMake,
            'cModel': self.cModel,
            'cYear': self.cYear,
            'fCost': self.fCost,
            'fType': self.fType,
            'hMpg': self.hMpg,
            'cMpg': self.cMpg,
            'comboMpg': self.comboMpg,
            'transType': self.transType,
            'coTwo': self.coTwo,
            'saveSpend': self.saveSpend
        }
        return data

    def from_dict(self, data, new_car=False):
        for field in ['cMake', 'cModel']:
            if field in data:
                setattr(self, field, data[field])
