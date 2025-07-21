from flask import request, jsonify
from app import app
from app.db import cursor, conn
from flask_jwt_extended import create_access_token
# from werkzeug.security import check_password_hash  # Not needed now

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    
    cursor.execute("SELECT id, password_hash, role FROM users WHERE email = %s", (data['email'],))
    user = cursor.fetchone()

    # 🔓 Plain password check
    if user and user[1] == data['password']:
        access_token = create_access_token(identity={"id": user[0], "role": user[2]})
        return jsonify(access_token=access_token), 200

    return jsonify(msg='Invalid credentials'), 401
