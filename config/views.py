import json
from typing import Union, Type

from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from reports.views import ViewInterface


@method_decorator(csrf_exempt, name='dispatch')
class ViewWrapper(View):
    view_creator_func: Type[ViewInterface] = None  # parameter is class (not instance)

    def get(self, request, *args, **kwargs) -> HttpResponse:
        kwargs.update(request.GET.dict())
        body, status = self.view_creator_func(request, **kwargs).get(**kwargs)
        return HttpResponse(json.dumps(body), status=status, content_type='application/json')

    def post(self, request, *args, **kwargs) -> HttpResponse:
        kwargs.update(json.loads(request.body))
        body, status = self.view_creator_func(request, **kwargs).post(**kwargs)
        return HttpResponse(json.dumps(body), status=status, content_type='application/json')
