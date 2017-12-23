var url = "http://127.0.0.1:5000/repairOrder";

var table = '<table id="table_info" class="bordered"><thead><tr><th>编号</th><th>车辆编号</th><th>金额</th><th>状态</th><th>接车员</th><th>派工员</th><th>维修员</th><th>质检员</th><th>创建时间</th><th>更新时间</th><th>项目</th></tr></thead></table>';
var info_tr = "<tr><td>{0}</td><td onclick='get_car_info({11})'><a>{1}</a></td><td>{2}</td><td>{3}</td><td>{4}</td><td>{5}</td><td>{6}</td><td>{7}</td><td>{8}</td><td>{9}</td><td onclick='get_project_info({10})'><a>查看</a></td></tr>";

$(document).ready(function(){
	select(now_page, page_size);
})

function select(page, page_size){
	init();
	now_page = page;
	var start = page*page_size;
	$.getJSON(
	url + "/select", 
	{
		start:start,
		page_size:page_size
	},
	function(data){
		total = data_process(data, start, add_info_tr);
		}
	)
}

function add_info_tr(item, start){
	if(item.repair_order_status == false)
		var repair_order_status = "未完成";
	else
		var repair_order_status = "已完成";
	$("#table_info").append(info_tr.format(start, item.car_id, item.repair_money_total, repair_order_status, item.car_collector_name, item.dispatcher_name, item.repairman_name,
	item.inspector_name, item.create_time, item.update_time, item.id, item.car_id));
}

function get_car_info(car_id){
	my_box('http://127.0.0.1:5000/car?car_id=' + car_id);
}

function get_project_info(repair_order_id){
	my_box('http://127.0.0.1:5000/repairProject?repair_order_id=' + repair_order_id);
}

