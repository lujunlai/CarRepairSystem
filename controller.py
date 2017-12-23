#   encoding=utf8
# controller 控制转发

from service import app, MaterialService, CarOwnerService, RepairOrderService, CarService, RepairProjectService
from flask import request, json


class RepairProjectController:

    def __init__(self):
        pass

    @staticmethod
    @app.route('/repairProject/insert', methods=['POST'])
    def repair_project_insert():
        insert_dict = dict()
        insert_dict['start'] = request.form.get('start')
        insert_dict['page_size'] = request.form.get('page_size')
        insert_dict['repair_order_id'] = request.form.get('repair_order_id')
        insert_dict['repair_project_dicts'] = json.loads(request.form.get('repair_project_dicts'))  # List
        # repair_project_name = repair_project_dict.get('repair_project_name')
        # repair_material_id = repair_project_dict.get('repair_material_id')
        # repair_material_cost_amount = repair_project_dict.get('repair_material_cost_amount')
        return RepairProjectService.insert(insert_dict).serialize

    @staticmethod
    @app.route('/repairProject/delete', methods=['GET'])
    def repair_project_delete():
        delete_list = request.args.get('delete_list')
        return RepairProjectService.delete(json.loads(delete_list)).serialize

    @staticmethod
    @app.route('/repairProject/update', methods=['POST'])
    def repair_project_update():
        update_dict = dict()
        update_dict['start'] = request.form.get('start')
        update_dict['page_size'] = request.form.get('page_size')
        update_dict['repair_order_id'] = request.form.get('repair_order_id')
        update_dict['repair_project_dicts'] = json.loads(request.form.get('repair_project_dicts'))  # List
        # repair_project_id = repair_project_dict.get('repair_project_id')
        # repair_project_name = repair_project_dict.get('repair_project_name')
        # repair_material_id = repair_project_dict.get('repair_material_id')
        # repair_material_cost_amount = repair_project_dict.get('repair_material_cost_amount')
        return RepairProjectService.update(update_dict).serialize

    @staticmethod
    @app.route('/repairProject/select', methods=['GET'])
    def repair_project_select():
        repair_order_id = request.args.get('repair_order_id')
        start = request.args.get('start')
        page_size = request.args.get('page_size')
        return RepairProjectService.select(repair_order_id, start, page_size).serialize

    @staticmethod
    @app.route('/repairProject/deleteByRepairOrderId', methods=['GET'])
    def repair_project_delete_by_repair_order_id():
        repair_order_id = request.args.get('repair_order_id')
        return RepairProjectService.delete_by_repair_id(repair_order_id).serialize

    @staticmethod
    @app.route('/repairProject/selectById', methods=['GET'])
    def repair_project_select_by_id():
        repair_project_id = request.args.get('repair_project_id')
        return RepairProjectService.select_by_id(repair_project_id).serialize


class RepairOrderController:

    def __init__(self):
        pass

    @staticmethod
    @app.route('/repairOrder/insert', methods=['POST'])
    def repair_order_insert():
        insert_dict = dict()
        insert_dict['car_collector_name'] = request.form.get('car_collector_name')
        insert_dict['dispatcher_name'] = request.form.get('dispatcher_name')
        insert_dict['car_id'] = request.form.get('car_id')
        insert_dict['repair_money_total'] = request.form.get('repair_money_total')
        insert_dict['repairman_name'] = request.form.get('repairman_name')
        insert_dict['inspector_name'] = request.form.get('inspector_name')
        return RepairOrderService.insert(insert_dict).serialize

    @staticmethod
    @app.route('/repairOrder/delete', methods=['GET'])
    def repair_order_delete():
        repair_order_id = request.args.get('repair_order_id')
        return RepairOrderService.delete(repair_order_id).serialize

    @staticmethod
    @app.route('/repairOrder/update', methods=['POST'])
    def repair_order_update():
        update_dict = dict()
        update_dict['repair_order_id'] = request.form.get('repair_order_id')
        update_dict['car_collector_name'] = request.form.get('car_collector_name')
        update_dict['dispatcher_name'] = request.form.get('dispatcher_name')
        update_dict['car_id'] = request.form.get('car_id')
        update_dict['repair_money_total'] = request.form.get('repair_money_total')
        update_dict['repairman_name'] = request.form.get('repairman_name')
        update_dict['inspector_name'] = request.form.get('inspector_name')
        update_dict['repair_order_status'] = request.form.get('repair_order_status')
        return RepairOrderService.update(update_dict).serialize

    @staticmethod
    @app.route('/repairOrder/select', methods=['GET'])
    def repair_order_select():
        start = request.args.get('start')
        page_size = request.args.get('page_size')
        return RepairOrderService.select(start, page_size).serialize

    @staticmethod
    @app.route('/repairOrder/selectById', methods=['GET'])
    def repair_order_select_by_id():
        repair_order_id = request.args.get('repair_order_id')
        return RepairOrderService.select_by_id(repair_order_id).serialize


