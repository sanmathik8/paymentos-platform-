from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy", "service": "payment-service"})

@app.route('/pay', methods=['POST'])
def pay():
    data = request.get_json()
    return jsonify({
        "status": "success",
        "transaction_id": "TXN123456",
        "amount": data.get("amount"),
        "currency": data.get("currency", "INR")
    })

@app.route('/status/<transaction_id>', methods=['GET'])
def status(transaction_id):
    return jsonify({
        "transaction_id": transaction_id,
        "status": "completed"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
