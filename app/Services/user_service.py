from pymongo import MongoClient
from app.config import Config
from app.Model.user import User
from bson import ObjectId

class UserService:
    def __init__(self):
        self.client = MongoClient(Config.MONGO_URI)
        self.db = self.client['corider-DB']
        self.collection = self.db.users

    def create_user(self, user_data: dict) -> str:
        user = User(**user_data)
        result = self.collection.insert_one(user.dict())
        return str(result.inserted_id)

    def get_all_users(self) -> list:
        users = list(self.collection.find())
        return [User(**user).dict() for user in users]

    def get_user(self, user_id: str) -> dict:
        user = self.collection.find_one({"_id": ObjectId(user_id)})
        return User(**user).dict() if user else None

    def update_user(self, user_id: str, user_data: dict) -> bool:
        result = self.collection.update_one(
            {"_id": ObjectId(user_id)},
            {"$set": user_data}
        )
        return result.modified_count > 0

    def delete_user(self, user_id: str) -> bool:
        result = self.collection.delete_one({"_id": ObjectId(user_id)})
        return result.deleted_count > 0