from flask import render_template, request

from app import app, db
from app.models import NetflixRecord

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/records")
def records_all():
  page = request.args.get('page', 1, type=int)
  records = NetflixRecord.query.order_by(NetflixRecord.show_id).paginate(page, 3, error_out=False)
  return render_template("all_records.html", title="Netflix Records", records=records)

@app.route("/record/<record>")
def record(record):
  record = NetflixRecord.query.filter_by(show_id=record).first()
  title = ""
  if record:
    title = record.title
  return render_template("record.html", title=title, record=record)