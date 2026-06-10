from flask import Flask, jsonify
import psutil

app = Flask(__name__)

@app.route('/status')
def status():
    return jsonify({
        "cpu":    psutil.cpu_percent(),
        "ram":    psutil.virtual_memory().percent,
        "disk":   psutil.disk_usage('/').percent,
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)