#   encoding=utf8
# service 业务逻辑，数据一致性
# 输出是Result类，status是操作状态，message是信息
# 输出提及的类为message里的对象

from dao import *
from logger import logged
from flask import jsonify


class RepairProjectService:

    def __init__(self):
        pass

    # 输入：项目信息 Dict
    # 输出：项目列表 List<RepairProjectDao>
    # 功能：项目信息插入数据库 包括RepairProject表
    @staticmethod
    @logged
    def insert(insert_dict):
        insert_time = datetime.now()
        repair_order_id = insert_dict.get('repair_order_id')
        repair_project_name = insert_dict.get('repair_project_name')
        repair_material_id = insert_dict.get('repair_material_id')
        repair_material_cost_amount = insert_dict.get('repair_material_cost_amount')

        new_repair_project = RepairProjectDao(repair_project_name, repair_material_id, repair_order_id,
                                              repair_material_cost_amount, insert_time, insert_time)
        new_repair_project.insert()
        RepairOrderDao.update(repair_order_id, None, None, None, None, None, None, None, None, insert_time)
        return db_commit(new_repair_project)

    # 输入：项目id列表 List<Int>
    # 输出：
    # 功能：批量删除项目 包括RepairProject表
    @staticmethod
    @logged
    def delete(delete_list):
        for repair_project_id in delete_list:
            RepairProjectDao.delete(repair_project_id)
        return db_commit(None)

    # 输入：项目信息 Dict
    # 输出：项目 RepairProjectDao
    # 功能：项目信息更新数据库 包括RepairProject表
    @staticmethod
    @logged
    def update(update_dict):
        update_time = datetime.now()
        repair_project_id = update_dict.get('repair_project_id')
        repair_project_name = update_dict.get('repair_project_name')
        repair_material_cost_amount = update_dict.get('repair_material_cost_amount')

        RepairProjectDao.update(repair_project_id, repair_project_name, None, None,
                                repair_material_cost_amount, None, None, update_time)

        update_repair_project = RepairProjectDao.select_by_id(repair_project_id)
        RepairOrderDao.update(update_repair_project.repair_order_id, None, None, None, None, None, None, None, None,
                              update_time)
        return db_commit(update_repair_project)

    # 输入：repair_order_id and start and page_size
    # 输出：查询维修项目 List<RepairProjectDao>
    # 功能：查询材料项目信息
    @staticmethod
    @logged
    def select(repair_order_id, start, page_size):
        return db_select(RepairProjectDao.select_by_repair_order_id(repair_order_id, start, page_size))

    # 输入：维修单id Int
    # 输出：
    # 功能：根据维修单id删除项目 包括RepairProject表
    @staticmethod
    @logged
    def delete_by_repair_id(repair_order_id):
        RepairProjectDao.delete_by_repair_order_id(repair_order_id)
        return db_commit(None)

    # 输入：项目id Int
    # 输出：项目对象 RepairProjectDao
    # 功能：通过id查询项目
    @staticmethod
    @logged
    def select_by_id(repair_project_id):
        return db_select(RepairProjectDao.select_by_id(repair_project_id))


class RepairOrderService:

    def __init__(self):
        pass

    # 输入：订单信息 Dict
    # 输出：订单对象 RepairOrderDao
    # 功能：订单插入数据库，repair_order表
    @staticmethod
    @logged
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

        return db_commit(new_repair_order)

    # 输入：订单id Int
    # 输出：
    # 功能：删除订单 包括repair_order表和repair_project表
    @staticmethod
    @logged
    def delete(repair_order_id):
        RepairOrderDao.delete(repair_order_id)
        RepairProjectDao.delete_by_repair_order_id(repair_order_id)
        return db_commit(None)

    # 输入：订单信息 Dict
    # 输出：订单对象 RepairOrderDao
    # 功能：订单更新数据库，repair_order表
    @staticmethod
    @logged
    def update(update_dict):
        update_time = datetime.now()

        repair_order_id = update_dict.get('repair_order_id')
        car_collector_name = update_dict.get('car_collector_name')
        dispatcher_name = update_dict.get('dispatcher_name')
        repair_money_total = update_dict.get('repair_money_total')
        repairman_name = update_dict.get('repairman_name')
        inspector_name = update_dict.get('inspector_name')
        repair_order_status = update_dict.get('repair_order_status')
        RepairOrderDao.update(repair_order_id, car_collector_name, dispatcher_name, None, repair_money_total,
                              repairman_name, inspector_name, repair_order_status, None, update_time)

        return db_commit(RepairOrderDao.select_by_id(repair_order_id))

    # 输入：start and page_size
    # 输出：订单对象列表 List<RepairOrderDao>
    # 功能：查询订单信息
    @staticmethod
    @logged
    def select(start, page_size):
        return db_select(RepairOrderDao.select(start, page_size))

    # 输入：订单id Int
    # 输出：订单对象 RepairOrderDao
    # 功能：通过id查询订单
    @staticmethod
    @logged
    def select_by_id(repair_order_id):
        return db_select(RepairOrderDao.select_by_id(repair_order_id))


