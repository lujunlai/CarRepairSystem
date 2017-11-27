# encoding=uft8


from dao import app, RepairOrderDao


# 用于管理
class RepairOrderService():
    repair_order_dao = RepairOrderDao()

    def __init__(self):
        pass

    # 接车员接到车主时，未注册先注册，注册完进行初始化订单操作
    # 涉及内容，接车员名字，调度员名字， 车辆id， 维修费用， 维修开始时间
    def collector(self, car_collector_name, dispatcher_name, car_id, repair_money_total, repair_start_time):
        self.repair_order_dao.collector(car_collector_name, dispatcher_name, car_id, repair_money_total,
                                        repair_start_time)

    # 调度员接到任务后进行维修派工和质检派工
    # 涉及内容， 维修员名字， 质检员名字
    def dispatcher(self, repairman_name, inspector_name):
        self.repairman_name = repairman_name
        self.inspector_name = inspector_name

    # 质检完成后打上维修结束时间
    # 涉及内容， 维修结束时间
    def finish(self, repair_end_time):
        self.repair_end_time = repair_end_time


class SelectService():

    def __init__(self):
        pass
