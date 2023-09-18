Nama : Rahida Syafa Nurdya
NPM  : 2206829023
Kelas: PBP-B


Link aplikasi Adaptable yang telah dideploy: https://nonasweetcreations.adaptable.app
Link repositori github: https://github.com/Rahidasyf/inventori.git

**TUGAS 2**
1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    1. membuat direktori utama baru dengan nama "inventori";
    2. kita akan membuka cmd/command prompt pada  direktori utama "inventori";
    3. menginisiasikan repositori baru pada git dengan memberikan perintah "git init" pada cmd;
    4. mengatur username dan email yang diasosiasikan dengan direktori utama ke repositori git dengan perintah "git config user.name "rahidasyf"" dan "git config user.email "rahidanona74@gmail.com""
    5. memastikan bahwa konfigurasi lokal telah diatur dan dilakukan dengan benar pada repositori lokal dengan perintah "git config --list --local"
    6. pada web github kita buat repositori baru yang bernama "inventori" dengan visibilitas Public

    **Membuat sebuah proyek Django baru**
    1. membuka cmd pada direktori utama "inventori" yang sudah dibuat 
    2. membuat virtual environment dengan perintah "python -m venv env" pada cmd tersebut
    3. aktifkan virtual environment dengan perintah "env\Scripts\activate.bat" (pada windows), jika sudah aktif ditandai dengan (env)
    4. menyiapkan dependencies yang diperlukan dengan membuat file "requirements.txt" dalam direktori utama "inventori" dengan menambahkan dependencies:
        django
        gunicorn
        whitenoise
        psycopg2-binary
        requests
        urllib3
    5. pasang dependencies dengan menjalankan perintah "pip install -r requirements.txt" pada cmd direktori utama "inventori"
    6. membuat proyek django bernama "inventori" dengan menjalankan perintah "django-admin startproject shopping_list ." pada cmd direktori utama "inventori"
    7. pada "settings.py" tambahkan "*" pada "ALLOWED_HOST" -> ALLOWED_HOSTS = ["*"]
    8. membuat file baru ".gitignore" pada direktori utama "inventori", file ini merupakan file konfigurasi yang digunakan dalam repositori github
    9. pada cmd deactivate virtual environment dengan perintah "deactivate"

    **Membuat aplikasi dengan nama main pada proyek tersebut**
    1. membuka cmd pada direktori utama "inventori" yang sudah dibuat 
    2. aktifkan virtual environment dengan perintah "env\Scripts\activate.bat" (pada windows), jika sudah aktif ditandai dengan (env)
    3. buat aplikasi baru dengan nama main dengan menjalankan perintah "python manage.py startapp main" pada cmd
    4. mendaftarkan aplikasi "main" ke dalam proyek dengan cara membuka file "settings.py" dalam direktori proyek "inventori" dalam variabel "INSTALLED_APPS" tambahkan " 'main', "
    *langkah ini membantu mendaftarkan aplikasi "main" ke proyek inventori*

    **Melakukan routing pada proyek agar dapat menjalankan aplikasi main**
    1. membuat file "urls.py" pada direktori "main" dengan isi: 
        from django.urls import path
        from main.views import show_main

        app_name = 'main'

        urlpatterns = [
            path('', show_main, name='show_main'),
        ]

    **Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib**
    1. Membuka dan mengubah file "models.py" yang ada pada direktori aplikasi main sesuai dengan syarat/atribut wajib dan opsional yang diinginkan dengan isi:
        from django.db import models

        class Product(models.Model):
            name = models.CharField(max_length=255)
            kelas = models.CharField(max_length=255)
            menu = models.CharField(max_length=255)
            amount = models.IntegerField()
            description = models.TextField()
            price = models.CharField(max_length=255)
            category = models.TextField()
    - name sebagai nama mahasiswa dengan tipe Char
    - kelas sebagai nama kelas dengan tipe CharField
    - menu name sebagai nama item/menu dengan tipe CharField
    - amount sebagai jumlah dari suatu item dengan tipe IntegerField
    - description sebagai deskripsi suatu item dengan tipe TextField
    - price sebagai harga suatu item dengan tipe CharField
    - category sebagai kategori dari suatu item dengan tipe TextField

    **Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu**
    1. Membuat direktori baru dengan nama "templates" di dalam direktori aplikasi "main"
    2. Buat file "main.html" pada direktori "templates", isi file ini sesuai dengan yang ingin kita tampilkan di peramban web, contoh:
        <!DOCTYPE html>
        <html>
            <head>
                <title>Menu Nona's Sweet Creation</title>
                <h3>Name: </h3>
                <p>{{name}}<p>
                <h3>Class: </h3>
                <p>{{kelas}}<p>
        </head>
        <h1>Nona's Sweet Creations</h1>
        <body>
            <table border="1">
                <tr>
                    <th colspan="1" bgcolor="#E6896B">Menu</th>
                </tr>
                <tr>
                    <td rowspan="1">
                        <img src="https://images.tokopedia.net/img/cache/700/VqbcmM/2022/11/7/7a52f071-fdae-47e6-a60a-b35f52e8529d.jpg" width="200" />
                    </td>
                </tr>
            </table>
        </body>
        <h5>Item Name: </h5>
        <p>{{menu}}<p>
        <h5>Stock Amount: </h5>
        <p>{{amount}}<p>
        <h5>Description: </h5>
        <p>{{description}}<p>
        <h5>Price: </h5>
        <p>{{price}}<p>
        <h5>Category: </h5>
        <p>{{category}}<p>
        </html>

    **Mengedit file views.py sesuai syarat/ketentuan wajib yang diperlukan**
    1. Buka berkas "views.py" pada file aplikasi main
    2. rubah berkas sesuai dengan yang berikut ini:
    from django.shortcuts import render
        def show_main(request):
            context = {
                'name': 'Rahida Syafa Nurdya',
                'kelas': 'PBP B',
                'menu': 'Kue Jongkong',
                'amount': '10',
                'description': 'Kue basah tradisional nan lembut, ringan disantap, lumer dimulut dan pastinya legit',
                'price': 'Rp25.000',
                'category': 'Kue Basah',
            }
            return render(request, "main.html", context)
    - context akan berisi data yang dikirimkan ke tampilan yaitu ->
        name = Data nama
        kelas = Daftar kelas
        menu = Item name
        amount = Jumlah tiap item
        description = Deskripsi Item
        price = Harga item
        category = Kategori Item


    **Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py**
    1. Buat file baru dengan nama "urls.py" dalam direktori main yang berisi:
        from django.urls import path
        from main.views import show_main

        app_name = 'main'

        urlpatterns = [
            path('', show_main, name='show_main'),
        ]
    2. Buka file "urls.py" dalam direktori proyek "inventori" 
    3. Impor fungsi inlude dari django.urls -> from django.urls import path, include
    4. Tambahkan rute URL dalam variabel urlpatterns:
        urlpatterns = [
            ...
            path('main/', include('main.urls')),
            ...
        ]

    **Melakukan push ke repositori github**
    1. membuka cmd pada direktori utama "inventori" yang sudah dibuat 
    2. jalankan "git status" , "git commit -m "Final", "git branch -M main", "git remote add origin <URL_REPO>" -> link reponya github yang sudah kita buat tadi, lalu "git push -u origin main"

    **Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet**
    1. Login akun adaptable lalu tekan "New App"
    2. Pilih Connect an Existing Repository.
    3. Pilih yang terhubung dengan GitHub serta pilih All Repositories
    4. Memilih repositori proyek yang baru dibuat yaitu "inventori". Pilihlah branch yang ingin dijadikan sebagai deployment branch
    5. Pilih Python App Template dan PostgreSQL
    6. Pilih python version yang sesuai yang dimiliki lalu masukkan perintah python manage.py migrate && gunicorn inventori.wsgi
    7. Masukkan nama aplikasi yang dinginkan 
    8. Centang HTTP Listener on PORT dan klik Deploy App

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
    Berikut bagan yang berisi request client
    ![This is an image](/Bagan_RequestClient_RahidaSyafaNurdya.jpg)

