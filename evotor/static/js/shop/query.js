function prepare_params(params) {
    var params2 = {}
    for (var key in params) {
        var o = params[key];
        if (typeof o == 'object') {
            params2[key] = JSON.stringify(params[key])
        } else {
            params2[key] = o
        }
    }

    return params2;
}

function query_html(model, template, params) {
    params.template = template;
    params = prepare_params(params)
    return $.get("/query/html/" + model + "/?" + $.param(params));
}

function query_json(model, params) {
    params = prepare_params(params)
    return $.get("/query/json/" + model + "/?" + $.param(params));
}
