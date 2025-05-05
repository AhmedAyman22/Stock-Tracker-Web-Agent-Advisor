from flask import Flask, render_template, jsonify, url_for ,request
import subprocess
import json
import os
import sys
api_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'api'))
sys.path.append(api_dir)
from stock_performance_fetcher import performanceFetcher

#print(performanceFetcher(['TSLA']))


app = Flask('Stock Advisor')

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/data")
def get_data():
    try:
        # Construct the absolute path to data.json
        app_dir = os.path.dirname(os.path.abspath(__file__)) # Get the directory of app.py
        data_path = os.path.join(app_dir, '..', 'data', 'data.json')
        with open(data_path, 'r') as f:
            data = json.load(f)
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({}) # Return empty if no data yet

@app.route("/refresh", methods=['POST'])
def refresh_data():
    try:
        scraper_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../scraper', 'scraper.py')
        subprocess.run(['python', scraper_path], check=True)
        app_dir = os.path.dirname(os.path.abspath(__file__)) # Get the directory of app.py
        data_path = os.path.join(app_dir, '..', 'data', 'data.json')
        with open(data_path, 'r') as f:
            data = json.load(f)
        return jsonify(data)
    except subprocess.CalledProcessError as e:
        print(f"Error running scraper: {e}")
        return jsonify({"error": "Failed to refresh data"}), 500
    except FileNotFoundError:
        return jsonify({})
  
  
@app.route("/submit", methods=['GET'])
def submit_tickers():
    print('\n\n\nsubmit_tickers\n\n\n')
    tickers = request.args['selectedCompaniesList']
    print(tickers)

if __name__ == '__main__':
    app.run(debug=True)