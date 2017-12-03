from django.http import JsonResponse
from django.shortcuts import render

from query_manager.utils import (
    exec_query,
    QueryParams,
    get_model,
    get_query,
)


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


def json_update_query_view(request, model_name):
    params = QueryParams.parse(request)
    model = get_model(model_name)
    query = get_query(params, model)

    query.update(**params.new_data)

    return JsonResponse({"result": "ok"})


def json_insert_query_view(request, model_name):
    params = QueryParams.parse(request)
    model = get_model(model_name)
    
    obj = model.objects.create(**params.new_data)
    
    return JsonResponse({
        "result": "ok",
        "data": obj.public_dto(),
    })
