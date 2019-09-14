from flask_restful import Api

from . import init_app
from .controllers.agent_controller import Agent

# Init app and db
app = init_app()
app.app_context().push()

# Add resources and routes
api = Api(app)
api.add_resource(Agent, "/api/agent")