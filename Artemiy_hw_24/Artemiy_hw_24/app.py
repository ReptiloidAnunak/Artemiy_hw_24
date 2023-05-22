import os
import json

from flask import Flask, request
from werkzeug.exceptions import BadRequest

from commands_mod import get_cmd1_result, get_cmd2_result
from userquery_class import UserQuery

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@app.route("/perform_query", methods=["POST"])
def perform_query():
    try:
        user_request_data = json.loads(request.data)
        user_query = UserQuery(user_request_data)
    except Exception as e:
        return f"Неправильный запрос: {e}"

    file_name_query = user_query.file_name
    file_query_path = os.path.join(DATA_DIR, file_name_query)

    if not os.path.exists(file_query_path):
        raise BadRequest

    # Command 1
    cmd1_res = get_cmd1_result(user_query, file_query_path)
    if user_query.cmd2 not in ["filter", "map", "unique", "sort", "limit"]:
        return cmd1_res

    # Command 2
    return get_cmd2_result(user_query, cmd1_res)


if __name__ == '__main__':
    app.run()


