var url = "http://127.0.0.1:5000/repairProject";

var table = '<table id="table_info" class="bordered"><thead><tr><th>序号</th><th>材料编号</th><th>消耗数量</th><th>状态</th><th>说明</th><th>创建时间</th><th>更新时间</th></tr></thead></table>';
var info_tr = "<tr><td>{0}</td><td onclick='get_material_info({7})'><a>{1}</a></td><td>{2}</td><td>{3}</td><td>{4}</td><td>{5}</td><td>{6}</td></tr>";

$(document).ready(function(){
	ready();
})

function ready(){
	if(repair_order_id != -1)
		select(now_page, page_size);
	else{
		init();
		toastr.error("错误进入！请退出！");
	}
}

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

function select_by_name(){
	$.getJSON(
	"http://127.0.0.1:5000/material/selectByName", 
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
				check_insert(data.message.id);
		}
		}
	)
}

function select_by_id(){
	$.getJSON(
	url + "/selectById", 
	{
		repair_project_id:$("#repair_project_id").val()
	},
	function(data){
		if (data.status == false)
			toastr.error(data.message);
		else{
			if(data.message == 'None')
				toastr.warning('项目编号不存在!');
			else{
				var item = data.message;
				var check_ = '<div class="container xlarge"><table class="bordered">' + 
							 '<thead><tr><th>项目编号</th><th>项目说明</th><th>消耗数量</th><th>操作</th></tr></thead>' + 
							 '<tr><td><a id="repair_project_id">{0}</a></td><td><input id="repair_project_name" type="text" value="{1}"/></td><td><input id="repair_material_cost_amount" type="number" value="{2}"/></td><td><input type="button" value="确定" onclick="check_input(update_by_id)"/></td></tr>'+
							 '</table></div>';
				check_ = check_.format(item.id, item.repair_project_name, item.repair_material_cost_amount);
				fancy_box(check_);
			}
		}
		}
	)
}


function insert(){
	$.post(
	url + '/insert',
	{
		repair_project_name:$("#repair_project_name").val(),
		repair_order_id:$("#repair_order_id").text(),
		repair_material_id:$("#repair_material_id").text(),
		repair_material_cost_amount:$("#repair_material_cost_amount").val(),
	},
	function(data){
		if (data.status == false)
			toastr.error(data.message);
		else{
			toastr.info('创建成功，项目编号：' + data.message.id);
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
		repair_project_id:$("#repair_project_id").text(),
		repair_project_name:$("#repair_project_name").val(),
		repair_material_cost_amount:$("#repair_material_cost_amount").val(),
	},
	function(data){
		if (data.status == false)
			toastr.error(data.message);
		else{
			toastr.info('更新成功，项目编号：' + data.message.id);
			only_box_close();
			ready();
		}
		}	
	)
}

function delete_by_id(){
	$.post(
	url + '/delete',
	{
		delete_list:[$("#repair_project_id").val()]
	},
	function(data){
		if (data.status == false)
			toastr.error(data.message);
		else{
			toastr.info('删除成功，项目编号：' + $("#repair_project_id").val());
			only_box_close();
			ready();
		}
		}	
	)
}

function check(){
	var check_ = '<div class="container xlarge"><table class="bordered">' + 
		'<thead><tr><th>材料名称</th><th>操作</th></tr></thead>' + 
		'<tr><td><input id="repair_material_name" type="text" placeholder="请输入需要使用的材料"/></td><td><input type="button" value="确定" onclick="check_input(select_by_name)"/></td></tr>'+
		'</table></div>';
	
	fancy_box(check_);
}

function check_insert(repair_material_id){
	var insert_html = '<div class="container xlarge"><table class="bordered">' + 
		'<thead><tr><th>订单编号</th><th>材料编号</th><th>说明</th><th>消耗数量</th><th>操作</th></tr></thead>' + 
		'<tr><td><a id="repair_order_id">' + repair_order_id + 
		'</a></td><td><a id="repair_material_id">' + repair_material_id +
		'</a></td><td><input id="repair_project_name" type="text" /></td><td><input id="repair_material_cost_amount" type="number" /></td><td><input type="button" onclick="check_input(insert)" value="确定"/></td></tr>'+
		'</table></div>';
		
	fancy_box(insert_html);
}

function add_info_tr(item, start){
	if(item.repair_material_status == false)
		var repair_material_status = "未取用";
	else
		var repair_material_status = "已取用";
	$("#table_info").append(info_tr.format(start + '-' + item.id, item.repair_material_id, item.repair_material_cost_amount, repair_material_status, item.repair_project_name, item.create_time, item.update_time, item.repair_material_id));
}

function get_material_info(material_id){
	my_box('http://127.0.0.1:5000/material?material_id=' + material_id);
}

function redo(){
	var check_ = '<div class="container xlarge"><table class="bordered">' + 
		'<thead><tr><th>项目编号</th><th>操作</th></tr></thead>' + 
		'<tr><td><input id="repair_project_id" type="number" placeholder="请输入需要删除的项目编号"/></td><td><input type="button" value="确定" onclick="check_input(delete_by_id)"/></td></tr>'+
		'</table></div>';
	
	fancy_box(check_);
}

function update(){
	var check_ = '<div class="container xlarge"><table class="bordered">' + 
		'<thead><tr><th>项目编号</th><th>操作</th></tr></thead>' + 
		'<tr><td><input id="repair_project_id" type="number" placeholder="请输入需要更新的项目编号"/></td><td><input type="button" value="确定" onclick="check_input(select_by_id)"/></td></tr>'+
		'</table></div>';
	
	fancy_box(check_);
}
