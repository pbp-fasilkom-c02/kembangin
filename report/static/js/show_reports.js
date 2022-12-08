$(document).ready(function(){
  $.get("/report-progress/json", function(data) {
    for (i=0; i < data.length; i++){
      $("#card-row").append(`
      <div class="card-col col">
        <div class="card shadow-xl m-auto h-100 duration-300 hover:scale-105" id="report-${data[i].pk}">
          <div class="card-body">
            <div class="grid grid-cols-6 gap-7 content-start">
              <div class="col-span-5"><h1 class="card-title font-bold text-red-500 text-xl">${data[i].name} (${data[i].age})</h1></div>
            <div>
              <button onclick="deleteReport(${data[i].pk})" class="button"  style="float:right;">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                <path stroke-linecap="round" stroke-linejoin="round" d="M14.74 9l-.346 9m-4.788 0L9.26 9m9.968-3.21c.342.052.682.107 1.022.166m-1.022-.165L18.16 19.673a2.25 2.25 0 01-2.244 2.077H8.084a2.25 2.25 0 01-2.244-2.077L4.772 5.79m14.456 0a48.108 48.108 0 00-3.478-.397m-12 .562c.34-.059.68-.114 1.022-.165m0 0a48.11 48.11 0 013.478-.397m7.5 0v-.916c0-1.18-.91-2.164-2.09-2.201a51.964 51.964 0 00-3.32 0c-1.18.037-2.09 1.022-2.09 2.201v.916m7.5 0a48.667 48.667 0 00-7.5 0" />
                </svg>
              </button>                
            </div>
            </div>                
            <h6 class="card-subtitle mb-2 text-gray-400">Dibuat pada ${data[i].date}</h6>
            <p class="card-text font-normal">‣ Tinggi badan: ${data[i].height}</p>
            <p class="card-text font-normal">‣ Berat badan: ${data[i].weight}</p>
            <p class="card-text font-normal">‣ Tingkat makan: ${data[i].eat}</p>
            <p class="card-text font-normal">‣ Tingkat minum: ${data[i].drink}</p>
            <p class="card-text font-normal">‣ Perkembangan: ${data[i].progress}</p>                        
          </div> 
        </div>
      </div>
    `)
    }
  });

  $("#add-button").click(function(){
    const name = $("#report-name").val()
    const age = $("#report-age").val()
    const height = $("#report-height").val()
    const weight = $("#report-weight").val()
    const eat = $("#report-eat").val()
    const drink = $("#report-drink").val()
    const progress = $("#report-progress").val()
    const report = {name:name, age:age, height:height, weight:weight, eat:eat, drink:drink, progress:progress,csrfmiddlewaretoken:'{{ csrf_token }}'}
    $.ajax({url:"/report-progress/add-report/", data:report, method:"POST"}).done(function (add) {
      $("#card-row").append(`
      <div class="card-col col">
        <div class="card shadow-xl m-auto h-100 duration-300 hover:scale-105" id="report-${add.pk}">
          <div class="card-body">
            <div class="grid grid-cols-6 gap-7 content-start">
              <div class="col-span-5"><h1 class="card-title font-bold text-red-500 text-xl">${add.name} (${add.age})</h1></div>
            <div>
              <button onclick="deleteReport(${add.pk})" class="button" style="float:right;">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                <path stroke-linecap="round" stroke-linejoin="round" d="M14.74 9l-.346 9m-4.788 0L9.26 9m9.968-3.21c.342.052.682.107 1.022.166m-1.022-.165L18.16 19.673a2.25 2.25 0 01-2.244 2.077H8.084a2.25 2.25 0 01-2.244-2.077L4.772 5.79m14.456 0a48.108 48.108 0 00-3.478-.397m-12 .562c.34-.059.68-.114 1.022-.165m0 0a48.11 48.11 0 013.478-.397m7.5 0v-.916c0-1.18-.91-2.164-2.09-2.201a51.964 51.964 0 00-3.32 0c-1.18.037-2.09 1.022-2.09 2.201v.916m7.5 0a48.667 48.667 0 00-7.5 0" />
                </svg>
              </button>                
            </div>
            </div>                
            <h6 class="card-subtitle mb-2 text-gray-400">Dibuat pada ${add.date}</h6>
            <p class="card-text font-normal">‣ Tinggi badan: ${add.height}</p>
            <p class="card-text font-normal">‣ Berat badan: ${add.weight}</p>
            <p class="card-text font-normal">‣ Tingkat makan: ${add.eat}</p>
            <p class="card-text font-normal">‣ Tingkat minum: ${add.drink}</p>
            <p class="card-text font-normal">‣ Perkembangan: ${add.progress}</p>                        
          </div> 
        </div>
      </div>
      `)
    })
    $('#reportModal').on('hidden.bs.modal', function () {
      $('#reportModal form')[0].reset();
    });
  });
});
var deleteReport = function(pk) {
    $.ajax({
        type: "DELETE",
        headers: { "X-CSRFToken": document.getElementsByName("csrfmiddlewaretoken")[0].value},
        url: "/report-progress/delete-report/1".replace(1, pk),
        encode: true,
    }).done(function (data) {
        document.getElementById(`report-${pk}`).remove();
    })
};