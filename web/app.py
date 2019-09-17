from flask_restful import Api

from . import init_app
from .controllers.submission_controller import Submission

# Init app and db
app = init_app()
app.app_context().push()

# Add resources and routes
api = Api(app)
api.add_resource(Submission, "/api/submit")