class MaterialService:

    def __init__(self):
        pass

    # 输入：材料信息 Dict
    # 输出：材料对象 RepairMaterialDao
    # 功能：材料插入数据库 包括repair_material表
    @staticmethod
    @logged
    def insert(insert_dict):
        insert_time = datetime.now()

        repair_material_name = insert_dict.get('repair_material_name')
        repair_material_has_amount = insert_dict.get('repair_material_has_amount')
        new_material = RepairMaterialDao(repair_material_name, repair_material_has_amount, insert_time, insert_time)
        new_material.insert()

        return db_commit(new_material)

    # 输入：材料id Int
    # 输出：
    # 功能：删除材料信息 包括repair_material表
    @staticmethod
    @logged
    def delete(repair_material_id):
        RepairMaterialDao.delete(repair_material_id)
        return db_commit(None)

    # 输入：材料信息 Dict
    # 输出：材料对象 RepairMaterialDao
    # 功能：材料信息更新数据库 包括repair_material表
    @staticmethod
    @logged
    def update(update_dict):
        update_time = datetime.now()
        repair_material_id = update_dict.get('repair_material_id')
        repair_material_name = update_dict.get('repair_material_name')
        repair_material_has_amount = update_dict.get('repair_material_has_amount')
        RepairMaterialDao.update(repair_material_id, repair_material_name, repair_material_has_amount,
                                 None, update_time)
        return db_commit(RepairMaterialDao.select_by_id(repair_material_id))

    # 输入：start and page_size
    # 输出：材料对象列表 List<RepairMaterialDao>
    # 功能：查询材料信息
    @staticmethod
    @logged
    def select(start, page_size):
        return db_select(RepairMaterialDao.select(start, page_size))

    # 输入：材料id Int
    # 输出：材料对象 RepairMaterialDao
    # 功能：根据id查询材料
    @staticmethod
    @logged
    def select_by_id(repair_material_id):
        return db_select(RepairMaterialDao.select_by_id(repair_material_id))

    # 输入：材料名称 String
    # 输出：材料对象 RepairMaterialDao
    # 功能：根据材料名称查询材料
    @staticmethod
    @logged
    def select_by_name(repair_material_name):
        return db_select(RepairMaterialDao.select_by_name(repair_material_name))

    # 输入：订单id Int
    # 输出：订单对象 RepairOrderDao
    # 功能：订单材料出库更新数据库 包括repair_project表和repair_material表
    @staticmethod
    @logged
    def confirm(repair_order_id):
        update_time = datetime.now()

        repair_projects = RepairProjectDao.select_by_repair_order_id(repair_order_id, 0, -1).item_list

        for repair_project in repair_projects:
            if repair_project.repair_material_status is False:
                RepairProjectDao.update(repair_project.id, None, None, None, None, True, None, update_time)
                RepairMaterialDao.update_amount(repair_project.repair_material_id,
                                                -repair_project.repair_material_cost_amount, update_time)
        RepairOrderDao.update(repair_order_id, None, None, None, None, None, None, None, None, update_time)
        return db_commit(RepairOrderDao.select_by_id(repair_order_id))


class CarService:

    def __init__(self):
        pass

    # 输入：车辆信息 Dict
    # 输出：车辆对象 CarDao
    # 功能：车辆信息插入数据库 包括car表
    @staticmethod
    @logged
    def insert(insert_dict):
        insert_time = datetime.now()
        car_owner_id = insert_dict.get('car_owner_id')
        car_brand = insert_dict.get('car_brand')
        plate_number = insert_dict.get('plate_number')
        new_car = CarDao(car_owner_id, car_brand, plate_number, insert_time, insert_time)
        new_car.insert()
        CarOwnerDao.update(car_owner_id, None, None, None, insert_time)
        return db_commit(new_car)

    # 输入：车辆id列表 List<Int>
    # 输出：
    # 功能：批量删除车辆信息 包括car表
    @staticmethod
    @logged
    def delete(delete_list):
        for car_id in delete_list:
            CarDao.delete(car_id)
        return db_commit(None)

    # 输入：车辆信息 Dict
    # 输出：车辆对象 CarDao
    # 功能：车辆信息插入数据库 包括car表
    @staticmethod
    @logged
    def update(update_dict):
        update_time = datetime.now()
        plate_number = update_dict.get('plate_number')
        car_id = update_dict.get('car_id')
        car_brand = update_dict.get('car_brand')
        CarDao.update(car_id, None, car_brand, plate_number, None, update_time)
        update_car = CarDao.select_by_id(car_id)
        CarOwnerDao.update(update_car.car_owner_id, None, None, None, update_time)
        return db_commit(update_car)

    # 输入：car_owner_id and start and page_size
    # 输出：车辆信息列表 List<CarDao>
    # 功能：查询车辆信息
    @staticmethod
    @logged
    def select(car_owner_id, start, page_size):
        return db_select(CarDao.select_by_car_owner_id(car_owner_id, start, page_size))

    # 输入：车辆id Int
    # 输出：车辆对象 CarDao
    # 功能：通过id查询车辆
    @staticmethod
    @logged
    def select_by_id(car_id):
        return db_select(CarDao.select_by_id(car_id))

    # 输入：车辆plate_number String
    # 输出：车辆对象 CarDao
    # 功能：通过plate_number查询车辆
    @staticmethod
    @logged
    def select_by_plate_number(plate_number):
        return db_select(CarDao.select_by_plate_number(plate_number))


