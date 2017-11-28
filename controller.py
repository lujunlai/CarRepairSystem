#   encoding=utf8


from service import app
from flask import request


class CollectorController:

    def __init__(self):
        pass

    # 传入：接车员姓名 string， 调度员姓名 string， 维修金额 float， 车辆牌照 string
    # 输出：维修单 id
    # insert
    @staticmethod
    @app.route('/collector/writeRepairOrder')
    def write_repair_order():
        print request.args
        return ''

    # 传入：维修单 id
    # 输出：维修单 id
    # update
    @staticmethod
    @app.route('/collector/confirmFinish')
    def confirm_finish():
        print request.args
        return ''

    # 传入：车主手机号 string
    # 输出：车主 id
    # select
    @staticmethod
    @app.route('/collector/checkCarOwner')
    def check_car_owner():
        print request.args
        return ''

    # 传入：车牌号 string
    # 输出：车 id
    # select
    @staticmethod
    @app.route('/collector/checkCar')
    def check_car():
        print request.args
        return ''

    # 传入：车主手机号 string， 车主姓名 string，
    # 输出：车主 id
    # insert
    @staticmethod
    @app.route('/collector/insertCarOwner')
    def insert_car_owner():
        print request.args
        return ''

    # 传入：车主 id， 车牌号 string， 车的牌子 string
    # 输出：车 id
    # insert
    @staticmethod
    @app.route('/collector/insertCar')
    def insert_car():
        print request.args
        return ''


class DispatcherController:

    def __init__(self):
        pass

    # 传入：维修员姓名 string， 质检员姓名 string
    # 输出：维修单 id
    # update
    @staticmethod
    @app.route('/dispatcher/chooseMan')
    def choose_man():
        print request.args
        return ''


class MaterialManagerController:

    def __init__(self):
        pass

    # 传入：材料 id list， 材料数量 int list
    # 输出：status
    # insert and update
    @staticmethod
    @app.route('/materialManager/manage')
    def manage():
        print request.args
        return ''

    # 传入：
    # 输出：
    @staticmethod
    @app.route('/materialManager/select')
    def select():
        print request.args
        return ''


class SystemMaintenancePersonnelController:

    def __init__(self):
        pass

    # 传入：
    # 输出：
    # select
    @staticmethod
    @app.route('/systemMaintenancePersonnel/selectRepairRecord')
    def select_repair_record():
        print request.args
        return ''

    # 传入：
    # 输出：
    # select
    @staticmethod
    @app.route('/systemMaintenancePersonnel/selectMaterialRecord')
    def select_material_record():
        print request.args
        return ''

    # 传入：
    # 输出：
    # select
    @staticmethod
    @app.route('/systemMaintenancePersonnel/selectCarOwnerRecord')
    def select_car_owner_record():
        print request.args
        return ''
