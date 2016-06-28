$('.input-group.date').datepicker({
                            format: "yyyy-mm-dd",
                            autoclose: true,
                            todayHighlight: true,
                            todayBtn: true,
                            setDate :  new Date(),
                        });
$(function () {
    $('#graphcontainer').highcharts({
        data: {
            table: 'report_column'
        },
        chart: {
            type: 'column'
        },
        title: {
            text: 'Data extracted from a HTML table in the page'
        },
        yAxis: {
            allowDecimals: false,
            title: {
                text: 'Units'
            }
        },
        tooltip: {
            formatter: function () {
                return '<b>' + this.series.name + '</b><br/>' +
                    this.point.y + ' ' + this.point.name.toLowerCase();
            }
        }
    });
});