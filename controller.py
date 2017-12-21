#   encoding=utf8
# controller 控制转发

from service import app, MaterialService, CarOwnerService, RepairOrderService
from flask import request, json


class RepairOrderController:

    def __init__(self):
        pass

    # 输入：
    # 输出：
    # 功能：
    @staticmethod
    @app.route('/repairOrder/insert', methods=['POST'])
    def repair_order_insert():
        insert_dict = dict()
        insert_dict['repair_order_id'] = request.form.get('repair_order_id')
        insert_dict['car_collector_name'] = request.form.get('car_collector_name')
        insert_dict['dispatcher_name'] = request.form.get('dispatcher_name')
        insert_dict['car_id'] = request.form.get('car_id')
        insert_dict['repair_money_total'] = request.form.get('repair_money_total')
        insert_dict['repairman_name'] = request.form.get('repairman_name')
        insert_dict['inspector_name'] = request.form.get('inspector_name')
        insert_dict['repair_order_status'] = request.form.get('repair_order_status')
        insert_dict['repair_project_dicts'] = json.loads(request.form.get('repair_project_dicts'))
        # repair_project_name, repair_material_id, repair_material_cost_amount
        return RepairOrderService.insert(insert_dict)

    # 输入：
    # 输出：
    # 功能：
    @staticmethod
    @app.route('/repairOrder/insertRepairProject', methods=['POST'])
    def repair_order_insert_repair_project():
        insert_dict = dict()
        insert_dict['repair_order_id'] = request.form.get('repair_order_id')
        insert_dict['repair_project_name'] = request.form.get('repair_project_name')
        insert_dict['repair_material_id'] = request.form.get('repair_material_id')
        insert_dict['repair_material_cost_amount'] = request.form.get('repair_material_cost_amount')
        return RepairOrderService.insert_repair_project(insert_dict)

    # 输入：
    # 输出：
    # 功能：
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
        update_dict['repair_project_dicts'] = json.loads(request.form.get('repair_project_dicts'))
        # repair_project_id, repair_project_name, repair_material_id, repair_material_cost_amount
        return RepairOrderService.update(update_dict)

    # 输入：
    # 输出：
    # 功能：
    @staticmethod
    @app.route('/repairOrder/select', methods=['GET'])
    def repair_order_select():
        start = request.args.get('start')
        page_size = request.args.get('page_size')
        return RepairOrderService.select(start, page_size)

    # 输入：
    # 输出：
    # 功能：
    @staticmethod
    @app.route('/repairOrder/selectRepairProject', methods=['GET'])
    def repair_order_select_repair_project():
        repair_order_id = request.args.get('repair_order_id')
        start = request.args.get('start')
        page_size = request.args.get('page_size')
        return RepairOrderService.select_repair_project(repair_order_id, start, page_size)

    # 输入：
    # 输出：
    # 功能：
    @staticmethod
    @app.route('/repairOrder/delete', methods=['GET'])
    def repair_order_delete():
        repair_order_id = request.args.get('repair_order_id')
        return RepairOrderService.delete(repair_order_id)

    # 输入：
    # 输出：
    # 功能：
    @staticmethod
    @app.route('/repairOrder/deleteRepairProject', methods=['GET'])
    def repair_order_delete_repair_project():
        repair_project_id = request.args.get('repair_project_id')
        return RepairOrderService.delete_repair_project(repair_project_id)

    # 输入：
    # 输出：
    # 功能：
    @staticmethod
    @app.route('/repairOrder/selectById', methods=['GET'])
    def repair_order_select_by_id():
        repair_order_id = request.args.get('repair_order_id')
        return RepairOrderService.select_by_id(repair_order_id)


