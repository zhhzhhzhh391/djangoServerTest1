import six
from rest_framework.response import Response
from rest_framework.serializers import Serializer

class JsonResponse(Response):
    def __init__(self, code=10000, msg="Success", data="", status=None,
                 template_name=None, headers=None,
                 exception=False, content_type=None):
        super(JsonResponse,self).__init__(data, status, template_name, headers, exception, content_type)
        self.data = {"code":code,"msg":msg,"data":data}

