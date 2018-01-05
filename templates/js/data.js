jQuery.ajaxSettings.traditional = true;
toastr.options.closeButton = true;
toastr.options.timeOut = 1000;
var only_box = null;

var page_item = "<li onclick='select({0}, page_size)'><a></a></li>";
var select_page_item = "<li class='active'><a></a></li>";
var previous_page_item = "<li onclick='previous()'><a></a></li>";
var next_page_item = "<li onclick='next()'><a></a></li>";
var now_page = 0;
var page_size = 10;
var total = 0;

function data_process(data, start, data_process_function){
	if(data.status == false)
		toastr.error(data.message);
	else{
		
		if(!data.message.list){
			if(data.message == 'None')
				total = 0;
			else{
				total = 1;
				data_process_function(data.message, 1);
			}
		}
		else
			for(index in data.message.list){
				total = data.message.total;
				start = start + 1;
				data_process_function(data.message.list[index], start);
			}
		
		$("#page").append(previous_page_item);
		
		for(var i = 0; i <= total/page_size; i ++){
			if(i == now_page)
				$("#page").append(select_page_item);
			else
				$("#page").append(page_item.format(i));
		}
			
		$("#page").append(next_page_item);
	}
	return total;
}

function previous(){
	if(now_page > 0){
		now_page = now_page - 1;
		select(now_page, page_size);
	}
}

function next(){
	if(now_page < parseInt(total/page_size)){
		now_page = now_page + 1;
		select(now_page, page_size);
	}
}

function init(){
	$("#table_div").html(table);
	$("#page_div").html('<ul id="page"></ul>');
}

function my_box(url){
	$("#box_div").append('<a data-fancybox data-type="iframe" id="my_box" style="display:none;"><h id="click"></h></a>')
	$("#my_box").attr('data-src', url);
	$("#my_box").fancybox({
		afterClose:function(){ready();},
		iframe : {
			
			preload : false,
			css:{
				width:'100%',
				height:'100%'
			}
		}
	}
	);
	$("#click").click();
	$("#my_box").remove();
}

function fancy_box(content){
	only_box_close();
	only_box = $.fancybox.open(content);
}

function only_box_close(){
	if (only_box != null){
		only_box.close();
		only_box = null;
	}
}

function check_input(fuc){
	
	var result = true;
	$("input").each(function(){
		if ($(this).val() == "")
			result = false;
	});

	if(result)
		fuc();
	else{
		toastr.warning("输入框不准为空！");
	}
}

function home(){
	this.location.href = "/";
}

function get_suggestion_repair_material_name(){
	$('#repair_material_name').autocomplete({
    lookup: function (query, done) {
	$.getJSON(
	"/material/queryByName?repair_material_name=" + query,
	function(data){
		if (data.status == false)
			toastr.error(data.message);
		else{
			var list = new Array();
			for (index in data.message.list){
				list[index] = {"value": data.message.list[index].repair_material_name, "data": null};
			}
			var result = {
				suggestions: list
			};
			done(result);
		}
		}
	)
    },
	showNoSuggestionNotice: true,
	noSuggestionNotice: '库中没有此材料',
	appendTo: '#suggestions-container',
	});
}

function get_suggestion_plate_number(){
	$('#plate_number').autocomplete({
    lookup: function (query, done) {
	$.getJSON(
	"/car/queryByPlateNumber",
	{
		plate_number: query,
		car_owner_id: car_owner_id,
		car_id: car_id
	},
	function(data){
		if (data.status == false)
			toastr.error(data.message);
		else{
			if (car_id == -1){
				var list = new Array();
				for (index in data.message.list){
					list[index] = {"value": data.message.list[index].plate_number, "data": null};
				}
				var result = {
					suggestions: list
				};
				done(result);
			}
			else{
				var result = {
					suggestions: [{"value":data.message.plate_number, "data":null}]
				};
				done(result);
			}
		}
		}
	)
    },
	showNoSuggestionNotice: true,
	noSuggestionNotice: '车辆信息未登记',
	appendTo: '#suggestions-container',
	});
}