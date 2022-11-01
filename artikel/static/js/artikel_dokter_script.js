$(document).ready(() => {
    $.get(window.location.href + "json/", function(data) {
        for (idx = 0; idx < data.length; idx++) {
            getData(data[idx]);
            detailArtikel(data[idx]);
            deleteData(data[idx]);
        }
    });

    $("#create-new-artikel").submit(function(event) {
        event.preventDefault();
        console.log("masuk")
        const form = $("#create-new-artikel")

        $.ajax({
            type: "POST",
            url: "create-new-artikel/",
            data: form.serialize(),
            headers: {
                'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')
            },
            success: function(data) {
                console.log("hore")
                getData(data);
                $("#title").val(""), $("#description").val(""), $("#photo").val("");
                const sectionCards = document.getElementById("artikel");
                console.log("berhaisl")
                sectionCards.insertAdjacentHTML("beforestart", $(`#${data.pk}-card`));
            },
        });

    });

    // $("#create-new-artikel").submit(function(event) {
    //     event.preventDefault();
    //     $.post(window.location.href + "create-new-artikel/", {
    //         image: $("#image").val(),
    //         title: $("#title").val(),
    //         description: $("#description").val(),
    //     }).done(function(data) {
    //         getData(data);
    //         $("#title").val(""), $("#description").val(""), $("#image").val("");
    //         const sectionCards = document.getElementById("artikel");
    //         sectionCards.insertAdjacentHTML("beforestart", $(`#${data.pk}-card`));
    //     });
    // });

    function getData(data) {
        $("#artikel").append(
            `
    <div id="${data.pk}-card" class="group relative rounded-lg cursor-pointer items-center justify-center overflow-hidden transition-shadow hover:shadow-xl hover:shadow-black/30">
      <div class="h-96 w-72">
          <img class="h-full w-full object-cover transition-transform duration-500 group-hover:rotate-3 group-hover:scale-125" src="${data.fields.photo}"
              alt="" />
      </div>
      <div class="absolute inset-0 bg-gradient-to-b from-transparent via-transparent to-black group-hover:from-black/70 group-hover:via-black/60 group-hover:to-black/70"></div>
      <div class="absolute inset-0 flex translate-y-[60%] flex-col items-center justify-center px-9 text-center transition-all duration-500 group-hover:translate-y-0">
          <h1 class="font-dmserif text-2xl font-bold text-white">${data.fields.title}</h1>
          <p class="mb-3 text-lg italic text-white opacity-0 transition-opacity duration-300 group-hover:opacity-100 text-ellipsis overflow-hidden">${data.fields.description}</p>
          <button id="${data.pk}-delete" class="rounded-full bg-neutral-900 py-2 px-3.5 font-com text-sm capitalize text-white shadow shadow-black/60">Delete</button>
      </div>
  </div>
        `
        );
    }

    function deleteData(data) {
        $(`#${data.pk}-delete`).click(function() {
            $.post(window.location.href + `delete-artikel/${data.pk}/`, {}).done(
                (res) => {
                    $(`#${data.pk}-card`).fadeOut();
                }
            );
        });
    }

    function detailArtikel(data) {
        $(`#${data.pk}-detail`).click(function() {
            $.get(window.location.href + `json/${data.pk}`, {}).done((res) => {
                console.log(res);
                console.log(res[0].fields.title);
                console.log(res[0].fields.title);
                $("#detail-artikel").html(
                    `
        <div id="${data.pk}-card" class="group relative rounded-lg cursor-pointer items-center justify-center overflow-hidden transition-shadow hover:shadow-xl hover:shadow-black/30">
          <div class="h-96 w-72">
              <img class="h-full w-full object-cover transition-transform duration-500 group-hover:rotate-3 group-hover:scale-125" src="${data.fields.photo}"
                  alt="" />
          </div>
          <div class="absolute inset-0 bg-gradient-to-b from-transparent via-transparent to-black group-hover:from-black/70 group-hover:via-black/60 group-hover:to-black/70"></div>
          <div class="absolute inset-0 flex translate-y-[60%] flex-col items-center justify-center px-9 text-center transition-all duration-500 group-hover:translate-y-0">
              <h1 class="font-dmserif text-3xl font-bold text-white">${data.fields.title}</h1>
              <p class="mb-3 text-lg italic text-white opacity-0 transition-opacity duration-300 group-hover:opacity-100">${data.fields.description}</p>
              <button id="${data.pk}-delete" class="rounded-full bg-neutral-900 py-2 px-3.5 font-com text-sm capitalize text-white shadow shadow-black/60">Delete</button>
          </div>
        
        </div>
        `
                );
            });
        });
    }

});