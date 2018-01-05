var url = "http://127.0.0.1:5000/material";

var table = '<table id="table_info" class="bordered"><thead><tr><th>序号</th><th>材料名称</th><th>余量</th><th>创建时间</th><th>更新时间</th></tr></thead></table>';
var info_tr = "<tr><td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td><td>{4}</td></tr>";

$(document).ready(function(){
	ready();
})

function ready(){
	if (material_id == -1)
		select(now_page, page_size);
	else
		select_by_id();
}

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

function insert(){
	$.post(
	url + '/insert',
	{
		repair_material_has_amount:$("#repair_material_has_amount").val(),
		repair_material_name:$("#repair_material_name").val(),
	},
	function(data){
		if (data.status == false)
			toastr.error(data.message);
		else{
			toastr.info('创建成功，材料编号：' + data.message.id);
			only_box_close();
			ready();
		}
		}	
	)
}

function update_by_id(){
	$.post(
	url + '/update',
	{
		repair_material_id:$("#repair_material_id").text(),
		repair_material_has_amount:$("#repair_material_has_amount").val(),
		repair_material_name:$("#repair_material_name").val(),
	},
	function(data){
		if (data.status == false)
			toastr.error(data.message);
		else{
			toastr.info('更新成功，材料编号：' + data.message.id);
			only_box_close();
			ready();
		}
		}	
	)
}

function select_by_name(){
	$.getJSON(
	url + "/selectByName", 
	{
		repair_material_name:$("#repair_material_name").val()
	},
	function(data){
		if (data.status == false)
			toastr.error(data.message);
		else{
			if(data.message == 'None')
				toastr.warning('库中没有此材料!');
			else
				toastr.info('材料编号：' + data.message.id + ' 库存：' + data.message.repair_material_has_amount);
		}
		}
	)
}

function confirm(){
	$.getJSON(
	url + '/confirm',
	{
		repair_order_id:$("#repair_order_id").val(),
	},
	function(data){
		if (data.status == false)
			toastr.error(data.message);
		else{
			if (data.message=="None")
				toastr.warning("订单不存在！");
			else{
				toastr.info('取用成功，订单编号：' + data.message.id);
				only_box_close();
				ready();
			}
		}
		}	
	)
}

function select_by_id(){
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

function select_by_name_for_update(){
	$.getJSON(
	url + "/selectByName", 
	{
		repair_material_name:$("#repair_material_name").val()
	},
	function(data){
		if (data.status == false)
			toastr.error(data.message);
		else{
			if(data.message == 'None')
				toastr.warning('库中没有此材料!');
			else{
				var item = data.message;
				var check_ = '<div class="container xlarge"><table class="bordered">' + 
							 '<thead><tr><th>材料编号</th><th>材料名称</th><th>变化数量</th><th>操作</th></tr></thead>' + 
							 '<tr><td><a id="repair_material_id">{0}</a></td><td><input id="repair_material_name" type="text" value="{1}"/></td><td><input id="repair_material_has_amount" type="number" placeholder="请输入变化的数量"/></td><td><input type="button" value="确定" onclick="check_input(update_by_id)"/></td></tr>'+
							 '</table></div>';
	
				check_ = check_.format(item.id, item.repair_material_name);
				fancy_box(check_);
			}
		}
		}
	)
}

function delete_by_name(){
	$.getJSON(
	url + '/deleteByName',
	{
		repair_material_name:$("#repair_material_name").val()
	},
	function(data){
		if (data.status == false)
			toastr.error(data.message);
		else{
			toastr.info('删除成功，材料名称：' + $("#repair_material_name").val());
			only_box_close();
			ready();
		}
		}	
	)
}

function check(){
	var check_ = '<div class="container xlarge"><table class="bordered">' + 
		'<thead><tr><th>材料名称</th><th>数量</th><th>操作</th></tr></thead>' + 
		'<tr><td><input id="repair_material_name" type="text" /></td><td><input id="repair_material_has_amount" type="number" /></td><td><input type="button" value="确定" onclick="check_input(insert)"/></td></tr>'+
		'</table></div>';
	
	fancy_box(check_);
}

function check_confirm(){
	var check_ = '<div class="container xlarge"><table class="bordered">' + 
		'<thead><tr><th>订单编号</th><th>操作</th></tr></thead>' + 
		'<tr><td><input id="repair_order_id" type="number" placeholder="请输入需要取材的订单编号"/></td><td><input type="button" value="确定" onclick="check_input(confirm)"/></td></tr>'+
		'</table></div>';
	
	fancy_box(check_);
}

function add_info_tr(item, start){
	$("#table_info").append(info_tr.format(start + '-' + item.id, item.repair_material_name, item.repair_material_has_amount, item.create_time, item.update_time));
}

function redo(){
	var check_ = '<div class="container xlarge"><table class="bordered">' + 
		'<thead><tr><th>材料名称</th><th>操作</th></tr></thead>' + 
		'<tr><td><input id="repair_material_name" type="text" placeholder="请输入需要删除的材料名称"/><div id="suggestions-container"></div></td><td><input type="button" value="确定" onclick="check_input(delete_by_name)"/></td></tr>'+
		'</table></div>';
	
	fancy_box(check_);
}

function update(){
	var check_ = '<div class="container xlarge"><table class="bordered">' + 
		'<thead><tr><th>材料名称</th><th>操作</th></tr></thead>' + 
		'<tr><td><input id="repair_material_name" type="text" placeholder="请输入需要更新的材料名称"/><div id="suggestions-container"></div></td><td><input type="button" value="确定" onclick="check_input(select_by_name_for_update)"/></td></tr>'+
		'</table></div>';
	
	fancy_box(check_);
}

function search(){
	var check_ = '<div class="container xlarge"><table class="bordered">' + 
		'<thead><tr><th>材料名称</th><th>操作</th></tr></thead>' + 
		'<tr><td><input id="repair_material_name" type="text" placeholder="请输入需要查询的材料名称"/><div id="suggestions-container"></div></td><td><input type="button" value="确定" onclick="check_input(select_by_name)"/></td></tr>'+
		'</table></div>';
	
	fancy_box(check_);
	
	get_suggestion_repair_material_name();
}