class MaterialController:

    def __init__(self):
        pass

    # 输入：
    # 输出：
    # 功能：
    @staticmethod
    @app.route('/material/insert', methods=['POST'])
    def material_insert():
        insert_dict = dict()
        insert_dict['repair_material_name'] = request.form.get('repair_material_name')
        insert_dict['repair_material_has_amount'] = request.form.get('repair_material_has_amount')
        return MaterialService.insert(insert_dict)

    # 输入：
    # 输出：
    # 功能：
    @staticmethod
    @app.route('/material/update', methods=['POST'])
    def material_update():
        update_dict = dict()
        update_dict['repair_material_id'] = request.form.get('repair_material_id')
        update_dict['repair_material_name'] = request.form.get('repair_material_name')
        update_dict['repair_material_has_amount'] = request.form.get('repair_material_has_amount')
        return MaterialService.update(update_dict)

    # 输入：
    # 输出：
    # 功能：
    @staticmethod
    @app.route('/material/confirm', methods=['GET'])
    def material_confirm():
        repair_order_id = request.args.get('repair_order_id')
        return MaterialService.confirm(repair_order_id)

    # 输入：
    # 输出：
    # 功能：
    @staticmethod
    @app.route('/material/select', methods=['GET'])
    def material_select():
        start = request.args.get('start')
        page_size = request.args.get('page_size')
        return MaterialService.select(start, page_size)

    # 输入：
    # 输出：
    # 功能：
    @staticmethod
    @app.route('/material/delete', methods=['GET'])
    def material_delete():
        repair_material_id = request.args.get('repair_material_id')
        return MaterialService.delete(repair_material_id)

    # 输入：
    # 输出：
    # 功能：
    @staticmethod
    @app.route('/material/selectById', methods=['GET'])
    def material_select_by_id():
        repair_material_id = request.args.get('repair_material_id')
        return MaterialService.select_by_id(repair_material_id)


class CarOwnerController:

    def __init__(self):
        pass

    # 输入：
    # 输出：
    # 功能：
    @staticmethod
    @app.route('/carOwner/insert', methods=['POST'])
    def car_owner_insert():
        insert_dict = dict()
        insert_dict['car_owner_name'] = request.form.get('car_owner_name')
        insert_dict['car_owner_number'] = request.form.get('car_owner_number')
        insert_dict['car_dicts'] = json.loads(request.form.get('car_dicts'))  # car_brand, plate_number
        return CarOwnerService.insert(insert_dict)

    # 输入：
    # 输出：
    # 功能：
    @staticmethod
    @app.route('/carOwner/insertCar', methods=['POST'])
    def car_owner_insert_car():
        insert_dict = dict()
        insert_dict['car_owner_id'] = request.form.get('car_owner_id')
        insert_dict['car_brand'] = request.form.get('car_brand')
        insert_dict['plate_number'] = request.form.get('plate_number')
        return CarOwnerService.insert_car(insert_dict)

    # 输入：
    # 输出：
    # 功能：
    @staticmethod
    @app.route('/carOwner/deleteCar', methods=['GET'])
    def car_owner_delete_car():
        car_id = request.args.get('car_id')
        return CarOwnerService.delete_car(car_id)

    # 输入：
    # 输出：
    # 功能：
    @staticmethod
    @app.route('/carOwner/update', methods=['POST'])
    def car_owner_update():
        update_dict = dict()
        update_dict['car_owner_name'] = request.form.get('car_owner_name')
        update_dict['car_owner_number'] = request.form.get('car_owner_number')
        update_dict['car_dicts'] = json.loads(request.form.get('car_dicts'))  # car_id, car_brand, plate_number
        return CarOwnerService.update(update_dict)

    # 输入：
    # 输出：
    # 功能：
    @staticmethod
    @app.route('/carOwner/select', methods=['GET'])
    def car_owner_select():
        start = request.args.get('start')
        page_size = request.args.get('page_size')
        return CarOwnerService.select(start, page_size)

    # 输入：
    # 输出：
    # 功能：
    @staticmethod
    @app.route('/carOwner/selectCar', methods=['GET'])
    def car_owner_select_car():
        car_owner_id = request.args.get('car_owner_id')
        start = request.args.get('start')
        page_size = request.args.get('page_size')
        return CarOwnerService.select_car(car_owner_id, start, page_size)

    # 输入：
    # 输出：
    # 功能：
    @staticmethod
    @app.route('/carOwner/delete', methods=['GET'])
    def car_owner_delete():
        car_owner_id = request.args.get('car_owner_id')
        return CarOwnerService.delete(car_owner_id)

    # 输入：
    # 输出：
    # 功能：
    @staticmethod
    @app.route('/carOwner/selectById', methods=['GET'])
    def car_owner_select_by_id():
        car_owner_id = request.args.get('car_owner_id')
        return CarOwnerService.select_by_id(car_owner_id)

    # 输入：
    # 输出：
    # 功能：
    @staticmethod
    @app.route('/carOwner/selectByCarOwnerNumber', methods=['GET'])
    def car_owner_select_by_car_owner_number():
        car_owner_number = request.args.get('car_owner_number')
        return CarOwnerService.select_by_car_owner_number(car_owner_number)

    # 输入：
    # 输出：
    # 功能：
    @staticmethod
    @app.route('/carOwner/selectCarByPlateNumber', methods=['GET'])
    def car_owner_select_car_by_plate_number():
        plate_number = request.args.get('plate_number')
        return CarOwnerService.select_car_by_plate_number(plate_number)
