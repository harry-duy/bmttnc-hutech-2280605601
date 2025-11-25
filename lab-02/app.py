from flask import Flask, render_template, request
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayfairCipher
from cipher.transposition import TranspositionCipher

app = Flask(__name__)

# ===== HOME PAGE =====
@app.route('/')
def home():
    return render_template('index.html')

# ===== CAESAR CIPHER =====
@app.route('/caesar')
def caesar():
    return render_template('caesar.html')

@app.route('/encrypt', methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    Caesar = CaesarCipher()
    encrypted_text = Caesar.encrypt_text(text, key)
    return f"""
    <html>
    <head>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css" rel="stylesheet"/>
    </head>
    <body>
        <div class="container mt-5">
            <div class="alert alert-success">
                <h4>CAESAR ENCRYPTION RESULT</h4>
                <p><strong>Text:</strong> {text}</p>
                <p><strong>Key:</strong> {key}</p>
                <p><strong>Encrypted text:</strong> {encrypted_text}</p>
            </div>
            <a href="/caesar" class="btn btn-primary">← Quay lại</a>
        </div>
    </body>
    </html>
    """

@app.route('/decrypt', methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    Caesar = CaesarCipher()
    decrypted_text = Caesar.decrypt_text(text, key)
    return f"""
    <html>
    <head>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css" rel="stylesheet"/>
    </head>
    <body>
        <div class="container mt-5">
            <div class="alert alert-info">
                <h4>CAESAR DECRYPTION RESULT</h4>
                <p><strong>Text:</strong> {text}</p>
                <p><strong>Key:</strong> {key}</p>
                <p><strong>Decrypted text:</strong> {decrypted_text}</p>
            </div>
            <a href="/caesar" class="btn btn-primary">← Quay lại</a>
        </div>
    </body>
    </html>
    """

# ===== VIGENÈRE CIPHER =====
@app.route('/vigenere')
def vigenere():
    return render_template('vigenere.html')

@app.route('/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    Vigenere = VigenereCipher()
    encrypted_text = Vigenere.vigenere_encrypt(text, key)
    return f"""
    <html>
    <head>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css" rel="stylesheet"/>
    </head>
    <body>
        <div class="container mt-5">
            <div class="alert alert-success">
                <h4>VIGENÈRE ENCRYPTION RESULT</h4>
                <p><strong>Text:</strong> {text}</p>
                <p><strong>Key:</strong> {key}</p>
                <p><strong>Encrypted text:</strong> {encrypted_text}</p>
            </div>
            <a href="/vigenere" class="btn btn-primary">← Quay lại</a>
        </div>
    </body>
    </html>
    """

@app.route('/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    Vigenere = VigenereCipher()
    decrypted_text = Vigenere.vigenere_decrypt(text, key)
    return f"""
    <html>
    <head>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css" rel="stylesheet"/>
    </head>
    <body>
        <div class="container mt-5">
            <div class="alert alert-info">
                <h4>VIGENÈRE DECRYPTION RESULT</h4>
                <p><strong>Text:</strong> {text}</p>
                <p><strong>Key:</strong> {key}</p>
                <p><strong>Decrypted text:</strong> {decrypted_text}</p>
            </div>
            <a href="/vigenere" class="btn btn-primary">← Quay lại</a>
        </div>
    </body>
    </html>
    """

# ===== RAIL FENCE CIPHER =====
@app.route('/railfence')
def railfence():
    return render_template('railfence.html')

@app.route('/railfence/encrypt', methods=['POST'])
def railfence_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    Railfence = RailFenceCipher()
    encrypted_text = Railfence.rail_fence_encrypt(text, key)
    return f"""
    <html>
    <head>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css" rel="stylesheet"/>
    </head>
    <body>
        <div class="container mt-5">
            <div class="alert alert-success">
                <h4>RAIL FENCE ENCRYPTION RESULT</h4>
                <p><strong>Text:</strong> {text}</p>
                <p><strong>Rails:</strong> {key}</p>
                <p><strong>Encrypted text:</strong> {encrypted_text}</p>
            </div>
            <a href="/railfence" class="btn btn-primary">← Quay lại</a>
        </div>
    </body>
    </html>
    """

@app.route('/railfence/decrypt', methods=['POST'])
def railfence_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    Railfence = RailFenceCipher()
    decrypted_text = Railfence.rail_fence_decrypt(text, key)
    return f"""
    <html>
    <head>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css" rel="stylesheet"/>
    </head>
    <body>
        <div class="container mt-5">
            <div class="alert alert-info">
                <h4>RAIL FENCE DECRYPTION RESULT</h4>
                <p><strong>Text:</strong> {text}</p>
                <p><strong>Rails:</strong> {key}</p>
                <p><strong>Decrypted text:</strong> {decrypted_text}</p>
            </div>
            <a href="/railfence" class="btn btn-primary">← Quay lại</a>
        </div>
    </body>
    </html>
    """

# ===== PLAYFAIR CIPHER =====
@app.route('/playfair')
def playfair():
    return render_template('playfair.html')

@app.route('/playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    Playfair = PlayfairCipher()
    matrix = Playfair.create_playfair_matrix(key)
    encrypted_text = Playfair.playfair_encrypt(text, matrix)
    return f"""
    <html>
    <head>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css" rel="stylesheet"/>
    </head>
    <body>
        <div class="container mt-5">
            <div class="alert alert-success">
                <h4>PLAYFAIR ENCRYPTION RESULT</h4>
                <p><strong>Text:</strong> {text}</p>
                <p><strong>Key:</strong> {key}</p>
                <p><strong>Encrypted text:</strong> {encrypted_text}</p>
            </div>
            <a href="/playfair" class="btn btn-primary">← Quay lại</a>
        </div>
    </body>
    </html>
    """

@app.route('/playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    Playfair = PlayfairCipher()
    matrix = Playfair.create_playfair_matrix(key)
    decrypted_text = Playfair.playfair_decrypt(text, matrix)
    return f"""
    <html>
    <head>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css" rel="stylesheet"/>
    </head>
    <body>
        <div class="container mt-5">
            <div class="alert alert-info">
                <h4>PLAYFAIR DECRYPTION RESULT</h4>
                <p><strong>Text:</strong> {text}</p>
                <p><strong>Key:</strong> {key}</p>
                <p><strong>Decrypted text:</strong> {decrypted_text}</p>
            </div>
            <a href="/playfair" class="btn btn-primary">← Quay lại</a>
        </div>
    </body>
    </html>
    """

# ===== TRANSPOSITION CIPHER =====
@app.route('/transposition')
def transposition():
    return render_template('transposition.html')

@app.route('/transposition/encrypt', methods=['POST'])
def transposition_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    Transposition = TranspositionCipher()
    encrypted_text = Transposition.encrypt(text, key)
    return f"""
    <html>
    <head>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css" rel="stylesheet"/>
    </head>
    <body>
        <div class="container mt-5">
            <div class="alert alert-success">
                <h4>TRANSPOSITION ENCRYPTION RESULT</h4>
                <p><strong>Text:</strong> {text}</p>
                <p><strong>Key:</strong> {key}</p>
                <p><strong>Encrypted text:</strong> {encrypted_text}</p>
            </div>
            <a href="/transposition" class="btn btn-primary">← Quay lại</a>
        </div>
    </body>
    </html>
    """

@app.route('/transposition/decrypt', methods=['POST'])
def transposition_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    Transposition = TranspositionCipher()
    decrypted_text = Transposition.decrypt(text, key)
    return f"""
    <html>
    <head>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css" rel="stylesheet"/>
    </head>
    <body>
        <div class="container mt-5">
            <div class="alert alert-info">
                <h4>TRANSPOSITION DECRYPTION RESULT</h4>
                <p><strong>Text:</strong> {text}</p>
                <p><strong>Key:</strong> {key}</p>
                <p><strong>Decrypted text:</strong> {decrypted_text}</p>
            </div>
            <a href="/transposition" class="btn btn-primary">← Quay lại</a>
        </div>
    </body>
    </html>
    """

# Main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)