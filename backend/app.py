import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import requests

# Use static path that works both in Docker and on Render
STATIC_FOLDER = os.path.join(os.path.dirname(__file__), '..', 'frontend')
STATIC_FOLDER = os.path.abspath(STATIC_FOLDER)

app = Flask(__name__, static_folder=STATIC_FOLDER, static_url_path='')
CORS(app)

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/check', methods=['GET'])
def check_domain():
    domain = request.args.get('domain')
    if not domain:
        return jsonify({'error': 'Missing domain parameter'}), 400

    email = f'test@{domain}'
    url = f'https://autodiscover-s.outlook.com/autodiscover/autodiscover.json?Email={email}&Protocol=Autodiscoverv1'

    try:
        resp = requests.get(url, timeout=5)

        if resp.status_code == 200:
            try:
                json_data = resp.json()
                if 'Url' in json_data:
                    return jsonify({
                        'domain': domain,
                        'status': 200,
                        'found': True,
                        'message': f"Domain is associated with Microsoft 365. Redirect URL: {json_data['Url']}"
                    })
                else:
                    return jsonify({
                        'domain': domain,
                        'status': 200,
                        'found': True,
                        'message': "Domain responded with 200 OK, but no redirect URL was provided."
                    })
            except Exception:
                return jsonify({
                    'domain': domain,
                    'status': 200,
                    'found': True,
                    'message': "Received 200 OK, but failed to parse JSON."
                })

        elif resp.status_code == 404:
            return jsonify({
                'domain': domain,
                'status': 404,
                'found': False,
                'message': "The domain is NOT associated with Microsoft 365."
            })

        elif resp.status_code == 400:
            try:
                error_data = resp.json()
                if error_data.get("ErrorCode") == "MissingProtocol":
                    return jsonify({
                        'domain': domain,
                        'status': 400,
                        'found': None,
                        'message': "Missing protocol parameter. This endpoint requires 'Protocol=Autodiscoverv1'."
                    })
                else:
                    return jsonify({
                        'domain': domain,
                        'status': 400,
                        'found': None,
                        'message': f"400 Bad Request: {error_data.get('ErrorMessage', 'Unknown error')}"
                    })
            except Exception:
                return jsonify({
                    'domain': domain,
                    'status': 400,
                    'found': None,
                    'message': "400 Bad Request received, and failed to parse error message."
                })

        else:
            return jsonify({
                'domain': domain,
                'status': resp.status_code,
                'found': None,
                'message': f"Unexpected response code: {resp.status_code}"
            })

    except requests.RequestException as e:
        return jsonify({
            'error': str(e),
            'found': None,
            'message': 'Request to Microsoft Autodiscover failed.'
        }), 500
