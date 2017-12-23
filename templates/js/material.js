var url = "http://127.0.0.1:5000/material";

var table = '<table id="table_info" class="bordered"><thead><tr><th>编号</th><th>材料名称</th><th>余量</th><th>创建时间</th><th>更新时间</th></tr></thead></table>';
var info_tr = "<tr><td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td><td>{4}</td></tr>";

$(document).ready(function(){
	if (material_id == -1)
		select(now_page, page_size);
	else
		selectById();
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

function selectById(){
	init();
	now_page = 0;
	var start = 0;
	$.getJSON(
	url + "/selectById", 
	{
		material_id:material_id
	},
	function(data){
		total = data_process(data, start, add_info_tr);
		}
	)
}

function add_info_tr(item, start){
	$("#table_info").append(info_tr.format(start, item.repair_material_name, item.repair_material_has_amount, item.create_time, item.update_time));
}
