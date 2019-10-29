from flask import jsonify

def handle_exception(e):
    print(f"ERROR - { str(e) }")
    return jsonify(error=str(e)), 500