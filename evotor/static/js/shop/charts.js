function plot_chart_id_need(barcode) {
    if (!barcode) {
        console.log("Invalid barcode")
        return
    }

    let canvas = $(".product-" + barcode + "-chart");
    if (!canvas.hasClass("inactive")) {
        console.log("Already plot")
        return;
    }
    canvas.removeClass("inactive")

    let labels = []
    let dataset = productChartsData[barcode]
    for (let i = 0; i < dataset.data.length; ++i) {
        labels.push("неделя " + i);
    }

    let ctx = canvas[0].getContext("2d");
    let myLineChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: "Продажи",
                data: dataset.data,
                borderColor: '#8888cc',
                backgroundColor: '#ccccff',
                fill: false,
            }],
        },
    });
    $(".product-" + barcode + "-chart-stub").hide();
}

$(function() {
    $(".product-expand-link").click(function() {
        plot_chart_id_need($(this).attr("barcode"));
    });
})
