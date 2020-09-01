from app import db

class NetflixRecord(db.Model):
  __tablename__ = 'netflix_records'

  show_id = db.Column(db.Integer, primary_key=True)
  type = db.Column(db.String)
  title = db.Column(db.String)
  director = db.Column(db.ARRAY(db.String))
  cast = db.Column(db.ARRAY(db.String))
  country = db.Column(db.ARRAY(db.String))
  date_added = db.Column(db.String)
  release_year = db.Column(db.Integer)
  rating = db.Column(db.String)
  duration = db.Column(db.String)
  listed_in = db.Column(db.ARRAY(db.String))
  description = db.Column(db.String)