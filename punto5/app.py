from flask import Flask, jsonify 

app = Flask(__name__)

@app.route("/<int:valor>")
def par_impar(valor):
    if(valor%2==0):
        return jsonify({
            "mensaje": "El numero es par"
        })
    else:
        return jsonify({
            "mensaje": "El numero es impar"
        })

app.run(host="0.0.0.0", port=5000)