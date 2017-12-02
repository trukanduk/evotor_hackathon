function query_html(model, template, params) {
    params.template = template;
    return $.get("/query/html/" + model + "/?" + $.param(params));
}

function query_json(model, params) {
    return $.get("/query/json/" + model + "/?" + $.param(params));
}
