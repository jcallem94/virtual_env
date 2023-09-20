from flask import Flask, request, jsonify, session
import random

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'  # Reemplaza 'tu_clave_secreta' con una clave secreta real y segura

frases = ["Elon Musk afirma que las redes sociales están diseñadas para mantenernos dentro de la plataforma, de modo que pasemos el mayor tiempo posible viendo contenidos.", 
          "Según un estudio realizado en 2018, más del 50% de las personas de entre 18 y 34 años se consideran dependientes de sus smartphones.", 
          "Las redes sociales tienen aspectos positivos y negativos, y debemos ser conscientes de ambos cuando utilicemos estas plataformas.", 
          "El estudio de la dependencia tecnológica es una de las áreas más relevantes de la investigación científica moderna."]

@app.route("/")
def hello_world():
    return """<h1>Hello, World! </h1>
    <a href="/frase_aleatoria">¡Ver un hecho al azar!</a>
    <a href="/adivinar_numero">¡Jugar al juego de adivinanza de números!</a>
    """

@app.route("/frase_aleatoria")
def frase():
    return f"<h1> {random.choice(frases)} </h1>"

@app.route("/adivinar_numero", methods=['GET', 'POST'])
def adivina_numero():
    if request.method == 'GET':
        # Mostrar el formulario para adivinar el número y guardar el número aleatorio en la sesión
        session['numero_aleatorio'] = random.randint(1, 10)
        return """
        <h1>Adivina el número</h1>
        <p>Estoy pensando en un número entre 1 y 10. ¡Adivina cuál es!</p>
        <form method="POST">
            <input type="number" name="guess" min="1" max="10" required>
            <input type="submit" value="Adivinar">
        </form>
        """
    elif request.method == 'POST':
        # Obtener el número aleatorio de la sesión
        answer = session.get('numero_aleatorio')
        guess = int(request.form['guess'])
        
        if guess == answer:
            result = "¡Correcto! ¡Has adivinado el número!"
        else:
            result = f"¡Oops! El número correcto era {answer}. Inténtalo de nuevo."

        return f"<h1>{result}</h1> <a href='/adivinar_numero'>Volver a jugar</a>"

if __name__ == "__main__":
    app.run(debug=True)

