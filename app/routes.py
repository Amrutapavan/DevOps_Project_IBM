from flask import jsonify, request, abort
from . import app

accounts_db = {}

@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Welcome to the Account Service!"}), 200

@app.route("/accounts", methods=["POST"])
def create_account():
    from .models import Account  # Deferred import to avoid circular import
    if not request.json or 'name' not in request.json or 'email' not in request.json:
        abort(400)
    account_id = len(accounts_db) + 1
    account = Account(
        id=account_id,
        name=request.json['name'],
        email=request.json['email'],
        address=request.json.get('address', ""),
        phone_number=request.json.get('phone_number', "")
    )
    accounts_db[account_id] = account
    return jsonify(account.serialize()), 201

@app.route("/accounts", methods=["GET"])
def get_all_accounts():
    from .models import Account  # Deferred import to avoid circular import
    return jsonify([account.serialize() for account in accounts_db.values()]), 200

@app.route("/accounts/<int:account_id>", methods=["GET"])
def get_account(account_id):
    from .models import Account  # Deferred import to avoid circular import
    account = accounts_db.get(account_id)
    if account is None:
        abort(404)
    return jsonify(account.serialize()), 200

@app.route("/accounts/<int:account_id>", methods=["PUT"])
def update_account(account_id):
    from .models import Account  # Deferred import to avoid circular import
    if not request.json:
        abort(400)
    account = accounts_db.get(account_id)
    if account is None:
        abort(404)
    account.name = request.json.get('name', account.name)
    account.email = request.json.get('email', account.email)
    account.address = request.json.get('address', account.address)
    account.phone_number = request.json.get('phone_number', account.phone_number)
    return jsonify(account.serialize()), 200

@app.route("/accounts/<int:account_id>", methods=["DELETE"])
def delete_account(account_id):
    from .models import Account  # Deferred import to avoid circular import
    account = accounts_db.pop(account_id, None)
    if account is None:
        abort(404)
    return '', 204
