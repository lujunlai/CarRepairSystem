toastr.options.closeButton = true;
toastr.options.timeOut = 1000;
toastr.info('您好！');

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
		iframe : {
			preload : false
		}
	}
	);
	$("#click").click();
	$("#my_box").remove();
}
