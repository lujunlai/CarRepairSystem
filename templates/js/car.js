var url = "http://127.0.0.1:5000/car";

var table = "<table id='table_info' class='bordered'><thead><tr><th>编号</th><th>车主编号</th><th>品牌</th><th>车牌号</th><th>创建时间</th><th>更新时间</th></tr></thead></table>";
var info_tr = "<tr><td>{0}</td><td onclick='get_car_owner_info({6})'><a>{1}</a></td><td>{2}</td><td>{3}</td><td>{4}</td><td>{5}</td></tr>";

$(document).ready(function(){
	if(car_owner_id != -1)
		select(now_page, page_size);
	else if(car_id != -1)
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
		page_size:page_size,
		car_owner_id:car_owner_id
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
		car_id:car_id
	},
	function(data){
		total = data_process(data, start, add_info_tr);
		}
	)
}

function add_info_tr(item, start){
	$("#table_info").append(info_tr.format(start, item.car_owner_id, item.plate_number, item.car_brand, item.create_time, item.update_time, item.car_owner_id));
}

function get_car_owner_info(car_owner_id){
	my_box('http://127.0.0.1:5000/carOwner?car_owner_id=' + car_owner_id);
}
