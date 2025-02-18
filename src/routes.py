from flask import Blueprint, request, jsonify
from models import User, Profile, Task

api = Blueprint("api", __name__)

@api.route('/status', methods=['GET', 'POST', 'PUT', 'DELETE'])
def get_status():
    return jsonify({ "status": "success" }), 200


@api.route('/profile/<int:id>', methods=['GET'])
def get_profile(id):

    user = User.query.get(id)

    if not user:
        return jsonify({ "msg": "User not found!"}), 404
    
    return jsonify(user.serialize()), 200


@api.route('/user/<int:id>/tasks/add', methods=['GET'])
def add_task(id):

    user = User.query.get(id)
    if not user:
        return jsonify({ "msg": "User not found!"}), 404
    
    query = request.args
    if not 'label' in query:
        return jsonify({ "msg": "Label is required!"}), 400
    
    task = Task()
    task.label = query['label']
    task.done = False
    #task.users_id = id
    #task.save()

    user.tasks.append(task)
    user.update()

    return jsonify({ "status": "success", "message": "Task added!" }), 200


@api.route('/profile/<int:id>', methods=['PUT'])
def actualizar_perfil(id):
    
    user = User.query.get(id)
    if not user:
        return jsonify({ "msg": "User not found!"}), 404

    datos_a_actualizar = request.get_json()

    user.profile.biography = datos_a_actualizar['biography'] if 'biography' in datos_a_actualizar else user.profile.biography
    user.update()

    return jsonify({ "status": "success", "message": "Profile updated!" }), 200