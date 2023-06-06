import pytest
from flask_testing import TestCase
from werkzeug.datastructures import FileStorage
from base64 import b64encode
import os
from main import app, files_dict

class AppTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_upload(self):
        tester = app.test_client(self)
        response = tester.get('/upload', headers={'Authorization': 'Basic ' + b64encode(b"adm:psw").decode()}, content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_files(self):
        tester = app.test_client(self)
        response = tester.get('/files', headers={'Authorization': 'Basic ' + b64encode(b"adm:psw").decode()}, content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_file_data(self):
        tester = app.test_client(self)
        response = tester.get('/file', headers={'Authorization': 'Basic ' + b64encode(b"adm:psw").decode()}, content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_file_upload(self):
        tester = app.test_client(self)
        with open('C:/PABCWork.NET/Python/CAR.csv', 'rb') as f:
            response = tester.post(
                '/upload',
                data={'file': (FileStorage(stream=f, filename='CAR.csv'), 'file')},
                headers={'Authorization': 'Basic ' + b64encode(b"adm:psw").decode()},
                content_type='multipart/form-data'
            )
        self.assertEqual(response.status_code, 302)
        self.assertIn('CAR.csv', files_dict)


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_app.py"])
