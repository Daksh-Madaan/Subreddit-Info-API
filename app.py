from flask import Flask, render_template, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/info/<string:n>')
def main(n):
    try:
        url = 'https://www.reddit.com/r/'+n
        head = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip',
            'DNT': '1',
            'Connection': 'close'
        }

        r = requests.get(url, headers=head)
        soup = BeautifulSoup(r.text, 'html.parser')

        m = soup.find('div', class_='_3b9utyKN3e_kzVZ5ngPqAu').text
        c = soup.find('div', class_='_1sDtEhccxFpHDn2RUhxmSq').text
        a = soup.find('div', class_='_1zPvgKHteTOub9dKkvrOl4').text

        result = {
            "Valid": True,
            "Members": m,
            "Created": c,
            "About": a,
            "URL": url
        }

        return jsonify(result)

    except AttributeError:
        result = {
            "Valid": False,
        }
        return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
