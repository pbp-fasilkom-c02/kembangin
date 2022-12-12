const useToast = (toastTrigger, komentar, invalid) => {
    const toast = invalid ? new bootstrap.Toast($('#liveToastInvalid')[0]) : komentar ? new bootstrap.Toast($('#liveToastKomentar')[0]) : new bootstrap.Toast($('#liveToast')[0])
    toast.show()
}

const comment = (reply) => `
<div class="animate-slide-in-fwd-center" id="${reply.pk}-reply">
    <div class="text-md mt-2">${reply.comment}</div>
    <div class="text-sm mt-3">${reply.created_at.split("T")[0]}</div>
    <div class="flex justify-between">
    
    <div class="text-sm mb-2">Dikomentari oleh <a class="font-bold" href="/user_profile/${reply.author_pk}">dr. ${reply.author}</a></div>
    <button class="cursor-pointer" id='${reply.pk}'>
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
<path stroke-linecap="round" stroke-linejoin="round" d="M14.74 9l-.346 9m-4.788 0L9.26 9m9.968-3.21c.342.052.682.107 1.022.166m-1.022-.165L18.16 19.673a2.25 2.25 0 01-2.244 2.077H8.084a2.25 2.25 0 01-2.244-2.077L4.772 5.79m14.456 0a48.108 48.108 0 00-3.478-.397m-12 .562c.34-.059.68-.114 1.022-.165m0 0a48.11 48.11 0 013.478-.397m7.5 0v-.916c0-1.18-.91-2.164-2.09-2.201a51.964 51.964 0 00-3.32 0c-1.18.037-2.09 1.022-2.09 2.201v.916m7.5 0a48.667 48.667 0 00-7.5 0" />
</svg>
</button>
    </div>
    <hr></div>`

const forumPost = (post) => `<div class="sm:ml-24 mt-10 flex flex-col">
<div class="text-center sm:text-left  text-xl sm:text-2xl font-bold">
    Forum Konsultasi
</div>
<div class="text-center sm:text-left">${post.created_at.split('T')[0]}</div>


</div>
<div class="mx-8 sm:mx-[22%] mt-2 sm:mt-5">
<div>
    <div class="sm:text-left text-center text-xl sm:text-3xl text-red-500 capitalize">
        ${post.question}
    </div>
    <div class="mt-1 sm:text-left text-center">Dibuat oleh <a class="font-bold" href="/user_profile/${post.author_pk}">${post.is_doctor ? "dr. " : ""}${post.author}</a></div>
    <div class="mt-4 sm:text-lg text-sm sm:text-left text-justify">${post.description}</div>
</div>
<div class="flex gap-5 mt-4">

<div class="flex gap-2">
<div>${post.upvote}</div>
<button id="upvote">
<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
<path stroke-linecap="round" stroke-linejoin="round" d="M15 11.25l-3-3m0 0l-3 3m3-3v7.5M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
</button>
</svg>


</div>
<div class="flex gap-2">
<div>${post.downvote}</div>
<button id="downvote">
<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
<path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75l3 3m0 0l3-3m-3 3v-7.5M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
</svg>
</button>
    </div>

</div>`

const addComment = (reply) => {
    return $('#comment-section').prepend(comment(reply))
}

const deleteReply = (reply) => {
    $(`#${reply.pk}`).click(function () {
        $.ajax({
            url: `/forum/${reply.pk}/delete-comment/`,
            type: 'DELETE',
            success: function (response) {

                if (response.status == "error") {
                    useToast(true, true, false)
                }
                else {
                    $(`#${reply.pk}-reply`).addClass("animate-slide-out-blurred-right")
                    setTimeout(function () { $(`#${reply.pk}-reply`).remove(); }, 600);
                }
            },
        })
    })
}

const upVote = (pk) => {
    $("#upvote").click(function () {
        $.ajax({
            url: `/forum/${pk}/vote/up`,
            type: 'PUT',
            success: function (response) {
                $('.get-id').empty()
                $('#comment-section').empty()
                createForum(response, pk)

            }
        });
    })
}
const downVote = (pk) => {
    $("#downvote").click(function () {
        $.ajax({
            url: `/forum/${pk}/vote/down`,
            type: 'PUT',
            success: function (response) {
                $('.get-id').empty()
                $('#comment-section').empty()
                createForum(response, pk)
            }
        });
    })
}

const createForum = (data, pk) => {
    $('.get-id').prepend(forumPost(data))
    upVote(pk)
    downVote(pk)
    data.replies.map((reply) => {
        addComment(reply)
        deleteReply(reply)
    })
}

$(document).ready(function () {
    const pk = $(".get-id").attr("id")
    $.get(`/forum/json/${pk}`, function (data) {
        createForum(data, pk)
    })

    $("#btn-submit").click(function () {
        $.post(`/forum/${pk}/add-comment`, { comment: $(".comment-input").val() }, function (res) {

            if (res.status == "error") {
                useToast(true, false, false)
            }
            if (res.status == "invalid") {
                useToast(true, false, true)
            }
            else {
                addComment(res)
                deleteReply(res)

            }

            $(".comment-input").val('')

        })
    })
})