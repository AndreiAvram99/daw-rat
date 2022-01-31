import main
from main import parse_text
import json
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/parse', methods=['POST'])
def parse():
    data = request.get_json()
    text = data["text"]
    print(text)
    noun, verb = main.parse_text(text)

    response = {
        "noun": noun,
        "verb": verb
    }

    return json.dumps(response)


if __name__ == '__main__':
    app.run(port=34567, debug=True)
