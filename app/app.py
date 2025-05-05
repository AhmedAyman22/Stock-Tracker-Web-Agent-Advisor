from flask import Flask, render_template, jsonify, url_for, request
import subprocess
import json
import time
import os
import sys
api_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'api'))
agent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'agent'))
sys.path.append(api_dir)
sys.path.append(agent_dir)
from stock_performance_fetcher import performanceFetcher
from agent import generateReport

app = Flask('Stock Advisor')

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/data")
def get_data():
    try:
        app_dir = os.path.dirname(os.path.abspath(__file__))
        data_path = os.path.join(app_dir, '..', 'data', 'data.json')
        with open(data_path, 'r') as f:
            data = json.load(f)
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({})

@app.route("/refresh", methods=['POST'])
def refresh_data():
    try:
        scraper_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../scraper', 'scraper.py')
        subprocess.run(['python', scraper_path], check=True)
        app_dir = os.path.dirname(os.path.abspath(__file__))
        data_path = os.path.join(app_dir, '..', 'data', 'data.json')
        with open(data_path, 'r') as f:
            data = json.load(f)
        return jsonify(data)
    except subprocess.CalledProcessError as e:
        print(f"Error running scraper: {e}")
        return jsonify({"error": "Failed to refresh data"}), 500
    except FileNotFoundError:
        return jsonify({})


@app.route("/submit", methods=['POST'])
def submit_tickers():
    #try:
    #agent_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../agent', 'agent.py')
    #subprocess.run(['python', agent_path], check=True)
    data = request.get_json()
    print('sending data to agent...')
    generateReport(data)
    print('generating report...')
    app_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(app_dir, '..', 'data', 'agent_report.json')
    with open(data_path, 'r') as f:
        data = json.load(f)
    f.close()
    print('sending report...')
    return jsonify(data['report'])

    #except subprocess.CalledProcessError as e:
        #print(f"Error running agent: {e}")
        #return jsonify({"error": "Failed to connect to AI"}), 500
    #except FileNotFoundError:
        #return jsonify({})

if __name__ == '__main__':
    app.run(debug=True)

