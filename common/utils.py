# -*- coding: utf-8 -*-
# @Time    : 2023/8/1 13:50
# @Author  : wwz18078
# @File    : utils.py
# @Software: PyCharm

from rest_framework.response import Response


class APIResponse(Response):
    def __init__(self, result=True, message="success", data=None, http_status=None, headers=None, exception=False,
                 **kwargs):
        response_data = {"result": result, "message": message, "data": data}
        response_data.update(**kwargs)
        super().__init__(data=response_data, status=http_status, headers=headers, exception=exception)
