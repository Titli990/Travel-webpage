from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    # df = pd.read_csv('Dataset.csv')     //to load a dataset which is use in dropdown menu
    # place_names = df['Place_name'].dropna().unique().tolist()
    # print(place_names)  # Add this line to check if place_names is being populated
    # return render_template('index.html', place_names=place_names)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
