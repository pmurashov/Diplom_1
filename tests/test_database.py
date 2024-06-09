from database import Database

class TestDatabase:
    def test_check_available_buns(self):
        database = Database()
        assert len(database.available_buns()) == 3


    def test_check_available_ingredients(self):
        database = Database()
        assert len(database.available_ingredients()) == 6