
from userquery_class import UserQuery
from utils import filter_query, map_query, limit_query, sort_query, unique_query
from utils import apply_regex


def get_cmd1_result(user_query: UserQuery, file: str) -> str:
    """Получает запрос пользователя и открытый файл, возвращает результат выполнения команды №1
    в зависимости от типа запроса"""
    with open(file) as f:
        if user_query.cmd1 == "filter":
            return "\n".join([x for x in (filter_query(user_query.value1, f))])

        elif user_query.cmd1 == "map":
            value1 = int(user_query.value1)
            return "\n".join([x for x in (map_query(value1, f))])

        elif user_query.cmd1 == "limit":
            return "\n".join([x for x in limit_query(file, user_query.value1)])

        elif user_query.cmd1 == "regex":
            return "\n".join([x for x in apply_regex(user_query.value1, f)])


def get_cmd2_result(user_query: UserQuery, cmd1_res: str) -> str:
    """Получает запрос пользователя и результат команды №1, возвращает результат выполнения команды №2
    в зависимости от типа запроса"""
    # Filter2
    if user_query.cmd2 == "filter":
        if user_query.cmd1 in ["filter", "limit"]:
            cmd1_res_slt = cmd1_res.split("\n")[::2]

        elif user_query.cmd1 == "map":
            cmd1_res_slt = cmd1_res.split("\n")
            return "\n".join([x for x in (filter_query(user_query.value2, cmd1_res_slt))])


    # Limit2
    elif user_query.cmd2 == "limit":
        limit = int(user_query.value2)
        if user_query.cmd1 == "filter":
            cmd1_res_slt = cmd1_res.split("\n")[::2]

        elif user_query.cmd1 == "map":
            cmd1_res_slt = cmd1_res.split("\n")
        result = cmd1_res_slt[:limit]
        return "\n".join(result)


    # Map2
    elif user_query.cmd2 == "map":
        value2 = int(user_query.value2)
        cmd1_res_slt = cmd1_res.split("\n")[::2]
        map_iter = map_query(value2, cmd1_res_slt)
        return "\n".join([x for x in map_iter])

    # Unique2
    elif user_query.cmd2 == "unique":
        if user_query.cmd1 == "map":
            data_column = cmd1_res.split("\n")
            return "\n".join([x for x in unique_query(data_column)])

    # Sort2
    elif user_query.cmd2 == "sort":
        if user_query.cmd1 in ["filter", "limit", "regex"]:
            cmd1_res_slt = cmd1_res.split("\n")[::2]
            return "\n".join([x for x in sort_query(cmd1_res_slt, user_query.value2)])

        elif user_query.cmd1 == "map":
            data_column = cmd1_res.split("\n")
            return "\n".join([x for x in sort_query(data_column, user_query.value2)])
