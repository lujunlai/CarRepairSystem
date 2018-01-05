var url = "http://127.0.0.1:5000/car";

var table = "<table id='table_info' class='bordered'><thead><tr><th>序号</th><th>车主编号</th><th>车牌号</th><th>品牌</th><th>创建时间</th><th>更新时间</th></tr></thead></table>";
var info_tr = "<tr><td>{0}</td><td onclick='get_car_owner_info({6})'><a>{1}</a></td><td>{2}</td><td>{3}</td><td>{4}</td><td>{5}</td></tr>";

$(document).ready(function(){
	ready();
})

function ready(){
	if(car_owner_id != -1)
		select(now_page, page_size);
	else if(car_id != -1)
		select_by_id();
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
		car_owner_id:car_owner_id
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
		plate_number:$("#plate_number").val(),
		car_brand:$("#car_brand").val(),
		car_owner_id:$("#car_owner_id").text(),
	},
	function(data){
		if (data.status == false)
			toastr.error(data.message);
		else{
			toastr.info('创建成功，车辆编号：' + data.message.id);
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
		car_id:$("#car_id").text(),
		plate_number:$("#plate_number").val(),
		car_brand:$("#car_brand").val(),
	},
	function(data){
		if (data.status == false)
			toastr.error(data.message);
		else{
			toastr.info('更新成功，车辆编号：' + data.message.id);
			only_box_close();
			ready();
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
		car_id:car_id
	},
	function(data){
		total = data_process(data, start, add_info_tr);
		}
	)
}

function select_by_plate_number_for_update(){
	$.getJSON(
	url + "/selectByPlateNumber", 
	{
		plate_number:$("#plate_number").val()
	},
	function(data){
		if (data.status == false)
			toastr.error(data.message);
		else{
			if(data.message == 'None')
				toastr.warning('车辆信息未登记!');
			else{
				var item = data.message;
				var check_ = '<div class="container xlarge"><table class="bordered">' + 
							 '<thead><tr><th>车辆编号</th><th>品牌</th><th>车牌号</th><th>操作</th></tr></thead>' + 
							 '<tr><td><a id="car_id">{0}</a></td><td><input id="car_brand" type="text" value="{1}"/></td><td><input id="plate_number" type="text" value="{2}"/></td><td><input type="button" value="确定" onclick="check_input(update_by_id)"/></td></tr>'+
							 '</table></div>';
	
				check_ = check_.format(item.id, item.car_brand, item.plate_number);
				fancy_box(check_);
			}
		}
		}
	)
}

function select_car_by_plate_number(){
	$.getJSON(
	url + "/selectByPlateNumber", 
	{
		plate_number:$("#plate_number").val()
	},
	function(data){
		if (data.status == false)
			toastr.error(data.message);
		else{
			if(data.message == 'None')
				toastr.warning('车辆信息未登记!');
			else
				toastr.info('车辆编号：' + data.message.id);
		}
		}
	)
}

function delete_by_plate_number(){
	$.post(
	url + '/deleteByPlateNumber',
	{
		plate_number:$("#plate_number").val()
	},
	function(data){
		if (data.status == false)
			toastr.error(data.message);
		else{
			toastr.info('删除成功，车牌号：' + $("#plate_number").val());
			only_box_close();
			ready();
		}
		}	
	)
}

function check(){
	var check_ = '<div class="container xlarge"><table class="bordered">' + 
		'<thead><tr><th>车主编号</th><th>车牌号</th><th>品牌</th><th>操作</th></tr></thead>' + 
		'<tr><td><a id="car_owner_id">'+ car_owner_id +
		'</a></td><td><input id="plate_number" type="text" /></td><td><input id="car_brand" type="text" /></td><td><input type="button" value="确定" onclick="check_input(insert)"/></td></tr>'+
		'</table></div>';
	
	fancy_box(check_);
}

function add_info_tr(item, start){
	$("#table_info").append(info_tr.format(start + '-' + item.id, item.car_owner_id, item.plate_number, item.car_brand, item.create_time, item.update_time, item.car_owner_id));
}

function get_car_owner_info(car_owner_id){
	my_box('http://127.0.0.1:5000/carOwner?car_owner_id=' + car_owner_id);
}

function redo(){
	var check_ = '<div class="container xlarge"><table class="bordered">' + 
		'<thead><tr><th>车牌号</th><th>操作</th></tr></thead>' + 
		'<tr><td><input id="plate_number" type="text" placeholder="请输入需要删除的车牌号"/><div id="suggestions-container"></div></td><td><input type="button" value="确定" onclick="check_input(delete_by_plate_number)"/></td></tr>'+
		'</table></div>';
	
	fancy_box(check_);
	
	get_suggestion_plate_number();
}

function update(){
	var check_ = '<div class="container xlarge"><table class="bordered">' + 
		'<thead><tr><th>车牌号</th><th>操作</th></tr></thead>' + 
		'<tr><td><input id="plate_number" type="text" placeholder="请输入需要更新的车牌号"/><div id="suggestions-container"></div></td><td><input type="button" value="确定" onclick="check_input(select_by_plate_number_for_update)"/></td></tr>'+
		'</table></div>';
	
	fancy_box(check_);
	
	get_suggestion_plate_number();
}

function search(){
	var check_ = '<div class="container xlarge"><table class="bordered">' + 
		'<thead><tr><th>车牌号</th><th>操作</th></tr></thead>' + 
		'<tr><td><input id="plate_number" type="text" placeholder="请输入需要查询的车牌号"/><div id="suggestions-container"></div></td><td><input type="button" value="确定" onclick="check_input(select_car_by_plate_number)"/></td></tr>'+
		'</table></div>';
	
	fancy_box(check_);
	
	get_suggestion_plate_number();
}

