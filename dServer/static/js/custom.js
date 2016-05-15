   
	    
function memory_chart(memory) {

              $('.chart').easyPieChart({
                barColor: '#ef1e25',
                trackColor: '#e5e5e5',
                barColor: '#337AB7',
                scaleColor: false,
                
                lineCap: 'round',
                lineWidth: 12,
                size: 110,
                animate: 1000,
              });

              $('.chart').data('easyPieChart').update(memory);
              $('span', $('.chart')).text(memory);

}


function set_memory(machine, memory)
{
  
             memory_chart(memory.memory_percentage);
             var use = 'RAM Used '+memory.usages_memory+'/'+memory.total_memory+' GB';
             $('label', $('.chart')).text(use);
}


function set_disk(machine, disk)
{
    var tr="";
    var i=1;
    $.each(disk, function(key, value){
        tr +=           "<tr>";
        tr +=           "   <td>"+i+"</td>";
        tr +=           "   <td>"+key+"</td>";
        tr +=           "   <td>"+value.Size+"</td>";
        tr +=           "   <td>"+value.Used+"</td>";
        tr +=           "   <td>"+value.Available+"</td>";
        tr +=           "   <td>"+value.Use+"</td>";
        tr +=           "   <td>"+value.Filesystem+"</td>";
        tr +=           "</tr>";
        i  += 1;
    });
    $("#go").html(tr);
}


function reports()
{

	$.getJSON($SCRIPT_ROOT + "/get", {
	    node: $("#node").text(),
	    }, function(data) {
		$.each(data.report, function(i, report){
		    
		    $.each(this, function(key, value){
		        if (key == "memory")
		        {
		            set_memory(i, this);
		        }
		        else if (key == "disk")
		        {
		            set_disk(i, this);
		        }
		    
		});
		    
		});		
	});
}


$('a[data-toggle="tab"]').on('shown.bs.tab', function (e) {

   var node = '';
   if (typeof $(this).data('node-id') !== 'undefined') {
      node = $(this).data('node-id');
   }
   $("#node").text(node);
   $("#go").html('');
   
    window.setInterval(function()
    {
        reports(); 
    }, 
    1000);
    
})

$('.list-group-item').on('click',function(e){
    var previous = $(this).closest(".list-group").children(".active");
    previous.removeClass('active'); // previous list-item
    $(e.target).addClass('active'); // activated list-item
    
  });
  
$(document).ready(function()
{

            

});


