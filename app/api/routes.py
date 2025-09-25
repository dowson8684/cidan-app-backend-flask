from app.api import bp

@bp.route('/ping', methods=['GET'])
def ping():
    return {"message": "pong"}