import logging

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World'

@app.route('/error')
def error_route():
    """Génère une exception pour tester le gestionnaire d'erreurs."""
    raise Exception("Test Error")

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500
    # app.logger.error(f"Erreur 500: {e}")  # Ajoute un log pour capturer l'erreur
    # return """
    # Une erreur interne est survenue : <pre>{}</pre>
    # Consultez les logs pour plus d'informations.
    # """.format(e), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
