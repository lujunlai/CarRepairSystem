var url = "http://127.0.0.1:5000/repairProject";

var table = '<table id="table_info" class="bordered"><thead><tr><th>编号</th><th>材料编号</th><th>消耗数量</th><th>状态</th><th>说明</th><th>创建时间</th><th>更新时间</th></tr></thead></table>';
var info_tr = "<tr><td>{0}</td><td onclick='get_material_info({7})'><a>{1}</a></td><td>{2}</td><td>{3}</td><td>{4}</td><td>{5}</td><td>{6}</td></tr>";

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
		page_size:page_size,
		repair_order_id:repair_order_id
	},
	function(data){
		total = data_process(data, start, add_info_tr);
		}
	)
}

function add_info_tr(item, start){
	if(item.repair_material_status == false)
		var repair_material_status = "未取用";
	else
		var repair_material_status = "已取用";
	$("#table_info").append(info_tr.format(start, item.repair_material_id, item.repair_material_cost_amount, repair_material_status, item.repair_project_name, item.create_time, item.update_time, item.repair_material_id));
}

function get_material_info(material_id){
	my_box('http://127.0.0.1:5000/material?material_id=' + material_id);
}
