function get_profile(id) {
    $.ajax({
        url: `/user_profile/get_user/`+id,
        type: 'GET',
        dataType: 'json',
    }).done(function(response) {
        var details = `
        <div>
            <p class="font-bold text-xl">Username:</p>
            <p class="text-3xl font-bold text-blue-500">
                ${response.is_doctor ? "dr. " : ""}${response.username}
            </p>
        </div>
        <div>
            <p class="font-bold text-xl">Email:</p>
            <p class="font-bold text-2xl text-blue-500">${response.email}</p>
        </div>
        `
        var profile = `
        <p>Telah membuat <span class="font-bold text-blue-500"> ${response.post_amount} pertanyaan</span> di forum</p>
        <p>Telah mendapatkan <span class="font-bold text-blue-500">${response.upvote_amount} poin</span> di forum</p>
        `
        var bio_part = `
        
        <p id="bio-content" class="rounded bg-red-200 border-2 border-neutral-500 py-2 px-2 responsive"></p>
        `
        $("#details").append(details)
        $("#profile").append(profile)
        $("#bio").append(bio_part)
        if(response.bio != ""){
            $("#bio-content").text(response.bio)
        }else{
            $("#bio-content").text("User belum menulis bio")
        }
        
        if (response.is_logged_user){
            var change_button = `
            <button class="mt-8 text-white bg-red-500 hover:bg-red-700 rounded-md font-bold px-5 py-2.5 mr-2 mb-2" data-bs-toggle="modal" data-bs-target="#change-profile-modal">Ubah Profile</button>
            `
            $("#change-button-container").append(change_button)
        }
        if (response.is_doctor){
            var reply_amount = `
                <div id="comment_amount">
                    <p>Telah membuat <span class="font-bold text-blue-500">${response.comment_amount} balasan</span> di forum</p>
                </div>
            `
            $("#profile").append(reply_amount)
            var rating_average = `<div class="text-blue-500 text-2xl font-bold"><span id="average">${response.rating_average}</span>/5</div>`
            $("#rating-average").append(rating_average)
            for (var i in response.ratings){
                var rating_item = response.ratings[i]
                var rating_content = `
                <div id="rating${rating_item.id}" class="mt-6">
                    <div>
                        <a href="/user_profile/${rating_item.author_pk}"
                        class="text-2xl block text-black-700 font-bold rounded hover:bg-red-200 md:hover:bg-transparent md:border-0 md:hover:text-red-400">
                        ${rating_item.author_is_doctor ? "dr. " : ""}${rating_item.author_username}
                        </a>
                    </div>
                    <div>
                        <p>${rating_item.date.split('T')[0]}</p>
                    </div>
                    <div id="rating-amount${rating_item.id}" class="mt-2">
                        <p>Rating:</p>
                    </div>
                    <div class="mt-2">
                        <p>Komentar:</p>
                    </div>
                    <div>
                        <p>${rating_item.comment}</p>
                    </div>
                    <div id="delete-div">
                        <button class="font-bold hover:text-red-500 mt-2" onclick="delete_rating(${rating_item.id}, ${rating_item.author_pk})">Delete</button>
                    </div>
                    <hr>
                </div>
                `
                $("#rating-content").append(rating_content)
                for (var i = 0; i < rating_item.rating; i++) {
                    $("#rating-amount"+rating_item.id).append("❤️")       
                }
            }
        }        
    })
}

$(document).ready(function() {
    $('#change-profile-form').submit(function(e) {
        var id = $(".profile-id").attr("id")
        var csrf = document.querySelector('[name=csrfmiddlewaretoken]').value
        e.preventDefault();
        $.ajax({
            url: "/user_profile/change_profile/" + id,
            type: 'POST',
            data: {
                bio: $("#id_bio").val(),
                csrfmiddlewaretoken: csrf,
            },
            
        }).done(function(response) {
            var bio = response.new_bio
            $("#bio-content").text(bio);
            hide_toast()
            $('#success_change_profile').toast('show')
        })
        $(this).trigger('reset')
    })
})

$(document).ready(function() {
    $('#create-rating-form').submit(function(e) {
        e.preventDefault();
        var id = $(".profile-id").attr("id")
        var csrf = document.querySelector('[name=csrfmiddlewaretoken]').value
        $.ajax({
            url: "/user_profile/create_rating/" + id,
            type: 'POST',
            data: {
                rating: $("#id_rating").val(),
                comment: $("#id_comment").val(),
                csrfmiddlewaretoken: csrf,
            },
            
        }).done(function(response) {
            if (response.status === "success_create" || response.status === "success_edit"){
                if (Object. keys(response).length === 10){
                    $(`#rating` + response.old_id).remove()
                }
                var rating_object = `
                <div id="rating${response.new_id}" class="mt-6">
                    <div>
                        <a href="/user_profile/${response.author_pk}"
                        class="text-2xl block text-black-700 font-bold rounded hover:bg-red-200 md:hover:bg-transparent md:border-0 md:hover:text-red-400">
                        ${response.is_doctor ? "dr. " : ""}${response.author}
                        </a>
                    </div>
                    <div>
                        <p>${response.date.split('T')[0]}</p>
                    </div>
                    <div id="rating-amount${response.new_id}" class="mt-2">
                        <p>Rating:</p>
                    </div>
                    <div class="mt-2">
                        <p>Komentar:</p>
                    </div>
                    <div>
                        <p>${response.comment}</p>
                    </div>
                    <div id="delete-div" class="mt-2">
                        <button class="font-bold hover:text-red-500" onclick="delete_rating(${response.new_id}, ${response.author_pk})">Delete</button>
                    </div>
                    <hr>
                </div>
                `
                $("#rating-content").append(rating_object)
                $("#average").text(response.rating_average)
                for (var i = 0; i < response.rating; i++) {
                    $("#rating-amount"+response.new_id).append("❤️") 
                }
            }
            hide_toast()
            switch(response.status){
                case "success_create":
                    $('#success_create_rating').toast('show')
                    break
                case "success_edit":
                    $('#success_change_rating').toast('show')
                    break
                case "error_login":
                    $('#error_login').toast('show')
                    break
                case "error_same_user":
                    $('#error_same_user').toast('show')
                    break
                default:
                    $('#error_general').toast('show')
            }
        })
        $(this).trigger('reset')
    })
})

function delete_rating(rating_id, author_id){
    var logged_id = $(".login-user-id").attr("id")
    $.ajax({
        type :"DELETE",
        url :`/user_profile/delete_rating/${rating_id}`,
        data: {
            author_id: author_id,
            logged_id: logged_id,
        },
    }).done(function(response){
        hide_toast()
        if (response.status === "success"){
            $(`#rating` + rating_id).remove()
            $(`#average`).text(response.rating_average)
            $('#success_delete_rating').toast('show')
        }else{
            $('#error_delete_rating').toast('show')
        }
    })
}

function hide_toast(){
    $('#success_create_rating').toast('hide')
    $('#success_change_rating').toast('hide')
    $('#error_login').toast('hide')
    $('#error_same_user').toast('hide')
    $('#success_delete_rating').toast('hide')
    $('#error_general').toast('hide')
    $('#error_delete_rating').toast('hide')
}