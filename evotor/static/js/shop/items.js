function request_items(model, template, filters) {
    $("#items-container").html('');
    $("#items-loading-img").show();
    $("#items-container-loading-error").hide();
    return query_html(model, template, filters)
            .done(function(html) { $("#items-container").html(html); })
            .fail(function(data) {
                $("#item-container-loading-error-desc").html(data.content || "Неизвестная ошибка");
                $("#items-container-loading-error").show();
            })
            .always(function() { $("#items-loading-img").hide(); });
}
