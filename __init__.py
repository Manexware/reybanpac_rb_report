from flask import Flask, render_template, request,flash,redirect
from forms import Form
import pymysql

app = Flask(__name__)
app.config.from_object('config')
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='password', db='rbpscp')
cur = conn.cursor()
#
@app.route('/',)
def report():
    return render_template('index.html')


@app.route('/pesos_cantidades', methods=['GET', 'POST'])
def pesos_cantidades():
    form = Form(request.form)
    _populated_select(form)
    if form.type.data =='1':
        cur.execute("SELECT id, peso, item, fecha, orden, cod_empacadora, peso_neto, peso_bruto, cod_item_corto, cod_hacienda, "
                    "ROUND(AVG(peso),2) as promedio, COUNT(orden) as total_cajas, cantidad, ROUND(MIN(peso),2) as minimo, "
                    "ROUND(MAX(peso),2) as maximo, ROUND(AVG(peso_bruto),2) as promedio_bruto FROM caja ")
    if form.type.data =='2':
        cur.execute("SELECT id, peso, item, fecha, orden, cod_empacadora, peso_neto, peso_bruto, cod_item_corto, cod_hacienda, "
                    "ROUND(AVG(peso),2) as promedio, COUNT(orden) as total_cajas, cantidad, ROUND(MIN(peso),2) as minimo, "
                    "ROUND(MAX(peso),2) as maximo, ROUND(AVG(peso_bruto),2) as promedio_bruto "
                    "FROM bandeja WHERE DATE(fecha)='$fecha_consulta' GROUP BY orden, cod_item_corto ORDER BY "
                    "cod_empacadora, orden")
    if form.type.data =='3':
        cur.execute("SELECT r.idracimo, r.idconvoy, r.peso, r.timestamp as fecha_racimo, r.numlote as lote_racimo, "
                    "r.cinta, r.edad, r.cod_empacadora, r.cod_hacienda, r.tara, c.timestamp as fecha_convoy,c.num_racimos, "
                    "c.cuadrilla, COUNT(peso) as cantidad_pesada, ROUND(AVG(tara),2) as prom_tara, "
                    "ROUND(MIN(CAST(peso AS DECIMAL)),2) as minimo, ROUND(MAX(CAST(peso AS DECIMAL)),2) as maximo, "
                    "ROUND(AVG(CAST(peso AS DECIMAL)),2) as peso_promedio from racimo r left join convoy c ON(r.idconvoy=c.idconvoy) "
                    "WHERE DATE(r.timestamp)='"+form.date.data+"' GROUP BY r.idconvoy, r.numlote, r.cinta")
        cur.execute("SELECT r.idracimo, r.idconvoy, r.peso, r.timestamp as fecha_racimo, r.numlote as lote_racimo, "
                    "r.cinta, r.edad, r.cod_empacadora, r.cod_hacienda, r.tara, c.timestamp as fecha_convoy,c.num_racimos, "
                    "c.cuadrilla, COUNT(peso) as cantidad_pesada, ROUND(AVG(tara),2) as prom_tara, "
                    "ROUND(MIN(CAST(peso AS DECIMAL)),2) as minimo, ROUND(MAX(CAST(peso AS DECIMAL)),2) as maximo, "
                    "ROUND(AVG(CAST(peso AS DECIMAL)),2) as peso_promedio from racimo r left join convoy c ON(r.idconvoy=c.idconvoy) "
                    "WHERE DATE(r.timestamp)='"+form.date.data+"' GROUP BY r.cinta")
    if not form.type.data == 'None':
        data= cur.fetchall()
    else:
        data= []
    if not form.validate_on_submit():
        flash('Ingresar bien todos los campos')
    return render_template('pesos_cantidades.html',form=form, data=data)


