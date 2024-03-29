from flask import Blueprint, request, jsonify

profilebp = Blueprint('profile', __name__)


profiles = []

@profilebp.route('/profiles', methods=['POST'])
def create_profile():
    data = request.json
    
    username = data.get('username')
    email = data.get('email')
    
    if not username or not email:
        return jsonify({"error": "Username and email are required"}), 400
    
    profile = {"id": len(profiles) + 1, "username": username, "email": email}
    profiles.append(profile)
    
    return jsonify({"message": "Profile created successfully", "profile": profile}), 201

@profilebp.route('/profiles/<int:profile_id>', methods=['PUT'])
def update_profile(profile_id):
    data = request.json
    
    new_username = data.get('username')
    new_email = data.get('email')
    
    profile = next((p for p in profiles if p['id'] == profile_id), None)
    
    if not profile:
        return jsonify({"error": "Profile not found"}), 404
    
    if new_username:
        profile['username'] = new_username
    if new_email:
        profile['email'] = new_email
        
    return jsonify({"message": f"Profile {profile_id} updated successfully", "profile": profile}), 200

@profilebp.route('/profiles/<int:profile_id>', methods=['GET'])
def get_profile(profile_id):
    profile = next((p for p in profiles if p['id'] == profile_id), None)
    
    if not profile:
       return jsonify({"error": "Profile not found"}), 404
   
    return jsonify({"profile": profile}), 200

@profilebp.route('/profiles/<int:profile_id>', methods=['DELETE'])
def delete_profile(profile_id):
    profile = next((p for p in profiles if p['id'] == profile_id), None)
    
    if not profile:
        return jsonify({"error": "Profile not found"}), 404
    
    profiles.remove(profile)
    
    return jsonify({"message": f"Profile {profile_id} deleted successfuly"}), 200
