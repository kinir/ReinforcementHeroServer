from flask_restful import Api

from . import init_app
from .controllers.submission_controller import Submission
from .controllers.game_controller import Game, Games
from .controllers.environment_controller import Environment, Environments
from .controllers.test_controller import Test

# Init app and db
app = init_app()
app.app_context().push()

# Add resources and routes
api = Api(app)
api.add_resource(Games, "/api/game", endpoint="games")
api.add_resource(Game, "/api/game", "/api/game/<game_id>", endpoint="game")
api.add_resource(Submission, "/api/submit", "/api/submit/<student_id>")
api.add_resource(Environments, "/api/env", endpoint="environments")
api.add_resource(Environment, "/api/env", endpoint="environment")

# Test resource
api.add_resource(Test, "/api/test/<id>")

# Raise flask exception instead of flask-restful exception
def raise_exception(sender, exception, **extra):
    raise exception

from flask_restful import got_request_exception
got_request_exception.connect(raise_exception, app)
