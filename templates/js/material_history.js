var url = "http://127.0.0.1:5000/repairMaterialHistory";

var table = "<table id='table_info' class='bordered'><thead><tr><th>序号</th><th>变化数量</th><th>说明</th><th>创建时间</th></tr></thead></table>";
var info_tr = "<tr><td>{0}</td><td><a>{1}</a></td><td>{2}</td><td>{3}</td></tr>";

$(document).ready(function(){
	ready();
})

function ready(){
	if(repair_material_name != "")
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
		repair_material_name:repair_material_name
	},
	function(data){
		total = data_process(data, start, add_info_tr);
		}
	)
}

function add_info_tr(item, start){
	$("#table_info").append(info_tr.format(start + '-' + item.id, item.change_amount, item.description, item.create_time));
}

