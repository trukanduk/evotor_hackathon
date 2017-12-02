function query_html(model, template, params, callback) {
    params.template = template;
    $.get("/query/html/" + model + "/" + $.param(params), callback);
}

function query_json(model, params, callback) {
    $.get("/query/json/" + model + "/" + $.param(params), function(data) {
        callback(data.data);
    });
}
