from app import app
from flask_sqlalchemy import SQLAlchemy

#database+driver://username:password@ipaddress:port/database
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root:root@127.0.0.1:3306/notes"
db = SQLAlchemy(app)