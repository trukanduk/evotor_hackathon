function request_items(model, template, filters) {
    $("#items-container").html('');
    $("#items-loading-img").show();
    $("#items-container-loading-error").hide();
    return query_html(model, template, filters)
            .done(function(html) {
                console.log("done")
                $("#items-container").html(html);
                update_items_icons();
            })
            .fail(function(data) {
                console.log("fail")
                $("#item-container-loading-error-desc").html(data.content || "Неизвестная ошибка");
                $("#items-container-loading-error").show();
            })
            .always(function() {
                console.log("always")
                $("#items-loading-img").hide();
            });
}

function update_items_icons() {
    $(".sort-items-pair").removeClass('active');
    $(".sort-icon-desc").show();
    $(".sort-icon-asc").hide();

    if (itemsOrderByInfo.length == 0) {
        return;
    }

    let orderInfo = itemsOrderByInfo[0];
    let order = 'asc';
    let column = orderInfo
    if (orderInfo.substring(0, 1) == "-") {
        order = 'desc';
        column = orderInfo.substring(1);
    }

    $(".item-header-" + column + " .sort-icon").hide();
    $(".item-header-" + column + " .sort-icon-" + order).show();
    $(".item-header-" + column + " .sort-items-pair").addClass('active');
}

$(function() {
    if (!itemsModelName) {
        return;
    }

    $(".sort-icon").click(function() {
        let order = ($(this).attr('order') == 'asc' ? '-' : '');
        let column = $(this).attr('column');

        let template = (typeof itemsTemplate === 'undefined' ? 'shop/' + itemsModelName + 's_items.html' : itemsTemplate);
        request_items(
                itemsModelName, template,
                {filter: itemsFilterInfo, order_by: '["' + order + column + '"]'});
    });
    update_items_icons()
});

