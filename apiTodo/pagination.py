from rest_framework import pagination

class MyPageNumberPagination(pagination.PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size' # client tarafından sayfadaki ürün sayısının belirlenmesine aracılık eder 
    page_query_param = 'sayfa'
    max_page_size = 100

class LargePageNumberPagination(pagination.PageNumberPagination):
    page_size = 3



class MyLimitOffsetPagination(pagination.LimitOffsetPagination):
    default_limit = 1
    max_limit = 10
    limit_query_param = 'per_page' #default limit parametresi
    offset_query_param = 'page'

class MyCursorPagination(pagination.CursorPagination):
    page_size = 2
    ordering = '-createdDate'
    cursor_query_param = 'cursor'
    
