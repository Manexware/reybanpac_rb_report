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
            text: 'Reporte de Barras'
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
var hacienda = document.getElementById("hacienda");
add_class_select(hacienda);
function add_class_select(select) {
        for (var i = 0; i < select.options.length; i++) {
                select.options[i].className += select.options[i].value.split("-")[0];
        }
}
$("#hacienda").chained("#zona");
