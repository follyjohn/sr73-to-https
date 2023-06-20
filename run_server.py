# -*- coding: utf-8 -*-
"""

Created on May 2022
@author: Mr ABBAS-TURKI

"""

from flask import Flask
import ssl


# définir le message secret
SECRET_MESSAGE = "monmotsecret" # A modifier
app = Flask(__name__)


@app.route("/")
def get_secret_message():
    return SECRET_MESSAGE


if __name__ == "__main__":
    # HTTP version
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile="server-public-key.pem", keyfile="server-private-key.pem", password="passwordsrv")
    app.run(debug=False, host="0.0.0.0", port=8081, ssl_context=context)
    # HTTPS version
    # A compléter  : nécessité de déplacer les bons fichiers vers ce répertoire
