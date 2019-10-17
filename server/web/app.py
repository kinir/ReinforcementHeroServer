from flask_restful import Api

from . import init_app
from .controllers.submission_controller import Submission
from .controllers.game_controller import Game, Games
from .controllers.environment_controller import Environment
from .controllers.test_controller import Test

# Init app and db
app = init_app()
app.app_context().push()

# Add resources and routes
api = Api(app)
api.add_resource(Games, "/api/game", endpoint="games")
api.add_resource(Game, "/api/game", "/api/game/<game_id>", endpoint="game")
api.add_resource(Submission, "/api/submit", "/api/submit/<student_id>")
api.add_resource(Environment, "/api/env")

# Test resource
api.add_resource(Test, "/api/test")
