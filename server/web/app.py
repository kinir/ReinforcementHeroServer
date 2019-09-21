from flask_restful import Api

from . import init_app
from .controllers.submission_controller import Submission
from .controllers.game_controller import Game
from .controllers.test_controller import Test

# Init app and db
app = init_app()
app.app_context().push()

# Add resources and routes
api = Api(app)
api.add_resource(Game, "/api/game", "/api/game/<game_id>")
api.add_resource(Submission, "/api/submit", "/api/submit/<game_id>")

# Test resource
api.add_resource(Test, "/api/test")
