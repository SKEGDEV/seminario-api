from flask import Flask
from src.DB.database_init import mysql
from flask_cors import CORS
from os import getenv
from dotenv import load_dotenv
#blueprints
from src.routes.auth_route import auth
from src.routes.admin_routes import admin_route
from src.routes.client_routes import client_routes
from src.routes.loan_routes import loan_route
from src.routes.report_routes import report_route
from src.routes.payment_routes import payment_route

app = Flask(__name__)
CORS(app)

app.config['MYSQL_DATABASE_HOST'] = getenv("host")
app.config['MYSQL_DATABASE_USER'] = getenv("user")
app.config['MYSQL_DATABASE_PASSWORD'] = getenv("password")
app.config['MYSQL_DATABASE_DB'] = getenv("database")
mysql.init_app(app)

app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(admin_route, url_prefix='/admin')
app.register_blueprint(client_routes, url_prefix="/client")
app.register_blueprint(loan_route, url_prefix="/loan")
app.register_blueprint(report_route, url_prefix='/report')
app.register_blueprint(payment_route, url_prefix='/payment')


if __name__ == "__main__":
    load_dotenv()
    app.run(port=getenv('server_port'), host=getenv('server_host'), debug=True)



