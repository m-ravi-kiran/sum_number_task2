import json

import flask
from flask import request

from api_response import ApiResponse
from app import Sum
from errors import ApiException

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/sum', methods=['PUT'])
def get_sum():
    try:
        data = json.loads(request.data)
        sm = Sum(3)
        sm.validate(*data)
        result = sm.sum_numbers(*data)
        return ApiResponse.get_success_response(result)
    except ApiException as e:
        return ApiResponse.get_error_response(e.message, e.status_code)
    except Exception as e:
        import traceback
        print(traceback.format_exc())
        return ApiResponse.get_error_response()


app.run(host='0.0.0.0')