@app.route('/racimos_cinta', methods=['GET', 'POST'])
def racimos_cinta():
    form = Form(request.form)
    _populated_select(form)
    if form.type.data =='1':
        cur.execute("SELECT id, peso, item, fecha, orden, cod_empacadora, peso_neto, peso_bruto, cod_item_corto, cod_hacienda, "
                    "ROUND(AVG(peso),2) as promedio, COUNT(orden) as total_cajas, cantidad, ROUND(MIN(peso),2) as minimo, "
                    "ROUND(MAX(peso),2) as maximo, ROUND(AVG(peso_bruto),2) as promedio_bruto FROM caja ")
    if form.type.data =='2':
        cur.execute("SELECT id, peso, item, fecha, orden, cod_empacadora, peso_neto, peso_bruto, cod_item_corto, cod_hacienda, "
                    "ROUND(AVG(peso),2) as promedio, COUNT(orden) as total_cajas, cantidad, ROUND(MIN(peso),2) as minimo, "
                    "ROUND(MAX(peso),2) as maximo, ROUND(AVG(peso_bruto),2) as promedio_bruto "
                    "FROM bandeja WHERE DATE(fecha)='$fecha_consulta' GROUP BY orden, cod_item_corto ORDER BY "
                    "cod_empacadora, orden")
    if form.type.data =='3':
        cur.execute("SELECT r.idracimo, r.idconvoy, r.peso, r.timestamp as fecha_racimo, r.numlote as lote_racimo, "
                    "r.cinta, r.edad, r.cod_empacadora, r.cod_hacienda, r.tara, c.timestamp as fecha_convoy,c.num_racimos, "
                    "c.cuadrilla, COUNT(peso) as cantidad_pesada, ROUND(AVG(tara),2) as prom_tara, "
                    "ROUND(MIN(CAST(peso AS DECIMAL)),2) as minimo, ROUND(MAX(CAST(peso AS DECIMAL)),2) as maximo, "
                    "ROUND(AVG(CAST(peso AS DECIMAL)),2) as peso_promedio from racimo r left join convoy c ON(r.idconvoy=c.idconvoy) "
                    "WHERE DATE(r.timestamp)='"+form.date.data+"' GROUP BY r.idconvoy, r.numlote, r.cinta")
        cur.execute("SELECT r.idracimo, r.idconvoy, r.peso, r.timestamp as fecha_racimo, r.numlote as lote_racimo, "
                    "r.cinta, r.edad, r.cod_empacadora, r.cod_hacienda, r.tara, c.timestamp as fecha_convoy,c.num_racimos, "
                    "c.cuadrilla, COUNT(peso) as cantidad_pesada, ROUND(AVG(tara),2) as prom_tara, "
                    "ROUND(MIN(CAST(peso AS DECIMAL)),2) as minimo, ROUND(MAX(CAST(peso AS DECIMAL)),2) as maximo, "
                    "ROUND(AVG(CAST(peso AS DECIMAL)),2) as peso_promedio from racimo r left join convoy c ON(r.idconvoy=c.idconvoy) "
                    "WHERE DATE(r.timestamp)='"+form.date.data+"' GROUP BY r.cinta")
    if not form.type.data == 'None':
        data= cur.fetchall()
    else:
        data= []
    if not form.validate_on_submit():
        flash('Ingresar bien todos los campos')
    return render_template('racimos_cinta.html',form=form, data=data)


@app.route('/racimos_faltantes',  methods=['GET', 'POST'])
def racimos_faltantes():
    form = Form(request.form)
    _populated_select(form)
    if form.type.data =='1':
        cur.execute("SELECT id, peso, item, fecha, orden, cod_empacadora, peso_neto, peso_bruto, cod_item_corto, cod_hacienda, "
                    "ROUND(AVG(peso),2) as promedio, COUNT(orden) as total_cajas, cantidad, ROUND(MIN(peso),2) as minimo, "
                    "ROUND(MAX(peso),2) as maximo, ROUND(AVG(peso_bruto),2) as promedio_bruto FROM caja ")
    if form.type.data =='2':
        cur.execute("SELECT id, peso, item, fecha, orden, cod_empacadora, peso_neto, peso_bruto, cod_item_corto, cod_hacienda, "
                    "ROUND(AVG(peso),2) as promedio, COUNT(orden) as total_cajas, cantidad, ROUND(MIN(peso),2) as minimo, "
                    "ROUND(MAX(peso),2) as maximo, ROUND(AVG(peso_bruto),2) as promedio_bruto "
                    "FROM bandeja WHERE DATE(fecha)='$fecha_consulta' GROUP BY orden, cod_item_corto ORDER BY "
                    "cod_empacadora, orden")
    if form.type.data =='3':
        cur.execute("SELECT r.idracimo, r.idconvoy, r.peso, r.timestamp as fecha_racimo, r.numlote as lote_racimo, "
                    "r.cinta, r.edad, r.cod_empacadora, r.cod_hacienda, r.tara, c.timestamp as fecha_convoy,c.num_racimos, "
                    "c.cuadrilla, COUNT(peso) as cantidad_pesada, ROUND(AVG(tara),2) as prom_tara, "
                    "ROUND(MIN(CAST(peso AS DECIMAL)),2) as minimo, ROUND(MAX(CAST(peso AS DECIMAL)),2) as maximo, "
                    "ROUND(AVG(CAST(peso AS DECIMAL)),2) as peso_promedio from racimo r left join convoy c ON(r.idconvoy=c.idconvoy) "
                    "WHERE DATE(r.timestamp)='"+form.date.data+"' GROUP BY r.idconvoy, r.numlote, r.cinta")
        cur.execute("SELECT r.idracimo, r.idconvoy, r.peso, r.timestamp as fecha_racimo, r.numlote as lote_racimo, "
                    "r.cinta, r.edad, r.cod_empacadora, r.cod_hacienda, r.tara, c.timestamp as fecha_convoy,c.num_racimos, "
                    "c.cuadrilla, COUNT(peso) as cantidad_pesada, ROUND(AVG(tara),2) as prom_tara, "
                    "ROUND(MIN(CAST(peso AS DECIMAL)),2) as minimo, ROUND(MAX(CAST(peso AS DECIMAL)),2) as maximo, "
                    "ROUND(AVG(CAST(peso AS DECIMAL)),2) as peso_promedio from racimo r left join convoy c ON(r.idconvoy=c.idconvoy) "
                    "WHERE DATE(r.timestamp)='"+form.date.data+"' GROUP BY r.cinta")
    if not form.type.data == 'None':
        data= cur.fetchall()
    else:
        data= []
    if not form.validate_on_submit():
        flash('Ingresar bien todos los campos')
    return render_template('racimos_faltantes.html',form=form, data=data)


