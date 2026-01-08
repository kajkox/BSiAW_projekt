from app import app, db
from flask import Flask
from flask_talisman import Talisman
import os

csp = {
    'default-src': '\'self\'',
    'img-src': ['\'self\'', 'data:'],
    'script-src': ['\'self\'', '\'unsafe-inline\'', 'https://cdn.jsdelivr.net', 'https://code.jquery.com', 'https://stackpath.bootstrapcdn.com'],
    'style-src': ['\'self\'', '\'unsafe-inline\'', 'https://cdn.jsdelivr.net', 'https://stackpath.bootstrapcdn.com', 'https://fonts.googleapis.com'],
    'object-src': '\'none\'',  
    'base-uri': '\'self\'',
    'font-src': ['\'self\'', 'https://fonts.gstatic.com', 'data:']
}

Talisman(app,
    content_security_policy=csp,
    force_https=False,
    session_cookie_secure=False,
    strict_transport_security=False,
    frame_options='DENY'
)

if __name__ == '__main__':
    with app.app_context():
        try:
            db.create_all()
        except Exception as e:
            print(f"Warning: Cannot connect to database: {e}", file=sys.stderr)

    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'

    app.run(host='0.0.0.0', port=5000, debug=debug_mode) # nosec B104
