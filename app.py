from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
# POSTGRESQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///messages_db'
# SQLITE
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


class Message(db.Model):
      id = db.Column(db.Integer, primary_key=True)
      user = db.Column(db.String(50), nullable=True)
      content = db.Column(db.String(500), nullable=True)
      created_at = db.Column(db.DateTime, default= datetime.utcnow)
      
      def __repr__(self):
          return '<Message %r>' % self.id
      
message = Message(user='John', content='Hello World!')

if __name__ == '__main__':
	with app.app_context():
		db.create_all()
		db.session.add(message)
		db.session.commit()
		app.run()