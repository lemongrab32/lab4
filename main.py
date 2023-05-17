from flask import Flask, render_template, request
from calc import calc
import unittest

app = Flask(__name__)


@app.route('/', methods=['post', 'get'])
def form():
    if request.method == 'POST':
        currency = request.form.get('list')
        value = request.form.get('value')
        desired = request.form.get('desired')
        print(value)
        return render_template('index.html', ans=calc(currency, value, desired))
    else:
        return render_template('index.html')


class TestConverter(unittest.TestCase):
    def test_values(self):
        self.assertEqual(calc("USD", 16, "RUB"), 1279.6768)
        self.assertEqual(calc("USD", 16.55, "RUB"), 1323.6657)
        self.assertEqual(calc("USD", -13, "RUB"), "ValueError")

    def test_types(self):
        self.assertEqual(calc("USD", "16", "RUB"), "TypeError")
        self.assertEqual(calc("USD", [1, 2, 3], "RUB"), "TypeError")
        self.assertEqual(calc("USD", (1, 2, 3), "RUB"), "TypeError")

if __name__ == "__main__":
    #app.run(debug=True)
    unittest.main()
