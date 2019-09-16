from flask_restful import Api

from . import init_app
from .controllers.submission_controller import Submission
#from .models.submission_model import Submission

# Init app and db
app = init_app()
app.app_context().push()

# Add resources and routes
api = Api(app)
api.add_resource(Submission, "/api/submit")
#sub = Submission(1, [1, 2, 3], "blabla")
#print(sub)
