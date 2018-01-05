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
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.schema import CheckConstraint

app = Flask(__name__, static_url_path='', static_folder='')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///system.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


# RepairOrder class
class RepairOrderDao(db.Model):

    __tablename__ = 'repair_order'

    id = db.Column(db.Integer, primary_key=True)
    car_collector_name = db.Column(db.String(80), nullable=False)
    dispatcher_name = db.Column(db.String(80), nullable=False)
    repairman_name = db.Column(db.String(80), nullable=False)
    inspector_name = db.Column(db.String(80), nullable=False)
    car_id = db.Column(db.Integer, nullable=False)
    repair_money_total = db.Column(db.Float, nullable=False)
    repair_order_status = db.Column(db.Boolean, nullable=False)
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)
    is_delete = db.Column(db.Boolean, nullable=False)

    def __init__(self, car_collector_name, dispatcher_name, car_id, repair_money_total, repairman_name,
                 inspector_name, create_time, update_time):
        self.car_collector_name = car_collector_name
        self.dispatcher_name = dispatcher_name
        self.car_id = car_id
        self.repair_money_total = repair_money_total
        self.repair_order_status = False
        self.create_time = create_time
        self.repairman_name = repairman_name
        self.inspector_name = inspector_name
        self.update_time = update_time
        self.is_delete = False

    # 插入记录
    def insert(self):
        db.session.add(self)
        # db.session.commit()

    # 更新记录
    @staticmethod
    def update(repair_order_id, car_collector_name, dispatcher_name, car_id, repair_money_total,
               repairman_name, inspector_name, repair_order_status, create_time, update_time):
        update_dict = dict()
        if car_collector_name is not None:
            update_dict['car_collector_name'] = car_collector_name
        if dispatcher_name is not None:
            update_dict['dispatcher_name'] = dispatcher_name
        if car_id is not None:
            update_dict['car_id'] = car_id
        if repair_order_status is not None:
            update_dict['repair_order_status'] = repair_order_status
        if repair_money_total is not None:
            update_dict['repair_money_total'] = repair_money_total
        if create_time is not None:
            update_dict['create_time'] = create_time
        if repairman_name is not None:
            update_dict['repairman_name'] = repairman_name
        if inspector_name is not None:
            update_dict['inspector_name'] = inspector_name
        if update_time is not None:
            update_dict['update_time'] = update_time
        RepairOrderDao.query.filter_by(id=repair_order_id).update(update_dict)
        # db.session.commit()

    # 删除记录
    @staticmethod
    def delete(repair_order_id):
        update_dict = dict()
        update_dict['is_delete'] = True
        RepairOrderDao.query.filter_by(id=repair_order_id).update(update_dict)
        # db.session.commit()

    # 查询记录
    @staticmethod
    def select(start, page_size):
        return PageItem(RepairOrderDao.query.filter_by(is_delete=False).order_by(RepairOrderDao.update_time.desc()).
                        offset(start).limit(page_size).all(),
                        RepairOrderDao.query.filter_by(is_delete=False).count())

    # 通过repair_order_id查询
    @staticmethod
    def select_by_id(repair_order_id):
        return RepairOrderDao.query.filter_by(id=repair_order_id, is_delete=False).first()

    def __repr__(self):
        return '<RepairOrder %r>' % self.id

    @property
    def serialize(self):
        return {
            "id": self.id,
            "car_collector_name": self.car_collector_name,
            "dispatcher_name": self.dispatcher_name,
            "repairman_name": self.repairman_name,
            "inspector_name": self.inspector_name,
            "car_id": self.car_id,
            "repair_money_total": self.repair_money_total,
            "repair_order_status": self.repair_order_status,
            "create_time": self.create_time.strftime("%Y-%m-%d %H:%M:%S"),
            "update_time": self.update_time.strftime("%Y-%m-%d %H:%M:%S"),
        }