@app.route('/ranking_empleados',  methods=['GET', 'POST'])
def ranking_empleados():
    form = Form(request.form)
    _populated_select(form)
    if form.type.data =='1':
        cur.execute("SELECT id, peso, item, fecha, orden, cod_empacadora, peso_neto, peso_bruto, cod_item_corto, cod_hacienda, "
                    "ROUND(AVG(peso),2) as promedio, COUNT(orden) as total_cajas, cantidad, ROUND(MIN(peso),2) as minimo, "
                    "ROUND(MAX(peso),2) as maximo, ROUND(AVG(peso_bruto),2) as promedio_bruto FROM caja ")
    if form.type.data =='2':
        cur.execute("SELECT id, peso, item, fecha, orden, cod_empacadora, peso_neto, peso_bruto, cod_item_corto, cod_hacienda, "
                    "ROUND(AVG(peso),2) as promedio, COUNT(orden) as total_cajas, cantidad, ROUND(MIN(peso),2) as minimo, "
                    "ROUND(MAX(peso),2) as maximo, ROUND(AVG(peso_bruto),2) as promedio_bruto "
                    "FROM bandeja WHERE DATE(fecha)='$fecha_consulta' GROUP BY orden, cod_item_corto ORDER BY "
                    "cod_empacadora, orden")
    if form.type.data =='3':
        cur.execute("SELECT r.idracimo, r.idconvoy, r.peso, r.timestamp as fecha_racimo, r.numlote as lote_racimo, "
                    "r.cinta, r.edad, r.cod_empacadora, r.cod_hacienda, r.tara, c.timestamp as fecha_convoy,c.num_racimos, "
                    "c.cuadrilla, COUNT(peso) as cantidad_pesada, ROUND(AVG(tara),2) as prom_tara, "
                    "ROUND(MIN(CAST(peso AS DECIMAL)),2) as minimo, ROUND(MAX(CAST(peso AS DECIMAL)),2) as maximo, "
                    "ROUND(AVG(CAST(peso AS DECIMAL)),2) as peso_promedio from racimo r left join convoy c ON(r.idconvoy=c.idconvoy) "
                    "WHERE DATE(r.timestamp)='"+form.date.data+"' GROUP BY r.idconvoy, r.numlote, r.cinta")
        cur.execute("SELECT r.idracimo, r.idconvoy, r.peso, r.timestamp as fecha_racimo, r.numlote as lote_racimo, "
                    "r.cinta, r.edad, r.cod_empacadora, r.cod_hacienda, r.tara, c.timestamp as fecha_convoy,c.num_racimos, "
                    "c.cuadrilla, COUNT(peso) as cantidad_pesada, ROUND(AVG(tara),2) as prom_tara, "
                    "ROUND(MIN(CAST(peso AS DECIMAL)),2) as minimo, ROUND(MAX(CAST(peso AS DECIMAL)),2) as maximo, "
                    "ROUND(AVG(CAST(peso AS DECIMAL)),2) as peso_promedio from racimo r left join convoy c ON(r.idconvoy=c.idconvoy) "
                    "WHERE DATE(r.timestamp)='"+form.date.data+"' GROUP BY r.cinta")
    if not form.type.data == 'None':
        data= cur.fetchall()
    else:
        data= []
    if not form.validate_on_submit():
        flash('Ingresar bien todos los campos')
    return render_template('ranking_empleados.html',form=form, data=data)

def _populated_select(form):
    cur.execute("SELECT idconvoy from convoy")
    cur.fetchall()
    zonas = [("00"+str(c[0]), c[0]) for c in cur._rows]
    form.zona.choices = zonas

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