3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
    - Virtual Environment digunakan untuk mengisolasi package/lingkungan dan dependencies dari aplikasi agar tidak saling bertabrakan dengan versi lain yang ada didalam komputer yang mungkin berbeda. Virtual Environment bergunak untuk memastikan bahwa ketika kita melakukan pembaruan pada suatu library di salah satu proyek, versi library tersebut tidak akan berubah pada proyek lainnya. Dengan Virtual Environment akan mempertahankan konsistensi ketika diimplementasi di lingkungan yang berbeda (mengurangi masalah).
    - Membuat aplikasi web berbasis Django tanpa menggunakan virtual environment bisa saja dilakukan, namun itu tidak disarankan karena hal ini merupakan praktik yang kurang baik yang dapat menyebabkan masalah dalam pengembangan dan pemeliharaan proyek. Tanpa virtual environment, kita akan lebih rentan terhadap konflik dependensi, masalah kompatibilitas, dan sulit untuk mengelola proyek yang lebih besar atau lebih kompleks. Peran Virtual Environment untuk mengisolasi, mengorganisasi serta mengelola proyek yang kita buat yang dapat mencegah adanya masalah jika tidak digunakan mungkin saja akan menimbulkan banyak masalah bagi proyek kita kedepannya.

4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
    - MVC (Model-View-Controller) adalah sebuah pola arsitektur dalam pengembangan sistem web yang terdiri dari tiga elemen utama, yaitu:
        - Model: Komponen yang bertanggung jawab untuk mengelola data dan berinteraksi langsung dengan basis data. Model mengelola data dan aturan bisnis, dan tidak bergantung pada tampilan atau pengontrol.
        - View: Menampilkan informasi kepada pengguna dengan cara yang sesuai dan mengirim input pengguna ke pengontrol. Tampilan mengamati model untuk mendapatkan data yang diperlukan untuk ditampilkan.
        - Controller: Penghubung antara model dan view ketika ada permintaan dari pengguna. Menerima input dari pengguna, memprosesnya, dan memutuskan tindakan selanjutnya. Pengontrol berkomunikasi dengan model dan memperbarui tampilan.
    Pola arsitektur ini membantu dalam mengatur dan memisahkan tanggung jawab masing-masing elemen dalam pengembangan situs web, dimana tampilan dan pengontrol memiliki ketergantungan yang kuat satu sama lain.

    - MVT (Model-View-Template) adalah varian dari MVC yang sering digunakan dalam kerangka kerja web Django. Dalam MVT, Template digunakan untuk mengelola tampilan dan memisahkan tampilan dari logika bisnis aplikasi. Model menangani data dan logika bisnis, sedangkan View mengatur tampilan dan menghubungkan Model dan Template
        - Model: Sama seperti pada MVC, ini adalah representasi dari data dan logika bisnis.
        - View: Menampilkan data kepada pengguna dan menanggapi permintaan dari pengguna. Bertanggung jawab untuk mengatur tampilan dan berinteraksi dengan model, tetapi tidak memiliki logika bisnis. 
        - Template: Mengatur tampilan (UI) dan format data yang akan ditampilkan. Menentukan bagaimana tampilan akhir akan terlihat. Ini adalah bagian dari Django yang bertanggung jawab untuk memproses dan menampilkan data dalam HTML.
     MVT adalah variasi dari MVC yang digunakan dalam kerangka kerja Django. Perbedaan utamanya adalah penggunaan template yang memisahkan logika tampilan dari logika bisnis.

    - MVVM (Model-View-ViewModel) adalah pola arsitektur yang sering digunakan dalam pengembangan aplikasi berbasis antarmuka pengguna (UI) yang kompleks, terutama dalam kerangka kerja seperti Angular atau Vue.js. ViewModel memainkan peran penting dalam memisahkan logika tampilan (View) dari logika bisnis (Model) dengan kemungkinan komunikasi dua arah antara Model dan View
        - Model: Sama seperti dalam MVC dan MVT, ini adalah representasi data dan logika bisnis.
        - View: Bertanggung jawab untuk menampilkan data/informasi ke pengguna dan mengamati ViewModel untuk mendapatkan data yang diperlukan untuk ditampilkan. Serta mengirim input pengguna ke ViewModel.
        - ViewModel: Bertindak sebagai perantara antara Model dan View. Ini mengelola pemformatan dan representasi data yang sesuai dengan tampilan. ViewModel juga dapat mengandung logika tampilan yang sederhana.
    
    **Perbedaan ketiganya** terletak pada bagaimana mereka mengelola tampilan dan alur kontrol, serta memisahkan komponen dalam pengembangan aplikasi. MVC memiliki kontroler yang mengendalikan alur, MVT menggunakan Template untuk mengatur tampilan, dan MVVM memiliki ViewModel yang bertindak sebagai perantara antara Model dan View. Pemilihan pola tergantung pada jenis aplikasi yang akan dibuat, dikembangkan, kerangka kerja yang digunakan, serta preferensi dan kebutuhan spesifik terkait proyek yang ingin dibuat. 

