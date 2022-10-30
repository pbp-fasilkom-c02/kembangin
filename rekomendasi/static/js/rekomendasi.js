$(document).ready(function () {
    // Get Cards
    loadRekomendasi();

    // Add Card
    $("#tambahRekomendasi").submit(function (e) {
        e.preventDefault();

        console.log("clicked");

        var data = JSON.stringify($("#tambahRekomendasi").serializeJSON())
        data = JSON.parse(data)
        console.log("data", data)

        $.ajax({
            type: "POST",
            dataType: "json",
            url: "add/",
            data: {
                data: data,
                csrfmiddlewaretoken: '{{ csrf_token }}'
            },

            success: function (response) {
                $('#tambahRekomendasi').each(function () {
                    this.reset();
                });

                console.log("sukses")
                loadTask();
                $('#authentication-modal').modal('toggle');
            },

            error: function (xhr, resp, text) {
                console.log("xhr", xhr)
                console.log("resp", resp)
                console.log("text", text)
            }
        })
    })



});

// GET
var row1 = document.createElement("div")
row1.classList.add("container", "my-12", "mx-auto", "px-5", "md:px-12")

var row2 = document.createElement("div")
row2.classList.add("flex", "flex-wrap", "-mx-1", "lg:-mx-4")



function loadRekomendasi() {
    row1.innerHTML = ""

    $.get("json/", function (data) {
        $.each(data, function (i, value) {
            var field = value.fields

            console.log("ok");

            var row3 = document.createElement("div")
            row3.classList.add("max-w-sm", "rounded", "overflow-hidden", "shadow-lg")

            // Gambar
            var img = document.createElement("img")
            img.src = field.gambar
            img.alt = field.nama_barang
            img.classList.add("max-w-sm", "rounded", "overflow-hidden", "shadow-lg")

            // Nama + Deskripsi
            var nama_deskripsi = document.createElement("div")
            nama_deskripsi.classList.add("px-6", "py-4")

            var nama = document.createElement("div")
            nama.classList.add("font-bold", "text-xl", "mb-2")
            nama.innerHTML = field.nama_barang
            nama_deskripsi.appendChild(nama)

            var deskripsi = document.createElement("p")
            deskripsi.classList.add("text-gray-700", "text-base")
            deskripsi.innerHTML = field.deskripsi
            nama_deskripsi.appendChild(deskripsi)

            // Harga + Button beli
            var harga_beli = document.createElement("div")
            harga_beli.classList.add("px-6", "pt-4", "pb-2")

            var harga = document.createElement("span")
            harga.classList.add("inline-block", "bg-gray-200", "rounded-full", "px-3", "py-1", "text-sm", "font-semibold", "text-gray-700", "mr-2", "mb-2")
            harga.innerHTML = "Rp" + field.harga_barang
            harga_beli.appendChild(harga)

            var div_btn = document.createElement("div")
            div_btn.classList.add("bg-red-400", "text-white", "rounded-lg", "pl-3", "md:pl-2", "p-2", "text-center")
            harga_beli.appendChild(div_btn)

            var a_btn = document.createElement("a")
            a_btn.classList.add("bg-red-400", "text-white", "rounded-lg", "pl-3", "md:pl-2", "p-2", "text-center")
            a_btn.href = field.url
            a_btn.innerHTML = "Beli"
            div_btn.appendChild(a_btn)

            harga_beli.appendChild(div_btn)

            row3.appendChild(img)
            row3.appendChild(nama_deskripsi)
            row3.appendChild(harga_beli)

            row2.appendChild(row3)
            row1.appendChild(row2)
        })

        document.body.append(row1)
    })

}