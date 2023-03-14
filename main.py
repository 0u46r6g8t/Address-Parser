from web.script_parser import Parser
from flask import Flask

## Define avariable for the app
app = Flask(__name__)
parser = Parser()

def return_json_message(isError, message, data=None):
    return {
        'isError': isError,
        'message': message,
        'data': data
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
    app.run(debug=True)