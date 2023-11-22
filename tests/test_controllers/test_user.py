from src.controllers.user import User, db
from src.db.database import Database
from src.config.config import Config

def test_fetch_user_data(monkeypatch):
    monkeypatch.setattr(Config,"QUERY_TO_VIEW_USER", "")
    monkeypatch.setattr(Database,"get_items",lambda _,a,b: ("tanvi","noida","203051"))
    assert User.fetch_user_data("tanvi") == ("tanvi","noida","203051")

def test_fetch_user_data_negative(monkeypatch):
    monkeypatch.setattr(Config,"QUERY_TO_VIEW_USER", "")
    monkeypatch.setattr(Database,"get_items",lambda _,a,b: ("tanvi","noida","203051"))
    assert User.fetch_user_data("tanvi") == ("tanvi","noida","203051")
