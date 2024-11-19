from flask import Flask
from dotenv import load_dotenv
from utils.db import db,init_db
from views.Heladeria_controller import principal_routes
import os

load_dotenv(override=True)
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]= f"mysql+pymysql://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SECRET_KEY'] = 'secret'

db.init_app(app)#SQLAlchemy(app)
init_db(app)

principal_routes(app)

    
if __name__ == "__main__":
    app.run(debug=True)