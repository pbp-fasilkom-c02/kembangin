$(document).ready(() => {
    $.ajax({
        type: "GET",
        url: "json/",
        dataType: "json",
        success: function(data) {
            for (idx = 0; idx < data.length; idx++) {
                getData(data[idx]);
                detailArtikel(data[idx]);
                upVote(data[idx]);
                downVote(data[idx]);
                getComment(data[idx]);
            }
        },
    });

    $.ajax({
        type: "GET",
        url: "comment/json/",
        dataType: "json",
        success: function(data) {
            for (idx = 0; idx < data.length; idx++) {
                getExp(data[idx])
            }
        },
    });

    $("#share-exp").submit(function(event) {
        event.preventDefault();
        const form = $("#share-exp")

        $.ajax({
            type: "POST",
            url: "share-exp/",
            data: form.serialize(),
            headers: {
                'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')
            },
            success: function(data) {
                getExp(data);
                const sectionCards = document.getElementById("posting");
                sectionCards.insertAdjacentHTML("beforestart", $(`#${data.pk}-posting-exp`));
            },
        });

    });

    function getExp(data) {
        $("#posting").append(
            `
        <div id="${data.pk}-posting-exp" class="flex border-solid border-2 mx-auto items-center justify-center shadow-lg mx-8 mb-4 ">
          <div class="w-full bg-white rounded-lg px-4 pt-2">
             <div class="flex flex-wrap -mx-3 mb-6">
                <h2 class="px-4 pt-3 pb-2 text-gray-800 text-lg">Experience</h2>
                <div class="w-full md:w-full px-3 mb-2 mt-2">
                   <p>${data.fields.comment}</p>
                </div>
             </div>
          </div>
        </div>
        `
        )
    }


    function getData(data) {
        $("#post-comments").submit(function(event) {
            event.preventDefault();
            const form = $("#post-comments")

            $.ajax({
                type: "POST",
                url: `post-comment/${data.pk}`,
                data: form.serialize(),
                success: function(data) {
                    form.trigger("reset");
                    getComment(data);
                    $("#comment-area").val("");
                    const sectionCards = document.getElementById("comment");
                    sectionCards.insertAdjacentHTML(
                        "beforestart",
                        $(`#${data.pk}-comment-card`)
                    );
                },
            });

        });

        $("#artikel").append(
            `
             <div>
                <div id="${data.pk}-card" class="group relative rounded-lg cursor-pointer items-center justify-center overflow-hidden transition-shadow hover:shadow-xl hover:shadow-black/30">
                    <div class="lg:h-96 lg:w-[600px]">
                        <img class="h-full w-full object-cover transition-transform duration-500 group-hover:rotate-3 group-hover:scale-125" src="${data.fields.photo}"
                            alt="" />
                    </div>
                    <div class="absolute inset-0 bg-gradient-to-b from-transparent via-transparent to-black group-hover:from-black/70 group-hover:via-black/60 group-hover:to-black/70"></div>
                    <div class="absolute inset-0 flex translate-y-[20%] flex-col items-center justify-center px-9 text-center transition-all duration-500 group-hover:translate-y-0">
                        <h1 class="font-dmserif text-3xl font-bold text-black  text-clip overflow-hidden group-hover:text-white">${data.fields.title}</h1>
                        <p class="mb-3 text-lg italic text-white opacity-0 transition-opacity duration-300 group-hover:opacity-100 text-clip overflow-hidden">${data.fields.description}</p>
                        <button id="${data.pk}-detail" class="bg-pink-500 text-white active:bg-pink-600 font-bold uppercase text-sm px-6 py-3 rounded shadow hover:shadow-lg outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150" type="button" onclick="toggleModal('modal-id')">
                          Detail
                        </button>
                        <div class="flex">
                          <div class="flex text-white text-xl gap-2 m-5">
                            <p id="${data.pk}-upp">${data.fields.upvote}</p>
                            <button id="${data.pk}-upvote">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                          <path stroke-linecap="round" stroke-linejoin="round" d="M15 11.25l-3-3m0 0l-3 3m3-3v7.5M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                            </button>
                          </svg>
                          </div>
                          <div class="flex text-white text-xl gap-2 m-5">
                            <p id="${data.pk}-downn">${data.fields.downvote}</p>
                            <button id="${data.pk}-downvote">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                               <path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75l3 3m0 0l3-3m-3 3v-7.5M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                            </svg>
                           </button>
                          </div>
                        </div>
                    </div>                    
                </div>
            </div>
            `
        );
    }

    function getComment(data) {
        $("#comment").html(
            `<a id="${data.pk}-comment-card" class="group block max-w-xs mx-auto rounded-lg p-6 bg-white ring-1 ring-slate-900/5 shadow-lg space-y-3 hover:bg-sky-500 hover:ring-sky-500">
          <div class="flex items-center space-x-3">
            <svg class="h-6 w-6 stroke-sky-500 group-hover:stroke-white" fill="none" viewBox="0 0 24 24"><!-- ... --></svg>
            <h3 class="text-slate-900 group-hover:text-white text-sm font-semibold">New project</h3>
          </div>
          <p class="text-slate-500 group-hover:text-white text-sm">${data.fields.comment}</p>
        </a>
        `
        );
    }

    function detailArtikel(data) {
        $(`#${data.pk}-detail`).click(function() {
            $.get(window.location.href + `json/${data.pk}`, {}).done((res) => {
                $("#detail-artikel").html(
                    `
                        <div id="${res[0].pk}-card" class="relative flex-auto"></div>
                            <div class="group relative rounded-lg cursor-pointer items-center justify-center overflow-hidden transition-shadow hover:shadow-xl hover:shadow-black/30">
                                <div class="h-96 w-[700px]">
                                <img class="h-full w-full object-cover" src="${res[0].fields.photo}"
                                    alt="" />
                            </div>
                            <div class="absolute inset-0 bg-gradient-to-b from-transparent via-transparent to-black"></div>
                                               
                            </div>
                            </div>
                            <h1 class="text-center font-dmserif text-3xl font-bold text-black ">${res[0].fields.title}</h1>
                            <p class="text-center mb-3 text-lg italic text-black transition-opacity duration-300 group-hover:opacity-100">${res[0].fields.description}</p>
                        </div>
            `
                );
            });
        });
    }

    const upVote = (data) => {
        $(`#${data.pk}-upvote`).click(function() {
            $.post(window.location.href + `${data.pk}/vote/up`, {}).done((res) => {
                $(`#${data.pk}-upp`).text(res.upvote);
            });
        });
    };

    const downVote = (data) => {
        $(`#${data.pk}-downvote`).click(function() {
            $.post(window.location.href + `${data.pk}/vote/down`, {}).done(
                (res) => {
                    $(`#${data.pk}-downn`).text(res.downvote);
                }
            );
        });
    };
});


