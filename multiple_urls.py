from  flask import Flask
from  flask_swagger_ui import get_swaggerui_bluepxrint

app = Flask(__name__)


SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
API_URL = "https://petstore.swagger.io/v2/swagger.json"  # Our API url (can of course be a local resource)



#for once we run the file we can access this function by this user and the next function with AI
@app.route('/user')
def user_data():
    return 'this user having python knowledge'

@app.route('/AI/')
def status_ai():
    return 'this persone need to learn in depth AI concepts'


swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "Swagger Petstore"
    },
    # oauth_config={  # OAuth config. See https://github.com/swagger-api/swagger-ui#oauth2-configuration .
    #    'clientId': "your-client-id",
    #    'clientSecret': "your-client-secret-if-required",
    #    'realm': "your-realms",
    #    'appName': "your-app-name",
    #    'scopeSeparator': " ",
    #    'additionalQueryStringParams': {'test': "hello"}
    # }
)

app.register_blueprint(swaggerui_blueprint)


if __name__=='__main__':
    app.run(debug=True)