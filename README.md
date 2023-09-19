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
    **XML *(eXtensible Markup Languange)***
        - XML didesain *self-descriptive* sehingga kita dapat mengerti informasi yang disampaikan dari data yang tertulis
        - XML digunakan untuk **menyimpan dan mengirimkan data**
        - XML berisi informasi yang dibungkus di dalam ***tag***  
        - Kita perlu menulis program untuk mengirim, menerima, menyimpan, atau menampilkan informasi
        - **Struktur**: XML merupakan bahasa yang memiliki struktur hierarki yang kuat karena data dalam XML membentuk struktur yang bersarang seperti *tree* yang diawali oleh *root* -> *branch* -> *leaves*. Dokumen XML harus mengandung sebuah root element (parent element lain)
        - **Tujuan**: XML dikembangkan untuk menggambarkan struktur data dan membantu pertukaran data antara aplikasi yang berbeda dengan cara yang dapat dibaca dan dipahami oleh manusia
        - **Tags**: XML menggunakan tags khusus untuk mengelompokkan dan mengidentifikasi data, kita juga dapat membuat DTD *Document Type Definition*/skema XML untuk mendefinisikan struktur data yang lebih ketat
        - **Penggunaan**: XML digunakan untuk konfigurasi file, menukar data, dan menyimpan data struktural
        - **Sensitifitas**: Pada setiap elemen dalam XML perlu memiliki closing tag. Tag dalam XML sifatnya case sensitive (besar kecil huruf juga berpengaruh)

    **JSON *(JavaScript Object Notation)***
        - JSON didesain *self-describing* yang mudah dimengerti
        - JSON digunakan untuk **menyimpan dan mengirim data**
        - Sintaksnya merupakan turunan dari *Object* JavaScript
        - Format JSON berbentuk ***text*** yang membuat kode untuk membaca dan membuat JSON banyak terdapat dibanyak bahasa pemrograman
        - **Struktur**: JSON merupakan format data ringan yang terdiri dari ***key-value pairs*** yang digunakan untuk menggambarkan objek. Data JSON **lebih sederhana** dibandingkan XML
        - **Tujuan**: JSON dikembangkan untuk pertukaran data antara aplikasi yang berjalan di platform yang berbeda (biasanya dilakukan dalam lingkungan web)
        - **Notasi**: JSON menggunakan notasi objek JavaScript
        - **Penggunaan**: JSON digunakan untuk mengirim dan menerima data antara server dan browser, serta antara server dan server dalam format yang ringkas dan mudah dibaca mesin

    **HTML *(Hypertext Markup Language)***
        - HTML merupakan penanda bahasa yang digunakan untuk membuat struktur dan tampilan konten pada halaman web
        - **Struktur**: HTML menggunakan elemen-elemen **markup** untuk menggambarkan berbagai jenis konten, seperti teks, gambar, tautan dan formulir
        - **Tujuan**: HTML digunakan untuk membangun struktur dokumen web, **bukan untuk pertukaran data**. HTML digunakan untuk **menggambarkan konten dan tata letak** halaman web
        - **Interaktivitas**: HTML digunakan bersama dengan JavaScript untuk menambahkan interaktivitas dan fungsionalitas ke halaman web
        - **Penggunaan**: HTML merupakan **bahasa dasar** yang digunakan untuk membuat halaman web dan **tidak digunakan untuk mengirim data** dalam format yang sama seperti XML ataupun JSON

3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
    - **Mudah dibaca**: 
    JSON menggunakan **notasi objek JavaScript** yang sederhana sehingga mudah dibaca dan diinterpretasi oleh mesin.
    - **Ringkas**: 
    JSON memiliki struktur dan format data yang ringan dan ringkas sehingga mengurangi overhead data yang menghemat *bandwidth*
    - **Lingkungan Web Alami**: 
    JSON menggunakan sintaksis yang mirip dengan objek JavaScript sehingga banyak digunakan untuk pengembangan web. Sebagian bahasa pemrograman yang digunakan di web dapat dengan mudah mengurai dan membangun data JSON, sehingga dapat mempermudah pengolahan data dari sisi klien (browser) dan server
    - **Serialisasi dan Deserialisasi Mudah**:
    Library dan framework yang luas telah dikembangkan untuk mendukung serialisasi (mengubah data menjadi JSON) dan deserialiasi (mengubah JSON menjadi objek atau struktur data) dalam berbagai bahasa pemrograman sehingga mempermudah proses pertukaran data antara berbagai bahasa dan platform
    - **Cross-Origin Resource Sharing (CORS)**:
    Dalam pertukaran data melalui HTTP, JSON mendukung CORS yang memungkinkan aplikasi web mengambil data dari domain yang berbeda tanpa masalah keamanan cross-origin
    - **Fleksibel**:
    JSON dapat mewakili berbagai jenis data yang membuatnya sangat fleksibel untuk menggambarkan berbagai jenis informasi
    - **Ringan dan Efisien**:
    JSON memiliki overhead data yang kecil dibandingkan format pertukaran data lain seperti XML yang dapat menghemat bandwidth dan mempercepat proses transfer data
    - **RESTful APIs**: JSON digunakan dalam pengembangan layanan web RESTful sehingga data dapat dikirim dan diterima dengan permintaan HTTP GET, POST, PUT, dan DELETE
    - **Dokumentasi yang Baik**:
    JSON didokumentasikan dengan baik dalam API yang memudahkan pengembangan untuk memahami struktur data yang diharapkan