class MaterialController:

    def __init__(self):
        pass

    @staticmethod
    @app.route('/material/insert', methods=['POST'])
    def material_insert():
        insert_dict = dict()
        insert_dict['repair_material_name'] = request.form.get('repair_material_name')
        insert_dict['repair_material_has_amount'] = request.form.get('repair_material_has_amount')
        return MaterialService.insert(insert_dict).serialize

    @staticmethod
    @app.route('/material/update', methods=['POST'])
    def material_update():
        update_dict = dict()
        update_dict['repair_material_id'] = request.form.get('repair_material_id')
        update_dict['repair_material_name'] = request.form.get('repair_material_name')
        update_dict['repair_material_has_amount'] = request.form.get('repair_material_has_amount')
        return MaterialService.update(update_dict).serialize

    @staticmethod
    @app.route('/material/confirm', methods=['GET'])
    def material_confirm():
        repair_order_id = request.args.get('repair_order_id')
        return MaterialService.confirm(repair_order_id).serialize

    @staticmethod
    @app.route('/material/select', methods=['GET'])
    def material_select():
        start = request.args.get('start')
        page_size = request.args.get('page_size')
        return MaterialService.select(start, page_size).serialize

    @staticmethod
    @app.route('/material/delete', methods=['GET'])
    def material_delete():
        material_id = request.args.get('material_id')
        return MaterialService.delete(material_id).serialize

    @staticmethod
    @app.route('/material/selectById', methods=['GET'])
    def material_select_by_id():
        material_id = request.args.get('material_id')
        return MaterialService.select_by_id(material_id).serialize


class CarController:

    def __init__(self):
        pass

    @staticmethod
    @app.route('/car/insert', methods=['POST'])
    def car_insert():
        insert_dict = dict()
        insert_dict['start'] = request.form.get('start')
        insert_dict['page_size'] = request.form.get('page_size')
        insert_dict['car_owner_id'] = request.form.get('car_owner_id')
        insert_dict['car_dicts'] = json.loads(request.form.get('car_dicts'))  # List
        # car_brand = car_dict.get('car_brand')
        # plate_number = car_dict.get('plate_number')
        return CarService.insert(insert_dict).serialize

    @staticmethod
    @app.route('/car/delete', methods=['GET'])
    def car_delete():
        delete_list = request.args.get('delete_list')
        return CarService.delete(json.loads(delete_list)).serialize

    @staticmethod
    @app.route('/car/update', methods=['POST'])
    def car_update():
        update_dict = dict()
        update_dict['start'] = request.form.get('start')
        update_dict['page_size'] = request.form.get('page_size')
        update_dict['car_owner_id'] = request.form.get('car_owner_id')
        update_dict['car_dicts'] = json.loads(request.form.get('car_dicts'))  # List
        # car_id = car_dict.get('car_id')
        # car_brand = car_dict.get('car_brand')
        # plate_number = car_dict.get('plate_number')
        return CarService.update(update_dict).serialize

    @staticmethod
    @app.route('/car/select', methods=['GET'])
    def car_select():
        car_owner_id = request.args.get('car_owner_id')
        start = request.args.get('start')
        page_size = request.args.get('page_size')
        return CarService.select(car_owner_id, start, page_size).serialize

    @staticmethod
    @app.route('/car/selectById', methods=['GET'])
    def select_by_id():
        car_id = request.args.get('car_id')
        return CarService.select_by_id(car_id).serialize

    @staticmethod
    @app.route('/car/selectByPlateNumber', methods=['GET'])
    def select_by_plate_number():
        plate_number = request.args.get('plate_number')
        return CarService.select_by_plate_number(plate_number).serialize


class CarOwnerController:

    def __init__(self):
        pass

    @staticmethod
    @app.route('/carOwner/insert', methods=['POST'])
    def car_owner_insert():
        insert_dict = dict()
        insert_dict['car_owner_name'] = request.form.get('car_owner_name')
        insert_dict['car_owner_number'] = request.form.get('car_owner_number')
        return CarOwnerService.insert(insert_dict).serialize

    @staticmethod
    @app.route('/carOwner/delete', methods=['GET'])
    def car_owner_delete():
        car_owner_id = request.args.get('car_owner_id')
        return CarOwnerService.delete(car_owner_id).serialize

    @staticmethod
    @app.route('/carOwner/update', methods=['POST'])
    def car_owner_update():
        update_dict = dict()
        update_dict['car_owner_name'] = request.form.get('car_owner_name')
        update_dict['car_owner_number'] = request.form.get('car_owner_number')
        return CarOwnerService.update(update_dict).serialize

    @staticmethod
    @app.route('/carOwner/select', methods=['GET'])
    def car_owner_select():
        start = request.args.get('start')
        page_size = request.args.get('page_size')
        return CarOwnerService.select(start, page_size).serialize

    @staticmethod
    @app.route('/carOwner/selectById', methods=['GET'])
    def car_owner_select_by_id():
        car_owner_id = request.args.get('car_owner_id')
        return CarOwnerService.select_by_id(car_owner_id).serialize

    @staticmethod
    @app.route('/carOwner/selectByCarOwnerNumber', methods=['GET'])
    def car_owner_select_by_car_owner_number():
        car_owner_number = request.args.get('car_owner_number')
        return CarOwnerService.select_by_car_owner_number(car_owner_number).serialize