**TUGAS 3**
1. Apa perbedaan antara form POST dan form GET dalam Django?
    - **POST** -> Permintaan POST digunakan untuk **mengirim data** (file, data formulir, dll.) ke server. Jika berhasil berhasil, maka akan mengembalikan kode status **HTTP 201 (OK)**. POST **mengirimkan data** baru ke API. Data dikirim secara **langsung dan tidak ditampilkan di URL**. Data yang dikirim melalui form POST **tidak dibatasi panjang string** dan **lebih aman**. Pengambilan variabel dilakukan dengan **request.POST.get**. 
    Data formulir dikirimkan dalam badan permintaan HTTP. Ini berarti data formulir tidak akan terlihat dalam URL. Oleh karena itu, lebih aman untuk mengirim data sensitif seperti kata sandi. Formulir dapat diamankan dengan menggunakan token CSRF (Cross-Site Request Forgery) dalam Django untuk mencegah serangan palsu terhadap situs web.
    POST tidak memiliki batasan kapasitas data yang ketat, sehingga kita dapat mengirimkan dalam jumlah data yang lebih besar. POST biasanya digunakan ketika Anda ingin mengirim data formulir untuk membuat, memperbarui, atau menghapus sesuatu di server, atau ketika Anda ingin mengunggah file.
    - **GET** -> Permintaan GET digunakan untuk **membaca/mengambil** data dari server web. GET mengembalikan **HTTP kode status 200 (OK)** jika data berhasil diambil dari server. GET **mengambil data** dari API. Data dikirim **tidak langsung dan ditampilkan di URL** sehingga user dapat dengan mudah memasukkan nilai. Data yang dikirim melalui form GET **dibatasi panjang string sampai 2047 karakter** dan **kurang aman**. Pengambilan variabel dilakukan dengan **request.GET.get**. 
    Data formulir ditambahkan ke URL sebagai parameter query string. Ini membuat data dapat terlihat di URL, yang bisa kurang aman, terutama jika formulir berisi informasi sensitif.
    GET memiliki batasan kapasitas yang terbatas karena data dikirim melalui URL yang memiliki batasan panjang. GET umumnya digunakan untuk mengambil data dari server, seperti melakukan pencarian atau menavigasi ke halaman berdasarkan parameter URL.
Dalam penggunaannya, form POST digunakan untuk *mengirim data yang bersifat sensitif* atau data yang akan mengubah keadaan sistem, seperti mengubah database. Sedangkan form GET digunakan untuk mengambil *data yang tidak bersifat sensitif*, seperti form pencarian

2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
