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
$(document).ready(function(){
    $('#report_table').DataTable({
    language:{
    "sProcessing":     "Procesando...",
    "sLengthMenu":     "Mostrar _MENU_ registros",
    "sZeroRecords":    "No se encontraron resultados",
    "sEmptyTable":     "Ningún dato disponible en esta tabla",
    "sInfo":           "Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros",
    "sInfoEmpty":      "Mostrando registros del 0 al 0 de un total de 0 registros",
    "sInfoFiltered":   "(filtrado de un total de _MAX_ registros)",
    "sInfoPostFix":    "",
    "sSearch":         "Buscar:",
    "sUrl":            "",
    "sInfoThousands":  ",",
    "sLoadingRecords": "Cargando...",
    "oPaginate": {
        "sFirst":    "Primero",
        "sLast":     "Último",
        "sNext":     "Siguiente",
        "sPrevious": "Anterior"
    },
    "oAria": {
        "sSortAscending":  ": Activar para ordenar la columna de manera ascendente",
        "sSortDescending": ": Activar para ordenar la columna de manera descendente"
    }
}});
});
var hacienda = document.getElementById("hacienda");
add_class_select(hacienda);
function add_class_select(select) {
        for (var i = 0; i < select.options.length; i++) {
                select.options[i].className += select.options[i].value.split("-")[0];
        }
}
$("#hacienda").chained("#zona");

