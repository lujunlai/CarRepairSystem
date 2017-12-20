#   encoding=utf8
# dao 数据库操作
# 接车员 car_collector
# 调度员 dispatcher
# 维修员 repairman
# 质检员 inspector
# 材料管理员 material_manager
# 系统维护人员 system_maintenance_personnel
# 车主 car_owner
# 维修项目 repair_project
# 维修材料 repair_material


from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_url_path='', static_folder='')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///system.db'

db = SQLAlchemy(app)


# RepairOrder class
class RepairOrderDao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    car_collector_name = db.Column(db.String(80))
    dispatcher_name = db.Column(db.String(80))
    repairman_name = db.Column(db.String(80))
    inspector_name = db.Column(db.String(80))
    car_id = db.Column(db.Integer)
    repair_money_total = db.Column(db.Float)
    repair_start_time = db.Column(db.DateTime)
    repair_end_time = db.Column(db.DateTime)
    is_delete = db.Column(db.Boolean)

    # 插入记录
    def __init__(self, car_collector_name, dispatcher_name, car_id, repair_money_total, repair_start_time,
                 repairman_name, inspector_name, repair_end_time):
        self.car_collector_name = car_collector_name
        self.dispatcher_name = dispatcher_name
        self.car_id = car_id
        self.repair_money_total = repair_money_total
        self.repair_start_time = repair_start_time
        self.repairman_name = repairman_name
        self.inspector_name = inspector_name
        self.repair_end_time = repair_end_time
        self.is_delete = False
        db.session.add(self)
        db.session.commit()

    # 更新记录
    @staticmethod
    def update(repair_order_id, car_collector_name, dispatcher_name, car_id, repair_money_total, repair_start_time,
               repairman_name, inspector_name, repair_end_time):
        update_dict = dict()
        if car_collector_name is not None:
            update_dict['car_collector_name'] = car_collector_name
        if dispatcher_name is not None:
            update_dict['dispatcher_name'] = dispatcher_name
        if car_id is not None:
            update_dict['car_id'] = car_id
        if repair_money_total is not None:
            update_dict['repair_money_total'] = repair_money_total
        if repair_start_time is not None:
            update_dict['repair_start_time'] = repair_start_time
        if repairman_name is not None:
            update_dict['repairman_name'] = repairman_name
        if inspector_name is not None:
            update_dict['inspector_name'] = inspector_name
        if repair_end_time is not None:
            update_dict['repair_end_time'] = repair_end_time
        RepairOrderDao.query.filter_by(id=repair_order_id).update(update_dict)
        db.session.commit()

    # 删除记录
    def delete(self):
        update_dict = dict()
        update_dict['is_delete'] = True
        RepairOrderDao.query.filter_by(id=self.id).update(update_dict)
        db.session.commit()

    # 查询记录
    @staticmethod
    def select():
        return RepairOrderDao.query.all()

    # 通过id查询
    @staticmethod
    def select_by_id(repair_order_id):
        return RepairOrderDao.query.filter_by(id=repair_order_id)

    def __repr__(self):
        return '<RepairOrder %r>' % self.id


# CarOwner class
class CarOwnerDao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    car_owner_name = db.Column(db.String(80))
    car_owner_number = db.Column(db.String(80), unique=True)
    is_delete = db.Column(db.Boolean)

    def __init__(self, car_owner_name, car_owner_number):
        self.car_owner_name = car_owner_name
        self.car_owner_number = car_owner_number
        self.is_delete = False

    def __repr__(self):
        return '<CarOwner %r>' % self.id


# Car class
class CarDao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    car_owner_id = db.Column(db.Integer)
    car_brand = db.Column(db.String(80))
    plate_number = db.Column(db.String(80), unique=True)
    is_delete = db.Column(db.Boolean)

    def __repr__(self):
        return '<Car %r>' % self.id


# RepairProject class
class RepairProjectDao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    repair_project_name = db.Column(db.String(80))
    repair_material_id = db.Column(db.Integer)
    repair_order_id = db.Column(db.Integer)
    repair_material_cost_amount = db.Column(db.Integer)
    repair_material_status = db.Column(db.Boolean)
    is_delete = db.Column(db.Boolean)

    def __repr__(self):
        return '<RepairProject %r>' % self.id


# RepairMaterial class
class RepairMaterialDao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    repair_material_name = db.Column(db.String(80))
    repair_material_has_amount = db.Column(db.Integer)
    is_delete = db.Column(db.Boolean)

    def __repr__(self):
        return '<RepairMaterial %r>' % self.id


db.create_all()
