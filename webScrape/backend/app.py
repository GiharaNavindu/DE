from flask import Flask, request, jsonify
from flask_cors import CORS
from scraper.scraper import scrape_books

app = Flask(__name__)
CORS(app)  # This allows all origins. You can specify origins for better security.

@app.route('/scrape', methods=['POST'])
def scrape():
    data = request.get_json()
    url = data.get('url')
    if not url:
        return jsonify({"error": "URL is required"}), 400
   
    result = scrape_books(url)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
