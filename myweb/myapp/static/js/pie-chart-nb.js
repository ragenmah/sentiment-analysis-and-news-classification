Highcharts.chart('pie-chart-nb', {
    chart: {
        plotBackgroundColor: null,
        plotBorderWidth: null,
        plotShadow: false,
        type: 'pie'
    },
    title: {
        text: 'Pie-Chart for Naive Bayes'
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
        name: 'Naive Bayes',
        colorByPoint: true,
        data: [{
            name: 'Positive',
            y: 22
        }, {
            name: 'Negative',
            y: 33,
            sliced: true,
            selected: true
        }, {
            name: 'Neutral',
            y: 21
        }]
    }]
});