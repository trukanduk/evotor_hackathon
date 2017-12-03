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
    let data1 = []
    let data2 = []
    let dataset = shopData[barcode]
    for (let i = 0; i < dataset.values.length; ++i) {
        labels.push("неделя " + i);
        if (dataset.is_pred[i]) {
            data2.push(dataset.values[i])
        } else {
            if (dataset.is_pred[i + 1]) {
                data2.push(dataset.values[i])
            } else {
                data2.push(NaN)
            }
            data1.push(dataset.values[i])
        }
    }

    let ctx = canvas[0].getContext("2d");
    let myLineChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: "История",
                data: data1,
                borderColor: '#8888cc',
                backgroundColor: '#ccccff',
                fill: false,
            },
            {
                label: "Прогноз",
                data: data2,
                borderColor: '#88cc88',
                backgroundColor: '#ccffcc',
                fill: false,
                beginAtZero: false
            }],
        },
        options: {
            title: {
            display: true,
            text: 'Дневные продажи'
        }
        }
    });
    $(".product-" + barcode + "-chart-stub").hide();
}

$(function() {
    $(".product-expand-link").click(function() {
        plot_chart_id_need($(this).attr("barcode"));
    });
})
