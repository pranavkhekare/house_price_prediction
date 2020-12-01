from flask import Flask, request, jsonify
import utils

app = Flask(__name__)
predictor = utils.HousePricePredictor()


@app.route('/hello')
def hello():
    return 'Hi'


@app.route('/get_locations', methods=['GET'])
def get_locations():
    response = jsonify({'locations' : predictor.get_location_names()})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/get_prediction', methods=['POST'])
def get_prediction():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bath = int(request.form['bath'])
    balcony = int(request.form['balcony'])
    bhk = float(request.form['bhk'])

    response = jsonify({
        'estimated_price': predictor.get_estimated_price(location, total_sqft, bath, balcony, bhk)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    print('< Starting python flask server for price prediction ... >')
    predictor.load_resources()
    app.run()