var openmodal = document.querySelectorAll(".modal-open");
for (var i = 0; i < openmodal.length; i++) {
    openmodal[i].addEventListener("click", function(event) {
        event.preventDefault();
        toggleModal();
    });
}

const overlay = document.querySelector(".modal-overlay");
overlay.addEventListener("click", toggleModal);

var closemodal = document.querySelectorAll(".modal-close");
for (var i = 0; i < closemodal.length; i++) {
    closemodal[i].addEventListener("click", toggleModal);
}

document.onkeydown = function(evt) {
    evt = evt || window.event;
    var isEscape = false;
    if ("key" in evt) {
        isEscape = evt.key === "Escape" || evt.key === "Esc";
    } else {
        isEscape = evt.keyCode === 27;
    }
    if (isEscape && document.div.classList.contains("modal-active")) {
        toggleModal();
    }
};

function toggleModal() {
    const div = document.querySelector("div");
    const modal = document.querySelector(".modal");
    modal.classList.toggle("opacity-0");
    modal.classList.toggle("pointer-events-none");
    div.classList.toggle("modal-active");
}

function toggleModal(modalID) {
    document.getElementById(modalID).classList.toggle("hidden");
    document.getElementById(modalID + "-backdrop").classList.toggle("hidden");
    document.getElementById(modalID).classList.toggle("flex");
    document.getElementById(modalID + "-backdrop").classList.toggle("flex");
}