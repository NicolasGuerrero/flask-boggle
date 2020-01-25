from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):


    def test_valid_word(self):
        with app.test_client() as client:
            with client.session_transaction() as change_session:
                change_session['board_list'] = [["T", "Z", "Z", "Z", "Z"],
                                            ["E", "Z", "Z", "Z", "Z"],
                                            ["S", "Z", "Z", "Z", "Z"],
                                            ["T", "Z", "Z", "Z", "Z"],
                                            ["T", "Z", "Z", "Z", "Z"]]
        
        resp = client.post("/test-word", json={"word": 'TEST'})
        data = resp.get_json()["result"]

        self.assertEqual(data, "ok")


