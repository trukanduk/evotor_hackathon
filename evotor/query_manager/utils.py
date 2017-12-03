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


class QueryParams:
    def __init__(self, filter=None, order_by=None, limit_from=None, limit_to=None, new_data=None):
        self.filter = filter if filter is not None else {}
        self.order_by = order_by if order_by is not None else {}
        self.limit_from = limit_from
        self.limit_to = limit_to
        self.new_data = new_data if new_data is not None else {}

    @staticmethod
    def parse(request):
        raw = request.GET if request.method == "GET" else request.POST
        limit_from = raw.get("limit_from", None)
        if limit_from is not None:
            limit_from = int(limit_from)
        limit_to = raw.get("limit_to", None)
        if limit_to is not None:
            limit_to = int(limit_to)
        return QueryParams(
            filter=json.loads(raw.get("filter", "{}")),
            order_by=json.loads(raw.get("order_by", "[]")),
            limit_from=limit_from,
            limit_to=limit_to,
            new_data=json.loads(raw.get("new_data", "{}")),
        )


def get_model(model_name):
    return _name2model[model_name]

def exec_query(request, model_name):
    return exec_query_raw(QueryParams.parse(request), get_model(model_name))
    

def exec_query_raw(params, model):
    objs = get_query(params, model).all()
    return objs

    
def get_query(params, model):
    query = (
        model.objects
            .filter(**params.filter)
            .order_by(*params.order_by)
    )

    if params.limit_from is not None or params.limit_to is not None:
        if params.limit_from is None:
            query = query[:params.limit_to]
        elif limit_to is None:
            query = query[params.limit_from:]
        else:
            query = query[params.limit_from:params.limit_to]

    return query
