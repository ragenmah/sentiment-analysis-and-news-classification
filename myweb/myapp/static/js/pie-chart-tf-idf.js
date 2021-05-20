Highcharts.chart('pie-chart-tf-idf', {
    chart: {
        plotBackgroundColor: null,
        plotBorderWidth: null,
        plotShadow: false,
        type: 'pie'
    },
    title: {
        text: 'Pie-Chart for TF-IDF'
    },
    tooltip: {
        pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
    },
    plotOptions: {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
                enabled: true,
                format: '<b>{point.name}</b>: {point.percentage:.1f} %',
                style: {
                    color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
                }
            }
        }
    },
    series: [{
        name: 'TF-IDF',
        colorByPoint: true,
        data: [{
            name: 'Positive',
            y: 33
        }, {
            name: 'Negative',
            y: 24,
            sliced: true,
            selected: true
        }, {
            name: 'Neutral',
            y: 19
        }]
    }]
});