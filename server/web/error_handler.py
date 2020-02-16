from flask import jsonify
import traceback

def handle_exception(e):
    print(f"ERROR - { str(e) }")
    print(repr(traceback.format_stack()))
    
    return jsonify(error=str(e)), 500