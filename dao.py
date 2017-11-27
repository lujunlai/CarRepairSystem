#   encoding=utf8
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
class RepairOrder(db.Model):
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

    # 接车员接到车主时，未注册先注册，注册完进行初始化订单操作
    # 涉及内容，接车员名字，调度员名字， 车辆id， 维修费用， 维修开始时间
    def __init__(self, car_collector_name, dispatcher_name, car_id, repair_money_total, repair_start_time):
        self.car_collector_name = car_collector_name
        self.dispatcher_name = dispatcher_name
        self.car_id = car_id
        self.repair_money_total = repair_money_total
        self.repair_start_time = repair_start_time
        self.is_delete = False

    # 调度员接到任务后进行维修派工和质检派工
    # 涉及内容， 维修员名字， 质检员名字
    def dispatcher(self, repairman_name, inspector_name):
        self.repairman_name = repairman_name
        self.inspector_name = inspector_name

    # 质检完成后打上维修结束时间
    # 涉及内容， 维修结束时间
    def finish(self, repair_end_time):
        self.repair_end_time = repair_end_time
        db.session.add(self)
        db.session.commit()

    # 删除记录
    def delete(self):
        RepairOrder.query.filter_by(id=self.id).update({'is_delete': True})
        db.session.commit()


    def __repr__(self):
        return '<RepairOrder %r>' % self.id


# CarOwner class
class CarOwner(db.Model):
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
class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    car_owner_id = db.Column(db.Integer)
    car_brand = db.Column(db.String(80))
    plate_number = db.Column(db.String(80), unique=True)
    is_delete = db.Column(db.Boolean)

    def __repr__(self):
        return '<Car %r>' % self.id


# RepairProject class
class RepairProject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    repair_material_id = db.Column(db.Integer)
    repair_order_id = db.Column(db.Integer)
    repair_material_cost_amount = db.Column(db.Integer)
    is_delete = db.Column(db.Boolean)

    def __repr__(self):
        return '<RepairProject %r>' % self.id


# RepairMaterial class
class RepairMaterial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    repair_material_name = db.Column(db.String(80))
    repair_material_has_amount = db.Column(db.Integer)
    is_delete = db.Column(db.Boolean)

    def __repr__(self):
        return '<RepairMaterial %r>' % self.id


db.create_all()

