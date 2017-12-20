#   encoding=utf8
# service 业务逻辑，数据一致性

from dao import *


class RepairOrderService:

    def __init__(self):
        pass

    # 输入：
    # 输出：
    # 功能：
    @staticmethod
    def insert(insert_dict):
        insert_time = datetime.now()

        car_collector_name = insert_dict.get('car_collector_name')
        dispatcher_name = insert_dict.get('dispatcher_name')
        car_id = insert_dict.get('car_id')
        repair_money_total = insert_dict.get('repair_money_total')
        repairman_name = insert_dict.get('repairman_name')
        inspector_name = insert_dict.get('inspector_name')
        new_repair_order = RepairOrderDao(car_collector_name, dispatcher_name, car_id, repair_money_total,
                                          repairman_name, inspector_name, insert_time, insert_time)
        new_repair_order.insert()

        material_project_dicts = insert_dict.get('material_project_dicts')
        for material_project_dict in material_project_dicts:
            repair_project_name = material_project_dict.get('repair_project_name')
            repair_material_id = material_project_dict.get('repair_material_id')
            repair_material_cost_amount = material_project_dict.get('repair_material_cost_amount')
            temp_material_project_dict = RepairProjectDao(repair_project_name, repair_material_id, new_repair_order.id,
                                                          repair_material_cost_amount, insert_time, insert_time)
            temp_material_project_dict.insert()

        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return {"status": False, "message": e}
        else:
            return {"status": True, "message": new_repair_order}

    # 输入：
    # 输出：
    # 功能：
    @staticmethod
    def update(update_dict):
        update_time = datetime.now()

        repair_order_id = update_dict.get('repair_order_id')
        car_collector_name = update_dict.get('car_collector_name')
        dispatcher_name = update_dict.get('dispatcher_name')
        car_id = update_dict.get('car_id')
        repair_money_total = update_dict.get('repair_money_total')
        repairman_name = update_dict.get('repairman_name')
        inspector_name = update_dict.get('inspector_name')
        repair_order_status = update_dict.get('repair_order_status')
        RepairOrderDao.update(repair_order_id, car_collector_name, dispatcher_name, car_id, repair_money_total,
                              repairman_name, inspector_name, repair_order_status, None, update_time)

        material_project_dicts = update_dict.get('material_project_dicts')
        for material_project_dict in material_project_dicts:
            repair_project_id = material_project_dict.get('repair_project_id')
            repair_project_name = material_project_dict.get('repair_project_name')
            repair_material_id = material_project_dict.get('repair_material_id')
            repair_material_cost_amount = material_project_dict.get('repair_material_cost_amount')

            RepairProjectDao.update(repair_project_id, repair_project_name, repair_material_id, None,
                                    repair_material_cost_amount, False, None, update_time)

        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return {"status": False, "message": e}
        else:
            return {"status": True, "message": RepairOrderDao.select_by_id(repair_order_id)}

    # 输入：
    # 输出：
    # 功能：
    @staticmethod
    def select():
        return RepairOrderDao.select()

    # 输入：
    # 输出：
    # 功能：
    @staticmethod
    def delete(repair_order_id):
        RepairOrderDao.delete(repair_order_id)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return {"status": False, "message": e}
        else:
            return {"status": True, "message": None}

    # 输入：
    # 输出：
    # 功能：
    @staticmethod
    def select_by_id(repair_order_id):
        return RepairOrderDao.select_by_id(repair_order_id)


class MaterialService:

    def __init__(self):
        pass

    # 输入：
    # 输出：
    # 功能：
    @staticmethod
    def insert():
        pass

    # 输入：
    # 输出：
    # 功能：
    @staticmethod
    def update():
        pass

    # 输入：
    # 输出：
    # 功能：
    @staticmethod
    def select():
        pass

    # 输入：
    # 输出：
    # 功能：
    @staticmethod
    def delete():
        pass

    # 输入：
    # 输出：
    # 功能：
    @staticmethod
    def select_by_id(id):
        pass


class CarOwnerService:

    def __init__(self):
        pass

    # 输入：
    # 输出：
    # 功能：
    @staticmethod
    def insert():
        pass

    # 输入：
    # 输出：
    # 功能：
    @staticmethod
    def update():
        pass

    # 输入：
    # 输出：
    # 功能：
    @staticmethod
    def select():
        pass

    # 输入：
    # 输出：
    # 功能：
    @staticmethod
    def delete():
        pass

    # 输入：
    # 输出：
    # 功能：
    @staticmethod
    def select_by_id(id):
        pass


if __name__ == "__main__":
    old_repair_order = RepairOrderDao.select_by_id(2)
    result = RepairOrderDao.select()
    # update_dict = dict()
    # update_dict['repair_order_id'] = 1
    # update_dict['car_id'] = 2
    # insert_dict = dict()
    # new_repair_order = RepairOrderService.update(update_dict)
    # test_repair_order = RepairOrderService.insert(insert_dict)
    print 'xxx'
