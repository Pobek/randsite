from app import app, db
from app.models import NetflixRecord

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8080)