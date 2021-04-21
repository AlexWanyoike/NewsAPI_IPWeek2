import os

from app import create_app 
from flask_script import Manager,Shell,Server



# Creating app instance
config_name = os.environ.get('APPS_SETTINGS')
app = create_app(config_name)

manager = Manager(app)
manager.add_command('server',Server)
@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    manager.run()