# CarOwner class
class CarOwnerDao(db.Model):

    __tablename__ = 'car_owner'

    id = db.Column(db.Integer, primary_key=True)
    car_owner_name = db.Column(db.String(80), nullable=False)
    car_owner_number = db.Column(db.String(80), unique=True, nullable=False)
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)
    is_delete = db.Column(db.Boolean, nullable=False)

    def __init__(self, car_owner_name, car_owner_number, create_time, update_time):
        self.car_owner_name = car_owner_name
        self.car_owner_number = car_owner_number
        self.create_time = create_time
        self.update_time = update_time
        self.is_delete = False

    # 插入记录
    def insert(self):
        db.session.add(self)
        # db.session.commit()

    # 更新记录
    @staticmethod
    def update(car_owner_id, car_owner_name, car_owner_number, create_time, update_time):
        update_dict = dict()
        if car_owner_name is not None:
            update_dict['car_owner_name'] = car_owner_name
        if car_owner_number is not None:
            update_dict['car_owner_number'] = car_owner_number
        if create_time is not None:
            update_dict['create_time'] = create_time
        if update_time is not None:
            update_dict['update_time'] = update_time
        CarOwnerDao.query.filter_by(id=car_owner_id).update(update_dict)
        # db.session.commit()

    # 删除记录
    @staticmethod
    def delete(car_owner_id):
        update_dict = dict()
        update_dict['is_delete'] = True
        CarOwnerDao.query.filter_by(id=car_owner_id).update(update_dict)
        # db.session.commit()

    # 查询记录
    @staticmethod
    def select(start, page_size):
        return PageItem(CarOwnerDao.query.filter_by(is_delete=False). order_by(CarOwnerDao.update_time.desc()).
                        offset(start).limit(page_size).all(),
                        CarOwnerDao.query.filter_by(is_delete=False).count())

    # 通过car_owner_id查询
    @staticmethod
    def select_by_id(car_owner_id):
        return CarOwnerDao.query.filter_by(id=car_owner_id, is_delete=False).first()

    # 通过car_owner_number查询
    @staticmethod
    def select_by_car_owner_number(car_owner_number):
        return CarOwnerDao.query.filter_by(car_owner_number=car_owner_number, is_delete=False).first()

    def __repr__(self):
        return '<CarOwner %r>' % self.id

    @property
    def serialize(self):
        return {
            "id": self.id,
            "car_owner_name": self.car_owner_name,
            "car_owner_number": self.car_owner_number,
            "create_time": self.create_time.strftime("%Y-%m-%d %H:%M:%S"),
            "update_time": self.update_time.strftime("%Y-%m-%d %H:%M:%S"),
        }


# Car class
class CarDao(db.Model):

    __tablename__ = 'car'

    id = db.Column(db.Integer, primary_key=True)
    car_owner_id = db.Column(db.Integer, nullable=False)
    car_brand = db.Column(db.String(80), nullable=False)
    plate_number = db.Column(db.String(80), unique=True, nullable=False)
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)
    is_delete = db.Column(db.Boolean, nullable=False)

    def __init__(self, car_owner_id, car_brand, plate_number, create_time, update_time):
        self.car_owner_id = car_owner_id
        self.car_brand = car_brand
        self.plate_number = plate_number
        self.create_time = create_time
        self.update_time = update_time
        self.is_delete = False

    # 插入记录
    def insert(self):
        db.session.add(self)
        # db.session.commit()

    # 更新记录
    @staticmethod
    def update(car_id, car_owner_id, car_brand, plate_number, create_time, update_time):
        update_dict = dict()
        if car_owner_id is not None:
            update_dict['car_owner_id'] = car_owner_id
        if car_brand is not None:
            update_dict['car_brand'] = car_brand
        if plate_number is not None:
            update_dict['plate_number'] = plate_number
        if create_time is not None:
            update_dict['create_time'] = create_time
        if update_time is not None:
            update_dict['update_time'] = update_time
            CarDao.query.filter_by(id=car_id).update(update_dict)
        # db.session.commit()

    # 删除记录
    @staticmethod
    def delete(plate_number):
        update_dict = dict()
        update_dict['is_delete'] = True
        CarDao.query.filter_by(plate_number=plate_number).update(update_dict)
        # db.session.commit()

    # 删除记录
    @staticmethod
    def delete_by_car_owner_id(car_owner_id):
        update_dict = dict()
        update_dict['is_delete'] = True
        CarDao.query.filter_by(car_owner_id=car_owner_id).update(update_dict)
        # db.session.commit()

    # 查询记录
    @staticmethod
    def select(start, page_size):
        return PageItem(CarDao.query.filter_by(is_delete=False).order_by(CarDao.update_time.desc())
                        .offset(start).limit(page_size).all(),
                        CarDao.query.filter_by(is_delete=False).count())

    # 通过car_id查询
    @staticmethod
    def select_by_id(car_id):
        return CarDao.query.filter_by(id=car_id, is_delete=False).first()

    # 通过plate_number查询
    @staticmethod
    def select_by_plate_number(plate_number):
        return CarDao.query.filter_by(plate_number=plate_number, is_delete=False).first()

    # 通过car_owner_id, plate_number模糊查询
    @staticmethod
    def query_by_plate_number(car_owner_id, plate_number):
        plate_number = '%' + plate_number + '%'
        return PageItem(CarDao.query.filter_by(car_owner_id=car_owner_id, is_delete=False)
                        .filter(CarDao.plate_number.like(plate_number)).all(),
                        CarDao.query.filter_by(car_owner_id=car_owner_id, is_delete=False)
                        .filter(CarDao.plate_number.like(plate_number)).count())

    # 通过car_owner_id查询
    @staticmethod
    def select_by_car_owner_id(car_owner_id, start, page_size):
        return PageItem(CarDao.query.filter_by(car_owner_id=car_owner_id, is_delete=False)
                        .order_by(CarDao.update_time.desc()).offset(start).limit(page_size).all(),
                        CarDao.query.filter_by(car_owner_id=car_owner_id, is_delete=False).count())

    def __repr__(self):
        return '<Car %r>' % self.id

    @property
    def serialize(self):
        return {
            "id": self.id,
            "car_owner_id": self.car_owner_id,
            "car_brand": self.car_brand,
            "plate_number": self.plate_number,
            "create_time": self.create_time.strftime("%Y-%m-%d %H:%M:%S"),
            "update_time": self.update_time.strftime("%Y-%m-%d %H:%M:%S"),
        }


