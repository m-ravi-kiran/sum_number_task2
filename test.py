import unittest

import requests


class ApiTest(unittest.TestCase):
    API = 'http://localhost:5000/sum'

    def test_sucesss(self):
        r = requests.put(ApiTest.API, json=[1, 2, 3])
        self.assertEqual(r.status_code, 200)
        self.assertDictEqual(r.json(), {'status': 200, 'result': 6})

        r = requests.put(ApiTest.API, json=[1, 2, 14])
        self.assertEqual(r.status_code, 200)
        self.assertDictEqual(r.json(), {'status': 200, 'result': 3})

    def test_fail(self):
        r = requests.put(ApiTest.API, json=[1, 2])
        self.assertEqual(r.status_code, 400)
        self.assertDictEqual(r.json(), {'status': 400, 'error': 'Exactly 3 numbers are required'})

        r = requests.put(ApiTest.API, json=[1, 2, 'a'])
        self.assertEqual(r.status_code, 400)
        self.assertDictEqual(r.json(), {'status': 400, 'error': 'All inputs must be numeric'})


if __name__ == '__main__':
    unittest.main()
