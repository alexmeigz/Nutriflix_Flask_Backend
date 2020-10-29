from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#Base Code Acquired from https://blog.theodo.com/2017/03/developping-a-flask-web-app-with-a-postresql-database-making-all-the-possible-errors/
class BaseModel(db.Model):
    '''Base data model for all objects'''
    __abstract__ = True

    def __init__(self, *args):
        super().__init__(*args)

    def __repr__(self):
        '''Define a base way to print models'''
        return '%s(%s)' % (self.__class__.__name__, {
            column: value
            for column, value in self._to_dict().items()
        })

    def json(self):
        '''Define a base way to jsonify models, dealing with datetime objects''' 
        return {
            column: value if not isinstance(value, datetime.date) else value.strftime('%Y-%m-%d')
            for column, value in self._to_dict().items()
        }
