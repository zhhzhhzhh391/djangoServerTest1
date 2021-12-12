from rest_framework.pagination import PageNumberPagination

class LargerResultsSetPagination(PageNumberPagination):
    page_size = 2 #默认每页显示多少条数据  默认 主要是由前端决定
    max_page_size = 5 #前端控制的每页条数上限
    page_query_param = 'page'#前端查第一页、就传page=1
    page_size_query_param = 'page_size'
