import json

from shop.models import (
    Product,
    ProductTag,
    Provider,
    Purchase,
)


_name2model = {
    "product": Product,
    "product_tag": ProductTag,
    "provider": Provider,
    "purchase": Purchase,
}


def exec_query(request, model_name):
    model = _name2model[model_name]
    params = request.GET if request.method == "GET" else request.POST

    filter = json.loads(params.get("filter", "{}"))
    order_by = json.loads(params.get("order_by", "[]"))

    query = (
        model.objects
            .filter(**filter)
            .order_by(*order_by)
    )

    limit_from = params.get("limit_from", None)
    limit_to = params.get("limit_to", None)

    if limit_from is not None or limit_to is not None:
        if limit_from is None:
            query = query[:int(limit_to)]
        elif limit_to is None:
            query = query[int(limit_from):]
        else:
            query = query[int(limit_from):int(limit_to)]

    objs = query.all()
    return objs
