function request_items(model, template, filters, callback) {
    let low_callback = function(data) {
        console.log(data)
        $("#items-container").html(data);
    }
    query_html(model, template, filters, low_callback);
}
