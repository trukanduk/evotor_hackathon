from django.http import JsonResponse
from django.shortcuts import render

from query_manager.utils import exec_query


def json_query_view(request, model_name):
    try:
        objs = exec_query(request, model_name)
        data = list(map(lambda obj: obj.public_dto(), objs))
        return JsonResponse({
            "result": "ok",
            "data": data,
        })
    except Exception as e:
        return JsonResponse({
            "result": "error",
            "content": str(e),
        })


def html_query_view(request, model_name):
    params = request.GET if request.method == "GET" else request.POST
    template_path = params["template"]
    objs = exec_query(request, model_name)
    
    return render(request, template_path, {"objs": objs})

