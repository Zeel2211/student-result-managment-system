from flask import request, jsonify
from app import app
from app.db import cursor, conn
from flask_jwt_extended import jwt_required, get_jwt_identity

@app.route('/api/results', methods=['GET'])
@jwt_required()
def get_results():
    user = get_jwt_identity()
    if user['role'] == 'teacher':
        cursor.execute("SELECT * FROM results")
    else:
        cursor.execute("SELECT * FROM results WHERE student_id = %s", (user['id'],))
    results = cursor.fetchall()
    return jsonify([{
        'id': r[0],
        'student_id': r[1],
        'subject': r[2],
        'marks': r[3],
        'grade': r[4]
    } for r in results])

@app.route('/api/results', methods=['POST'])
@jwt_required()
def add_result():
    user = get_jwt_identity()
    if user['role'] != 'teacher':
        return jsonify({'msg': 'Unauthorized'}), 403
    data = request.get_json()
    cursor.execute("INSERT INTO results (student_id, subject, marks, grade) VALUES (%s, %s, %s, %s)",
                   (data['student_id'], data['subject'], data['marks'], data['grade']))
    conn.commit()
    return jsonify({'msg': 'Result added'}), 201

@app.route('/api/results/<int:id>', methods=['PUT'])
@jwt_required()
def update_result(id):
    user = get_jwt_identity()
    if user['role'] != 'teacher':
        return jsonify({'msg': 'Unauthorized'}), 403
    data = request.get_json()
    cursor.execute("UPDATE results SET subject=%s, marks=%s, grade=%s WHERE id=%s",
                   (data['subject'], data['marks'], data['grade'], id))
    conn.commit()
    return jsonify({'msg': 'Result updated'})

@app.route('/api/results/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_result(id):
    user = get_jwt_identity()
    if user['role'] != 'teacher':
        return jsonify({'msg': 'Unauthorized'}), 403
    cursor.execute("DELETE FROM results WHERE id = %s", (id,))
    conn.commit()
    return jsonify({'msg': 'Result deleted'})

