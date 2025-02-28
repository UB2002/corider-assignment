from flask import Flask
from app.config import Config
from app.Routes.User import user_bp
from pymongo import MongoClient

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
   
    
    # Test MongoDB connection on startup
    try:
        client = MongoClient(Config.MONGO_URI)
        # Try to ping the MongoDB server
        client.admin.command('ping')
        print("Connected to MongoDB successfully!")
    except Exception as e:
        print(f"MongoDB connection error: {e}")
    
    @app.route("/")
    def home():
        return {"message": "Welcome to the user management system"}
    
    # Register blueprints
    app.register_blueprint(user_bp)

    return app