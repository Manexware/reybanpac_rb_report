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
//var zona = document.getElementById("zona");
//var zona_selected = zona.options[zona.selectedIndex].text;
//var hacienda = document.getElementById("hacienda");
//var hacienda_options = hacienda.options;
////remove_options(zona_selected,hacienda);
//zona.addEventListener('change', function() {
//    zona_selected = zona.options[zona.selectedIndex].text;
//    //remove_options(zona_selected,hacienda);
//    }, false)
//
//function remove_options(select_options,select) {
//    var count=0;
//    var compare;
//    if (select_options == 1)
//        compare="001"
//    else if (select_options== 2)
//        compare="002"
//    else
//        compare="null"
//    for (var i = 0; i < hacienda.options.length; i++) {
//            select.add(hacienda.options[i]);
//        }
//    for (var i = 0; i < select.options.length; i++) {
//        if (compare!="null")
//            if(select.options[i].value.split("-")[0]!=compare)
//                select.options[i].remove();
//        }
//}
var hacienda = document.getElementById("hacienda");
add_class_select(hacienda);
function add_class_select(select) {
        for (var i = 0; i < select.options.length; i++) {
                select.options[i].className += select.options[i].value.split("-")[0];
        }
}

$("#series").chained("#mark");
$("#hacienda").chained("#zona");
