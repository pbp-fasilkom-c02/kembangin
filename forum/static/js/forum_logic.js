const useToast = (toastTrigger, loginRequired) => {
    const toast = loginRequired ? new bootstrap.Toast($('#liveToastLoginReq')[0]) : new bootstrap.Toast($('#liveToast')[0])
    toast.show()
}
const forumPost = (post) => `<div id='${post.pk}-post' class="animate-slide-in-fwd-center">
    <div class="flex justify-between ">

        <div class="text-md sm:text-xl text-red-500 capitalize underline cursor-pointer" onclick="location.href='/forum/${post.pk}'">
            ${post.question}
        </div>
        <button class="cursor-pointer" id='${post.pk}'>
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
<path stroke-linecap="round" stroke-linejoin="round" d="M14.74 9l-.346 9m-4.788 0L9.26 9m9.968-3.21c.342.052.682.107 1.022.166m-1.022-.165L18.16 19.673a2.25 2.25 0 01-2.244 2.077H8.084a2.25 2.25 0 01-2.244-2.077L4.772 5.79m14.456 0a48.108 48.108 0 00-3.478-.397m-12 .562c.34-.059.68-.114 1.022-.165m0 0a48.11 48.11 0 013.478-.397m7.5 0v-.916c0-1.18-.91-2.164-2.09-2.201a51.964 51.964 0 00-3.32 0c-1.18.037-2.09 1.022-2.09 2.201v.916m7.5 0a48.667 48.667 0 00-7.5 0" />
</svg>
</button>
        </div>
       
        <div class="text-sm sm:text-md mt-2">
            ${post.description}
        </div>
        <div class="text-sm mt-4">
            ${post.created_at.split('T')[0]}  
        </div>
        <div class="text-sm">
            Dibuat oleh <span class="font-bold">${post.is_doctor ? "dr. " : ""}${post.author}</span>
        </div>
        <div class="flex gap-4 mt-2">
            <div class="flex gap-2">
                <div>${post.replies.length}</div>
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
<path stroke-linecap="round" stroke-linejoin="round" d="M8.625 9.75a.375.375 0 11-.75 0 .375.375 0 01.75 0zm0 0H8.25m4.125 0a.375.375 0 11-.75 0 .375.375 0 01.75 0zm0 0H12m4.125 0a.375.375 0 11-.75 0 .375.375 0 01.75 0zm0 0h-.375m-13.5 3.01c0 1.6 1.123 2.994 2.707 3.227 1.087.16 2.185.283 3.293.369V21l4.184-4.183a1.14 1.14 0 01.778-.332 48.294 48.294 0 005.83-.498c1.585-.233 2.708-1.626 2.708-3.228V6.741c0-1.602-1.123-2.995-2.707-3.228A48.394 48.394 0 0012 3c-2.392 0-4.744.175-7.043.513C3.373 3.746 2.25 5.14 2.25 6.741v6.018z" />
</svg>

</div>
<div class="flex gap-2">
<div>${post.upvote}</div>
<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
<path stroke-linecap="round" stroke-linejoin="round" d="M15 11.25l-3-3m0 0l-3 3m3-3v7.5M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
</svg>


</div>
<div class="flex gap-2">
<div>${post.downvote}</div>
<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
<path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75l3 3m0 0l3-3m-3 3v-7.5M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
</svg>


</div>
        </div>
        <hr size="10" class="mt-5">
    </div>`

const addPost = (post) => {
    return $('#forum').prepend(forumPost(post))
}

const deletePost = (post) => {
    $(`#${post.pk}`).click(function () {
        $.ajax({
            url: `/forum/delete/${post.pk}`,
            type: 'DELETE',
            success: function (response) {

                if (response.status == "error") {

                    useToast(true, false)
                }
                else {
                    $(`#${post.pk}-post`).addClass("animate-slide-out-blurred-right")
                    setTimeout(function () { $(`#${post.pk}-post`).remove(); }, 600);
                }
            },
        })
    })
}

$(document).ready(function () {
    $.get('/forum/json', function (data) {
        console.log(data)
        data.map((post) => {
            addPost(post)
            deletePost(post)
        }

        )
    })

    $("#btn-submit").click(function () {
        const forum = {
            question: $(".question-input").val(),
            description: $(".description-input").val()
        }

        $.post('/forum/add', forum, function (res) {
            if (res.status == "error") {
                useToast(true, true)
            }
            else {
                addPost(res)
                deletePost(res)
            }


            $(".question-input").val('')
            $(".description-input").val('')
        })
    })
})