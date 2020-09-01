from flask import render_template, request

from app import app, db
from app.models import NetflixRecord

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/records")
def records_all():
  page = request.args.get('page', 1, type=int)
  records = NetflixRecord.query.order_by(NetflixRecord.show_id).paginate(page, 1, error_out=False)
  return render_template("records.html", title="Netflix Records", records=records)