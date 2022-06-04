########################################################
# IMPORTS
########################################################
from flask import Flask, render_template

########################################################
# FUNCTIONS
########################################################


def create_app(test_config=None):

    app = Flask(__name__)

    @app.route('/')
    def home():
        return render_template('index.html')

    return app


app = create_app()
if __name__ == '__main__':
    app.run(debug=True)
