from flask import Flask, request, make_response
import json

app = Flask(__name__)

index_add_counter = 0

@app.route('/')
def main():
    return "hhh"



@app.route('/client', methods=['GET', 'POST'])
def client():
    if request.method == 'POST':
        content = request.json

        print(content)

    if request.method == 'GET':
        pass

    return ''


if __name__ == '__main__':


    app.run(debug=True)