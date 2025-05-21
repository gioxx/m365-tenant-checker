from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend requests

@app.route('/check', methods=['GET'])
def check_domain():
    domain = request.args.get('domain')
    if not domain:
        return jsonify({'error': 'Missing domain parameter'}), 400

    email = f'test@{domain}'
    url = f'https://autodiscover-s.outlook.com/autodiscover/autodiscover.json?Email={email}'

    try:
        resp = requests.get(url, timeout=5)
        if resp.status_code in [200, 401]:
            return jsonify({
                'domain': domain,
                'status': resp.status_code,
                'found': True,
                'message': 'The domain is likely associated with a Microsoft 365 tenant.'
            })
        elif resp.status_code == 404:
            return jsonify({
                'domain': domain,
                'status': resp.status_code,
                'found': False,
                'message': 'The domain is NOT associated with Microsoft 365.'
            })
        else:
            return jsonify({
                'domain': domain,
                'status': resp.status_code,
                'found': None,
                'message': f'Unexpected response code: {resp.status_code}'
            })
    except requests.RequestException as e:
        return jsonify({
            'error': str(e),
            'found': None,
            'message': 'Request to Microsoft Autodiscover failed.'
        }), 500
