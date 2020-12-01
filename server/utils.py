import numpy as np
import json
import pickle


class HousePricePredictor:
    LOCATIONS = None
    DATA_COLS = None
    MODEL = None

    def load_resources(self):
        print('< Loading saved resources ... >')
        with open('D:\\3_Study\\1_Python\\house_price_prediction\\server\\resources\\columns.json', 'r') as f:
            self.DATA_COLS = json.load(f)['data_cols']
            self.LOCATIONS = self.DATA_COLS[4:]

        with open('D:\\3_Study\\1_Python\\house_price_prediction\\server\\resources\\banglore_house_price_model.pickle', 'rb') as f:
            self.MODEL = pickle.load(f)
        print('< Loading completed ... >')

    def get_location_names(self):
        return self.LOCATIONS

    def get_estimated_price(self, location, sqft, bath, balcony, bhk):
        try:
            location_idx = self.DATA_COLS.index(location.lower())
        except:
            location_idx = -1

        x = np.zeros(len(self.DATA_COLS))
        x[0] = sqft
        x[1] = bath
        x[2] = balcony
        x[3] = bhk
        if location_idx >= 0:
            x[location_idx] = 1

        return self.MODEL.predict([x])[0]


if __name__ == '__main__':
    predictor = HousePricePredictor()
    predictor.load_resources()
    print(predictor.get_location_names())
    print(predictor.get_estimated_price('1st Phase JP Nagar', 1000, 2, 1, 2))
    print(predictor.get_estimated_price('1st Phase JP Nagar', 1000, 3, 2, 3))
    print(predictor.get_estimated_price('Panvel', 1000, 2, 1, 2))
