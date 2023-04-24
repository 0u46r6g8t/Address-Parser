from web.script_parser import Parser
from flask import Flask
from gevent.pywsgi import WSGIServer


## Define avariable for the app
app = Flask(__name__)
parser = Parser()

def return_json_message(isError, message, data=None):
    return {
        'isError': isError,
        'message': message,
        'data': data
    }

@app.route('/', methods=['GET'])
def main():
    return {
        'isError': True,
        'message': 'Use of route /validate/:name',
        'data': None
    }

@app.route('/validate/<nameOfActivity>', methods=['GET'])
def index(nameOfActivity):
    try:
        if nameOfActivity:
            data = parser.get_data(nameOfActivity)

            if data != 'Activity not found':
                return return_json_message(False, 'Activity found', data)

        return return_json_message(True, 'Activity not found')        

    except Exception as e: 
        return 'Activity not found'
        
if __name__ == '__main__':
    # app.run(debug=True)
    try:
        http_server = WSGIServer(('0.0.0.0', 3333), app)
        http_server.serve_forever()
    except Exception as e:
        print('Error', e)
    except KeyboardInterrupt:
        print("Tchau")