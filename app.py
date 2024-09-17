from flask import Flask, request, send_file, jsonify, render_template
import os
from scraper import scrape_flipkart, scrape_amazon

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    data = request.json
    url = data.get('url')
    platform = data.get('platform')

    if not url or not platform:
        return jsonify({"error": "Missing URL or platform"}), 400

    try:
        if platform.lower() == 'flipkart':
            filename = scrape_flipkart(url)
        elif platform.lower() == 'amazon':
            filename = scrape_amazon(url)
        else:
            return jsonify({"error": "Unsupported platform"}), 400

        if not os.path.exists(filename):
            return jsonify({"error": "Failed to scrape reviews"}), 500

        return send_file(filename, as_attachment=True)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
