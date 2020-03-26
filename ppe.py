from app.extensions import db
from app.models import User, Mask
from app import create_app


## Flask app
server = create_app()


@server.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Mask': Mask}