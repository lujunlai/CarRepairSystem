from controller import app
from flask import send_from_directory, render_template, request


@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('templates/js', path)


@app.route('/pic/<path:path>')
def send_pic(path):
    return send_from_directory('templates/pic', path)


@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('templates/css', path)


@app.route('/favicon.ico')
def send_favicon():
    return send_from_directory('templates', 'favicon.ico')


@app.route('/repairOrder')
def repair_order():
    return render_template('repair_order.html')


@app.route('/car')
def car():
    car_dict = dict()
    car_dict['car_owner_id'] = request.args.get('car_owner_id') if request.args.get('car_owner_id') is not None else -1
    car_dict['car_id'] = request.args.get('car_id') if request.args.get('car_id') is not None else -1
    return render_template('car.html', car_dict=car_dict)


@app.route('/repairProject')
def repair_project():
    repair_order_id = request.args.get('repair_order_id')
    return render_template('repair_project.html', repair_order_id=repair_order_id)


@app.route('/material')
def material():
    material_dict = dict()
    material_dict['material_id'] = request.args.get('material_id') if request.args.get('material_id') is not None \
        else -1
    return render_template('material.html', material_dict=material_dict)


@app.route('/carOwner')
def car_owner():
    car_owner_dict = dict()
    car_owner_dict['car_owner_id'] = request.args.get('car_owner_id') if request.args.get('car_owner_id') is not None \
        else -1
    return render_template('car_owner.html', car_owner_dict=car_owner_dict)


if __name__ == '__main__':
    app.run(debug=True, threaded=True)
