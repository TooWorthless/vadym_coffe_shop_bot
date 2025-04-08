from core.abstractions import DatabaseAdapter

class FeedbackService:
    def __init__(self, db: DatabaseAdapter):
        self.db = db

    def save_feedback(self, user_id: int, text: str):
        self.db.add_feedback(user_id, text)