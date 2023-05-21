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
        return render_template('index.html', ans=calc(currency, value, desired))
    else:
        return render_template('index.html')


class TestConverter(unittest.TestCase):
    def test_values(self):
        self.assertEqual(calc("USD", 16, "RUB"), "The answer is 1278.5488")
        self.assertEqual(calc("USD", 16.55, "RUB"), "The answer is 1322.4989")
        self.assertEqual(calc("USD", -13, "RUB"), "ValueError: (-13.0) меньше нуля")

    def test_types(self):
        self.assertEqual(calc("USD", "шестнадцать", "RUB"), 'ValueError: "шестнадцать" - не является числом')
        self.assertEqual(calc("USD", [1, 2, 3], "RUB"), 'TypeError: недопустимое значение')
        self.assertEqual(calc("USD", (1, 2, 3), "RUB"), 'TypeError: недопустимое значение')


if __name__ == "__main__":
    app.run(debug=True)
unittest.main()
