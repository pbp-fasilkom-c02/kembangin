## Kembangin
Sebuah aplikasi yang berguna bagi pengguna untuk mendapatkan informasi dan kebutuhan kesehatan seakurat mungkin.

## Situs Aplikasi
Kembangin dapat diakses melalui kembangin.herokuapp.com

## Pengembang Aplikasi
Proyek ini dibuat oleh kelompok C02 yang beranggotakan sebagai berikut:
1. Arina Aunaka - 2106638690
2. Kade Satrya Noto Sadharma - 2106752376
3. Marcellinus Elbert - 2106752400
4. Maria Aurellia - 2106750862
5. Muhammad Rifqi Adli Gumay - 2106752224
6. Risa Lestari - 2106655274

## Cerita Aplikasi
Aplikasi ini berguna untuk menyimpan data mengenai progres kesehatan anak yang akan dilaporkan oleh orang tua mereka dalam aplikasi website. Selain itu, pengguna (selain dokter) dapat melihat berita terkini mengenai kesehatan dan perkembangan tubuh anak, dapat mendiskusikan pertanyaan pemicu yang diberikan bagi pengguna yang ingin berkonsultasi, rekomendasi kebutuhan yang diperlukan anak untuk perkembangan tubuhnya, dan dapat digunakan untuk menunjukkan kategori berat badan seseorang.

## Daftar Modul
Berikut ini adalah daftar modul yang akan diimplementasikan beserta pengembang dari setiap modul.
1. Berita/artikel yang berisi informasi mengenai kesehatan tubuh dan perkembangan anak — Risa
2. Forum diskusi antara pengguna (yang berkonsultasi) dengan dokter (sebagai penjawab pertanyaan-pertanyaan pada thread/post yang diposting — Marcell
3. Rekomendasi mengenai kebutuhan untuk kesehatan anak — Maria
4. Report progress mengenai perkembangan kesehatan anak — Arina
5. Kalkulator BMI (body mass index) — Iqi
6. Profile pengguna dan dokter — Kade

## Peran Pengguna
1. Pengguna yang tidak login
Pengguna (tidak harus login) hanya dapat melihat postingan dan thread yang dibuat oleh user yang login/creator. 
Pengguna yang tidak login tidak dapat melihat halaman profile dan harus melakukan registrasi terlebih dahulu.
Pengguna (tidak harus login) dapat mengukur BMI. 
Pengguna (tidak harus login) yang mengklik salah satu thread dapat melihat detail thread. Pada detail thread, terdapat 1 starter post yang dibuat oleh pembuat thread, dan kumpulan post yang dibuat di dalam thread yang bersangkutan (termasuk reply). Starter post tidak bisa dihapus.

2. Pengguna biasa yang sudah login
Pengguna (sudah login) dapat menginisiasi forum dengan membuat postingan (postingan pertama), membuat thread (reply/comment) dari parent postingan atau thread yang sudah ada, dan edit.
Pengguna (sudah login) dapat menggunakan fitur upvote atau fitur downvote, pengguna hanya bisa upvote/downvote sekali saja.
Hanya admin yang dapat menghapus post. Admin juga dapat membuat atau mengedit post yang dibuatnya sendiri. 
Pengguna (sudah login) dapat menambahkan progress pada report progress mengenai perkembangan kesehatan anak.

3. Spesialisasi untuk dokter yang sudah login
Dokter bisa menginisiasi forum dan bisa membalas forum. 
Dokter bisa membuat dan hapus rekomendasi kebutuhan anak.


