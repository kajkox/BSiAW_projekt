from app import app, db
from flask import Flask
from flask_talisman import Talisman

csp = {
    'default-src': '\'self\'',
    'img-src': '*',
    'script-src': ['\'self\'', '\'unsafe-inline\'', 'https://*'],
    'style-src': ['\'self\'', '\'unsafe-inline\'', 'https://*'],
}

Talisman(app,
    content_security_policy=csp,
    force_https=False,
    session_cookie_secure=False,
    strict_transport_security=False
)

if __name__ == '__main__':
    # Tworzenie tabel w bazie danych przy starcie, jeśli nie istnieją
    with app.app_context():
        db.create_all()

    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    # Uruchomienie serwera (host 0.0.0.0 jest wymagany dla Dockera)
    app.run(host='0.0.0.0', port=5000, debug=debug_mode) # nosec B104