4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step
    **Tahap Awal**
    1. Mengaktifkan virtual environment pada cmd root folder. 
    2. Mengatur routing agar sesuai dengan konvensi yang ada dengan mengubah isi pada file 'urls.py' yang ada di subdirektori inventori dengan mengubah path 'main/' dengan '' pada list urlspatterns
    3. Buat skeleton/kerangka dengan membuat file base.html yang merupakan kerangka umum.
    4. Pada file setting.py di subdirektori inventori tambahkan 'DIRS': [BASE_DIR / 'templates'], pada list TEMPLATES agar file base.html dapat terdeteksi sebagai berkas template
    5. Merubah kode pada berkas main.html menjadi kode yang menggunakan 'base.html' sebagai template utama

    **Membuat input form untuk menambahkan objek model pada app sebelumnya.**
    Form digunakan untuk menginput data product dan detail product pada aplikasi yang akan ditampilkan di halaman utama
    1. **Membuat file baru -> forms.py pada di dalam folder main** Form ini digunakan untuk dapat menerima data produk baru. Pada bagian fields disesuaikan dengan informasi product yang ingin di input dan ditampilkan, saya mengisi dengan -> fields = ["menu", "amount", "description", "price", "category"] karena saya ingin memiliki product yang berisi detail menu, jumlah, deskripsi, harga, dan kategori
    2. **Dalam file views.py di folder main**
        2.1**Mengimpor beberapa hal pada file views.py dalam folder main** yaitu:
        from django.http import HttpResponseRedirect
        from main.forms import ProductForm
        from django.urls import reverse
        2.2 Lalu selanjutnya **buat fungsi baru -> create_product** yang menerima parameter request, fungsi ini digunakan untuk menghasilkan form yang dapat **menambahkan data secara otomatis** ketika data di submit
        2.3 **Ubah fungsi show_main**
        Tambahkan -> products = Product.objects.all() setelah def show_main & 'products': products dalam context. Product.objects.all() digunakan untuk mengambil seluruh object product yang disimpan dalam database
    3. **Buka urls.py pada folder main**
        3.1 import fungsi create_product yang sudah dibuat pada tahap 2.2
        3.2 Menambahkan path url ke 'urlpatterns' untuk mengakses fungsi yang telah di-import dengan code -> path('create-product', create_product, name='create_product'),
    4. **Buat file create_product.html** pada direktori main/templates, file ini dibuat dengan tujuan untuk membuat halaman "Add New Product" yang digunakan untuk membuat form penambahan produk baru
    5. **Edit file main.html**, pengeditan ini dilakukan dengan tujuan untuk menampilkan data produk (setelah diinput) dalam bentuk table serta tombol "Add New Product" yang ada dibawahnya (jika ditekan akan menuju/direct ke halaman form)

    **Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.**
    **HTML**
        Untuk fungsi views dalam format HTML sudah dilakukan pada tugas 2 dimana kita melakukan edit pada **views.py di folder main** dengan menambahkan -> from django.shortcuts import render dan membuat fungsi show_main yang diberi return function yaitu -> return render(request, "main.html", context)
        request merupakan objek permintaan HTTP yang dikirim pengguna, main.html merupakan file untuk render tampila, context merupakan dict yang berisi data yang diteruskan ke tampilan

    **XML**
        1. **Membuka file views.py di folder main**
            1.1 **Mengimport *HttpResponse* dan *Serializer*** pada bagian atas file
            1.2 **Membuat fungsi show_xml** yang menerima parameter *request* dan didalamnya terdapat variabel yang menyimpan hasil query seluruh data dalam product, code:
            def show_xml(request):
                data = Product.objects.all()
            1.3 **Menambah return function** berupa *HttpResponse* yang berisi data hasil query, code:
            return HttpResponse(serializers serialize("xml", data), content_type="application/xml")

    **JSON**
        1. **Membuka file views.py di folder main**
            1.1 **Membuat fungsi show_json** yang menerima parameter *request* dan didalamnya terdapat variabel yang menyimpan hasil query seluruh data dalam product, code:
            def show_json(request):
                data = Product.objects.all()
            1.2 **Menambah return function** berupa *HttpResponse* yang berisi data hasil query, code:
            return HttpResponse(serializers.serialize("json", data), content_type="application/json")

    **XML by ID**
        1. **Membuka file views.py di folder main**
            1.1 **Membuat fungsi show_xml_by_id** yang menerima parameter *request* dan id didalamnya terdapat variabel yang menyimpan hasil query dari data dengan id tertentu dalam product, code:
            def show_xml_by_id(request, id):
                data = Product.objects.filter(pk=id)
            1.2 **Menambah return function** berupa *HttpResponse* yang berisi parameter data hasil query dan parameter *content_type* dengan value , "application/xml" code:
            return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

    **JSON by ID**
        1. **Membuka file views.py di folder main**
            1.1 **Membuat fungsi show_json_by_id** yang menerima parameter *request* dan id didalamnya terdapat variabel yang menyimpan hasil query dari data dengan id tertentu dalam product, code:
            def show_json_by_id(request, id):
                data = Product.objects.filter(pk=id)
            1.2 **Menambah return function** berupa *HttpResponse* yang berisi parameter data hasil query dan parameter *content_type* dengan value , "application/json" code:
            return HttpResponse(serializers.serialize("json", data), content_type="application/json")

    **Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.**
    1. **Membuka file urls.py yang ada dalam folder main** dan impor fungsi path dengan -> from django.urls import path
        1.1 **Routing HTML**
            -  **Import fungsi yang sudah dibuat** yaitu code "from main.views import show_main"
            - **Tambahkan path kedalam 'urlpatterns'** dengan -> path('', show_main, name='show_main'),
            Hal ini dilakukan guna mengakses fungsi yang sudah diimpor
        1.2 **Routing XML**
            - **Import fungsi yang sudah dibuat** yaitu code sebelumnya ditambahkan 'show_xml' "from main.views import show_main, create_product" **menjadi** "from main.views import show_main, create_product, **show_xml**"
            - **Menambahkan path url kedalam 'urlpatterns'**, hal ini dilakukan guna mengakses fungsi yang sudah diimpor, code:
            path('xml/', show_xml, name='show_xml'), 

        1.3 **Routing JSON**
            - **Import fungsi yang sudah dibuat** yaitu code sebelumnya ditambahkan 'show_json'"from main.views import show_main, create_product, show_xml" **menjadi** "from main.views import show_main, create_product, show_xml, **show_json**" 
            - **Menambahkan path url kedalam 'urlpatterns'**, hal ini dilakukan guna mengakses fungsi yang sudah diimpor, code:
            path('json/', show_json, name='show_json'), 

        1.4 **Routing XML by ID**
            - **Import fungsi yang sudah dibuat** yaitu code sebelumnya ditambahkan 'show_xml_by_id'"from main.views import show_main, create_product, show_xml, show_json" **menjadi** "from main.views import show_main, create_product, show_xml, show_json, **show_xml_by_id**" 
            - **Menambahkan path url kedalam 'urlpatterns'**, hal ini dilakukan guna mengakses fungsi yang sudah diimpor, code:
            path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),

        1.5 **Routing JSON by ID**
            - **Import fungsi yang sudah dibuat** yaitu code sebelumnya ditambahkan 'show_json_by_id'"from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id" **menjadi** "from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, **show_json_by_id**" 
            - **Menambahkan path url kedalam 'urlpatterns'**, hal ini dilakukan guna mengakses fungsi yang sudah diimpor, code:
            path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),

5. **Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.**
    **HTML**
    ![This is an image](/html_postman_2206829023_RahidaSyafaNurdya.png)

    **XML**
    ![This is an image](/xml_postman_2206829023_RahidaSyafaNurdya.png)

    **JSON**
    ![This is an image](/json_postman_2206829023_RahidaSyafaNurdya.png)

    **XML by ID**
    ![This is an image](/xml_by_id_postman_2206829023_RahidaSyafaNurdya.png)

    **JSON by ID**
    ![This is an image](/json_by_id_postman_2206829023_RahidaSyafaNurdya.png)