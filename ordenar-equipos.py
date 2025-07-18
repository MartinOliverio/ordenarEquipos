from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Tus equipos
equipos = ["Catalogo", "Compras", "Contabilidad", "Growth", "Informes", "Integraciones", "POS", "Stock", "Ventas"]

@app.route('/orden-presentacion', methods=['POST'])
def orden_presentacion():
    shuffled = equipos[:]
    random.shuffle(shuffled)
    mensaje = "*🎤 Orden aleatorio de presentación:* \n"
    mensaje += "\n".join(f"{i+1}. {e}" for i, e in enumerate(shuffled))
    return jsonify({
        "response_type": "in_channel",  # Para que lo vea todo el canal
        "text": mensaje
    })

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000)