# RepairProject class
class RepairProjectDao(db.Model):

    __tablename__ = 'repair_project'

    id = db.Column(db.Integer, primary_key=True)
    repair_project_name = db.Column(db.String(80), nullable=False)
    repair_material_id = db.Column(db.Integer, nullable=False)
    repair_order_id = db.Column(db.Integer, nullable=False)
    repair_material_cost_amount = db.Column(db.Integer, nullable=False)
    repair_material_status = db.Column(db.Boolean, nullable=False)
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)
    is_delete = db.Column(db.Boolean, nullable=False)

    def __init__(self, repair_project_name, repair_material_id, repair_order_id, repair_material_cost_amount,
                 create_time, update_time):
        self.repair_project_name = repair_project_name
        self.repair_material_id = repair_material_id
        self.repair_order_id = repair_order_id
        self.repair_material_cost_amount = repair_material_cost_amount
        self.repair_material_status = False
        self.create_time = create_time
        self.update_time = update_time
        self.is_delete = False

    # 插入记录
    def insert(self):
        db.session.add(self)
        # db.session.commit()

    # 更新记录
    @staticmethod
    def update(repair_project_id, repair_project_name, repair_material_id, repair_order_id, repair_material_cost_amount,
               repair_material_status, create_time, update_time):
        update_dict = dict()
        if repair_project_name is not None:
            update_dict['repair_project_name'] = repair_project_name
        if repair_material_id is not None:
            update_dict['repair_material_id'] = repair_material_id
        if repair_order_id is not None:
            update_dict['repair_order_id'] = repair_order_id
        if repair_material_cost_amount is not None:
            update_dict['repair_material_cost_amount'] = repair_material_cost_amount
        if repair_material_status is not None:
            update_dict['repair_material_status'] = repair_material_status
        if create_time is not None:
            update_dict['create_time'] = create_time
        if update_time is not None:
            update_dict['update_time'] = update_time
            RepairProjectDao.query.filter_by(id=repair_project_id).update(update_dict)
        # db.session.commit()

    # 删除记录
    @staticmethod
    def delete(repair_project_id):
        update_dict = dict()
        update_dict['is_delete'] = True
        RepairProjectDao.query.filter_by(id=repair_project_id).update(update_dict)
        # db.session.commit()

    # 删除记录
    @staticmethod
    def delete_by_repair_order_id(repair_order_id):
        update_dict = dict()
        update_dict['is_delete'] = True
        RepairProjectDao.query.filter_by(repair_order_id=repair_order_id).update(update_dict)
        # db.session.commit()

    # 查询记录
    @staticmethod
    def select(start, page_size):
        return PageItem(RepairProjectDao.query.filter_by(is_delete=False).order_by(RepairProjectDao.update_time.desc())
                        .offset(start).limit(page_size).all(),
                        RepairProjectDao.query.filter_by(is_delete=False).count())

    # 通过repair_project_id查询
    @staticmethod
    def select_by_id(repair_project_id):
        return RepairProjectDao.query.filter_by(id=repair_project_id, is_delete=False).first()

    # 通过repair_order_id查询
    @staticmethod
    def select_by_repair_order_id(repair_order_id, start, page_size):
        return PageItem(RepairProjectDao.query.filter_by(repair_order_id=repair_order_id, is_delete=False)
                        .order_by(RepairProjectDao.update_time.desc())
                        .offset(start).limit(page_size).all(),
                        RepairProjectDao.query.filter_by(repair_order_id=repair_order_id, is_delete=False).count())

    def __repr__(self):
        return '<RepairProject %r>' % self.id

    @property
    def serialize(self):
        return {
            "id": self.id,
            "repair_project_name": self.repair_project_name,
            "repair_material_id": self.repair_material_id,
            "repair_order_id": self.repair_order_id,
            "repair_material_cost_amount": self.repair_material_cost_amount,
            "repair_material_status": self.repair_material_status,
            "create_time": self.create_time.strftime("%Y-%m-%d %H:%M:%S"),
            "update_time": self.update_time.strftime("%Y-%m-%d %H:%M:%S"),
        }