class CarOwnerService:

    def __init__(self):
        pass

    # 输入：车主信息 Dict
    # 输出：车主对象 CarOwnerDao
    # 功能：车主信息插入数据库 包括car_owner表
    @staticmethod
    @logged
    def insert(insert_dict):
        insert_time = datetime.now()
        car_owner_name = insert_dict.get('car_owner_name')
        car_owner_number = insert_dict.get('car_owner_number')
        new_car_owner = CarOwnerDao(car_owner_name, car_owner_number, insert_time, insert_time)
        new_car_owner.insert()

        return db_commit(new_car_owner)

    # 输入：车主id Int
    # 输出：
    # 功能：删除车主信息
    @staticmethod
    @logged
    def delete(car_owner_id):
        CarOwnerDao.delete(car_owner_id)
        CarDao.delete_by_car_owner_id(car_owner_id)
        return db_commit(None)

    # 输入：车主信息 Dict
    # 输出：车主对象 CarOwnerDao
    # 功能：车主信息更新数据库 包括car_owner表
    @staticmethod
    @logged
    def update(update_dict):
        update_time = datetime.now()
        car_owner_id = update_dict.get('car_owner_id')
        car_owner_name = update_dict.get('car_owner_name')
        car_owner_number = update_dict.get('car_owner_number')
        CarOwnerDao.update(car_owner_id, car_owner_name, car_owner_number, None, update_time)

        return db_commit(CarOwnerDao.select_by_id(car_owner_id))

    # 输入：start and page_size
    # 输出：车主信息列表 List<CarOwnerDao>
    # 功能：查询车主信息
    @staticmethod
    @logged
    def select(start, page_size):
        return db_select(CarOwnerDao.select(start, page_size))

    # 输入：车主id Int
    # 输出：车主对象 CarOwnerDao
    # 功能：通过id查询车主
    @staticmethod
    @logged
    def select_by_id(car_owner_id):
        return db_select(CarOwnerDao.select_by_id(car_owner_id))

    # 输入：车主car_owner_number String
    # 输出：车主对象 CarOwnerDao
    # 功能：通过car_owner_number查询车主
    @staticmethod
    @logged
    def select_by_car_owner_number(car_owner_number):
        return db_select(CarOwnerDao.select_by_car_owner_number(car_owner_number))


class Result:

    def __init__(self, status, message):
        self.status = status
        self.message = message

    def __repr__(self):
        return '{"status": "' + repr(self.status) + '", "message": "' + repr(self.message) + '"}'

    @property
    def serialize(self):
        result_dict = {"status": self.status}

        if type(self.message) in [RepairOrderDao, CarDao, CarOwnerDao, RepairProjectDao, RepairMaterialDao, PageItem]:
            # or isinstance(self.message, PageItem): if not inherit object in python 2
            result_dict["message"] = self.message.serialize
        else:
            result_dict["message"] = repr(self.message)

        return jsonify(result_dict)


def db_commit(return_obj):
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return Result(False, e)
    else:
        return Result(True, return_obj)


def db_select(return_obj):
    return Result(True, return_obj)


if __name__ == "__main__":
    old_repair_order = RepairOrderDao.select_by_id(2)
    result = RepairOrderDao.select(0, -1)
    # update_dict = dict()
    # update_dict['repair_order_id'] = 1
    # update_dict['car_id'] = 2
    # insert_dict = dict()
    # new_repair_order = RepairOrderService.update(update_dict)
    # test_repair_order = RepairOrderService.insert(insert_dict)
    print 'xxx'