# RepairMaterial class
class RepairMaterialDao(db.Model):

    __tablename__ = 'repair_material'

    id = db.Column(db.Integer, primary_key=True)
    repair_material_name = db.Column(db.String(80), unique=True, nullable=False)
    repair_material_has_amount = db.Column(db.Integer, CheckConstraint('repair_material_has_amount>0'), nullable=False)
    create_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)
    is_delete = db.Column(db.Boolean, nullable=False)

    def __init__(self, repair_material_name, repair_material_has_amount, create_time, update_time):
        self.repair_material_name = repair_material_name
        self.repair_material_has_amount = repair_material_has_amount
        self.create_time = create_time
        self.update_time = update_time
        self.is_delete = False

    # 插入记录
    def insert(self):
        db.session.add(self)
        # db.session.commit()

    # 更新记录
    @staticmethod
    def update(repair_material_id, repair_material_name, repair_material_has_amount, create_time, update_time):
        update_dict = dict()
        if repair_material_name is not None:
            update_dict['repair_material_name'] = repair_material_name
        if repair_material_has_amount is not None:
            update_dict['repair_material_has_amount'] = RepairMaterialDao.repair_material_has_amount + \
                                                        repair_material_has_amount
        if create_time is not None:
            update_dict['create_time'] = create_time
        if update_time is not None:
            update_dict['update_time'] = update_time
            RepairMaterialDao.query.filter_by(id=repair_material_id).update(update_dict)
        # db.session.commit()

    # 修改数量
    @staticmethod
    def update_amount(repair_material_id, change_number, update_time):
        repair_material = RepairMaterialDao.query.filter_by(id=repair_material_id).first()
        repair_material.repair_material_has_amount = repair_material.repair_material_has_amount + change_number
        repair_material.update_time = update_time

    # 删除记录
    @staticmethod
    def delete(repair_material_name):
        update_dict = dict()
        update_dict['is_delete'] = True
        RepairMaterialDao.query.filter_by(repair_material_name=repair_material_name).update(update_dict)
        # db.session.commit()

    # 查询记录
    @staticmethod
    def select(start, page_size):
        return PageItem(RepairMaterialDao.query.filter_by(is_delete=False)
                        .order_by(RepairMaterialDao.update_time.desc()).offset(start).limit(page_size).all(),
                        RepairMaterialDao.query.filter_by(is_delete=False).count())

    # 通过repair_material_id查询
    @staticmethod
    def select_by_id(repair_material_id):
        return RepairMaterialDao.query.filter_by(id=repair_material_id, is_delete=False).first()

    # 通过repair_material_name查询
    @staticmethod
    def select_by_name(repair_material_name):
        return RepairMaterialDao.query.filter_by(repair_material_name=repair_material_name, is_delete=False).first()

    # 通过repair_material_name模糊查询
    @staticmethod
    def query_by_name(repair_material_name):
        repair_material_name = '%' + repair_material_name + '%'
        return PageItem(RepairMaterialDao.query.filter(RepairMaterialDao.repair_material_name.
                                                       like(repair_material_name)).filter_by(is_delete=False).all(),
                        RepairMaterialDao.query.filter(RepairMaterialDao.repair_material_name.like(repair_material_name)
                                                       ).filter_by(is_delete=False).count())

    def __repr__(self):
        return '<RepairMaterial %r>' % self.id

    @property
    def serialize(self):
        return {
            "id": self.id,
            "repair_material_name": self.repair_material_name,
            "repair_material_has_amount": self.repair_material_has_amount,
            "create_time": self.create_time.strftime("%Y-%m-%d %H:%M:%S"),
            "update_time": self.update_time.strftime("%Y-%m-%d %H:%M:%S"),
        }


class PageItem(object):

    def __init__(self, item_list, total):
        self.item_list = item_list
        self.total = total

    @property
    def serialize(self):
        item_list = list()
        for item in self.item_list:
            item_list.append(item.serialize)

        return {
            "list": item_list,
            "total": self.total
        }

    def __repr__(self):
        return repr({"list": self.item_list, "total": self.total})


db.create_all()

if __name__ == "__main__":
    now = datetime.now()
    # repair_order_test = RepairOrderDao('car_collector_name', 'dispatcher_name', 1, 1,
    #                                    'repairman_name', 'inspector_name', datetime.now(), datetime.now())
    # repair_order_test.insert()
    # repair_order = RepairOrderDao.select_by_id(1)
    # repair_material_test = RepairMaterialDao('repair_material_name', -1, now, now)
    # repair_material_test.insert()
    # db.session.commit()
    print 'xxx'
