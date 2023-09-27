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

**TUGAS 4**
**1.  Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?**
    ***UserCreationForm*** adalah sebuah impor formulir bawaan yang disediakan oleh Django dengan tujuan untuk **memudahkan pembuatan formulir pendaftaran** pengguna dalam aplikasi web. Dengan formulir ini, pengguna baru dapat mendaftar dengan mudah di situs web tanpa harus menulis kode dari awal. Formulir ini digunakan untuk mengumpulkan informasi yang diperlukan untuk membuat akun pengguna baru, seperti username dan password.
    **Kelebihan**
    - **Mudah digunakan**: UserCreationForm merupakan bagian dari modul 'django.contrib.auth.forms' sehingga kita dapat menggunakannya dengan mudah dalam aplikasi Django tanpa harus menulis kode dari awal
    - **Keamanan**: Formulir UserCreationForm sudah memiliki validasi bawaan yang memastikan bahwa input yang diberikan sesuai dengan aturan yang ditetapkan.
    - **Integrasi dengan Sistem Otentikasi Django**: Formulir UserCreationForm telah terintegrasi dengan baik dengan sistem otentikasi yang sudah ada di Django, yang mencakup manajemen otentikasi pengguna, login, logout, dan lainnya.
    **Kekurangan**
    - **Tidak sesuai untuk case custom**: Jika kita membiliki kebutuhan yang sangat khusus untuk proses pendaftaran pengguna(user), UserCreationForm mungkin terlalu sederhana sehingga kita perlu membuat formulir custom yang lebih sesuai. UserCreationForm itu sifatnya sudah default dan tidak bisa di kostumisasi (harus ada yang dirubah sendiri).
    - **Tampilan default mungkin tidak cocok**: Tampilan default dari UserCreationForm mungkin akan tidak sesuai dengan desain atau tampilan yang diinginkan dalam sebuah aplikasi, sehingga kita perlu melakukan kustomisasi tampilan secara mandiri agar sesuai dengan kebutuhan kita.
    - **Tidak mendukung fitur tambahan**: UserCreationForm hanya mencakup informasi dasar seperti nama pengguna(*username*) dan kata sandi(*password*). Jika kita perlu mengumpulkan informasi tambahan lainnya seperti email maka kita perlu menambahkan secara manual.

    Dapat disimpulkan, Django 'UserCreationForm' adalah alat yang kuat dan berguna untuk memulai dengan cepat dan mudah ketika mengembangkan aplikasi web dengan otentikasi pengguna. Tetapi jika kita membutuhkan komponen-komponen yang tidak tersedia maka kita harus perlu menyesuaikan atau perlu membuat formulir custom yang lebih sesuai dengan kebutuhan aplikasi.

**2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?**
    Autentikasi dan otorisasi adalah dua konsep yang sangat penting dalam pengembangan aplikasi web. Keduanya memiliki peran yang berbeda dalam menjaga keamanan dan kontrol akses ke sumber daya dalam aplikasi
    **Autentikasi**
    - **Definisi**
    Autentikasi adalah proses **memverifikasi identitas** pengguna yang mencoba mengakses suatu sistem ataupun aplikasi. Autentikasi dilakukan untuk memeriksa apakah pengguna adalah siapa yang diklaimnya (pengguna valid)
    - **Tujuan**
    Autentikasi digunakan untuk memeriksa apakah seorang pengguna telah berhasil masuk atau memiliki akun yang sah di dalam sistem. Autentikasi akan memeriksa apakah username dan password (keduanya) yang diberikan oleh pengguna cocok dengan data yang diterima dan tersimpan di dalam basis data pengguna.
    - **Cara kerja**
    Saat user memasukkan usernmae dan password saat mencoba login ke situs web, autentikasi akan memverifikasi apakah kombinasi username dan pssword sudah sesuai dengan data yang ada di database user.
    **Otorisasi**
    - **Definisi**
    Otorisasi adalah proses **mengontrol akses user** yang sudah diotentikasi ke berbagai sumber daya atau tindakan dalam aplikasi. Ini menentukan apa yang diizinkan dan dilarang oleh pengguna yang sudah terautentikasi
    - **Tujuan**
    Otorisasi digunakan untuk memastikan bahwa pengguna hanya memiliki akses ke sumber daya atau tindakan yang seharusnya mereka akses sesuai dengan peran dan izin yang telah ditetapkan untuk mereka.
    - **Cara kerja**
    Setelah user berhasil login, otorisasi akan menentukan apa yang dapat dilakukan user. Misal user hanya memiliki izin untuk melihat halaman profil mereka, sementara pengguna dengan peran admin mungkin memiliki izin untuk mengedit dan menghapus data pengguna lain.

    Proses Autentikasi dan Otorisasi penting dalam pengembangan aplikasi karena Autentikasi memastikan bahwa hanya pengguna yang memiliki akun sah yang dapat mengakses aplikasi, sementara Otorisasi memastikan bahwa pengguna hanya dapat melakukan tindakan yang sesuai dengan izin dan peran yang diberikan. Kedua hal ini membantu untuk mencegah akses yang tidak sah atau penyalahgunaan akun. Dengan adanya otorisasi kita dapat mengatur siapa saja yang dapat melakukan 'sesuatu' di dalam aplikasi yang kita buat dengan mengelola peran pengguna. Kedua konsep ini bekerja bersama untuk memastikan keamanan dan kontrol yang tepat dalam aplikasi yang kita buat. 

**3. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?**
    Cookies adalah file kecil yang disimpan di sisi klien (browser web)  saat berinteraksi dengan situs web. Cookies digunakan untuk menyimpan informasi yang dapat diakses kembali oleh situs web ketika pengguna mengunjungi situs tersebut kembali. Cookies adalah salah satu cara untuk mengelola dan menyimpan data sesi pengguna dalam konteks aplikasi web. Django menyediakan dukungan bawaan untuk mengelola cookies dan data sesi pengguna dengan cara:
    - **Cookies Sesi Django (Django Session Cookies)**:
    Django memiliki sistem sesi bawaan yang menggunakan cookies untuk mengelola data sesi pengguna. Saat pengguna pertama kali mengakses situs web yang menggunakan Django, server akan membuat ID sesi yang bersifat unik untuk pengguna tersebut. ID sesi ini disimpan dalam cookie di sisi klien. Data sesi sebenarnya disimpan di sisi server dan hanya ID sesi yang disimpan di cookie. Hal ini akan memungkinkan Django untuk mengidentifikasi pengguna ketika mereka kembali ke situs web.
    Kita dapat menyimpan data sesi pengguna dalam objek **request.session** di dalam view Django. Django otomatis akan mengelola cookie sesi dan data sesi akan terenkripsi dengan aman.
    - **Cookie Kustom (Custom Cookies)**:
    Kita dapat membuat dan mengelola cookie kustom dalam aplikasi Django, dengan ini memungkinkan kita menyimpan informasi tambahan yang perlu diakses kembali oleh aplikasi seperti informasi yang perlu dipertahankan selama sesi. Kita dapat menggunakan modul **'django.http.HttpResponse'** untuk mengatur cookies kustom dan mengambil nilai dari cookies di dalam view. 

**4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?**
    Penggunaan cookies dalam pengembangan web dapat aman jika dikelola dengan baik, tetapi juga memiliki risiko potensial yang perlu diwaspadai, yaitu:
    - **Pelacakan Pengguna**:
    Cookies dapat digunakan oleh pihak ketiga untuk melacak aktivitas pengguna di berbagai situs web lain. Hal ini dapat menghasilkan profil pengguna yang kemudian digunakan untuk tujuan iklan yang tidak diinginkan atau analisis perilaku program. 
    - **Pencurian Informasi**:
    Jika informasi bersifat sensitif seperti token otentikasi atau password  dan disimpan di dalam cookies dan cookies tersebut terpapar, informasi dapat dengan mudah dicuri oleh pihak yang tidak sah.
    - **Cookie Poisoning**:
    Penyerang dapat mencoba memanipulasi cookies dengan mengubah nilainya, yang dapat menyebabkan kerentanannya dalam aplikasi. Misal, jika sebuah website bergantung pada cookies untuk mengontrol izin pengguna, perubahan pada cookies dapat memberikan akses yang tidak sah.
    - **Cookies Tidak Terenkripsi**:
    Jika cookies mengandung informasi sensitif tidak dienkripsi, maka dapat dicuri oleh penyerang dengan mudah jika terjadi intersepsi data dalam perjalanan antara klien dan server. 
    - **Kebocoran Privasi**:
    Penyalahgunaan cookies dan pelacakan pengguna dapat mengancam privasi pengguna. 
    Untuk mengurangi risiko-risiko ini, kita harus:
    - **Gunakan HTTPS**:
    Kita harus memastikan bahwa website menggunakan HTTPS untuk mengamankan komunikasi antara klien dan server untuk mencegah penyadapan data yang tidak sah. 
    - **Enkripsi Data Sensitif**:
    Jika perlu menyimpan data sensitif dalam cookies, pastikan kita untuk mengenkripsi sebelum menyimpan dan jangan menyimpan kata sandi dalam cookies.
    - **Kendalikan Penggunaan Cookies Pihak Ketiga**:
    Pertimbangkan dampak penggunaan cookies pihak ketiga dan berikan pengguna opsi untuk menonaktifkan cookies pihak ketiga jika memungkinkan.
    - **Batasan Data yang Disimpan**:
    Hindari menyimpan data yang tidak diperlukan dalam cookies.
    - **Perbarui Cookies dengan bijak**:
    Jika kita menggunakan cookies pastikan untuk memperbarui atau menghapus setelah sesi pengguna berakhir. 

**5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**
    **Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.**
        **Fungsi dan Form Registrasi**
        - Pada views.py di subdirektori main kita membuat fungsi register yang akan menerima parameter request lalu import redirect, UserCreationForm, dan messages. 
        - Pada fungsi register ada kode yang perlu ditambahkan yang berfungsi untuk menghasilkan formulir registrasi secara otomatis dan akan menghasilkan account user ketika data di submit. Kodenya:
            def register(request):
            form = UserCreationForm()
            if request.method == "POST":
                form = UserCreationForm(request.POST)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Your account has been successfully created!')
                    return redirect('main:login')
            context = {'form':form}
            return render(request, 'register.html', context)
        - Buat berkas baru HTML dengan judul register.html pada folder main/templates.
        - Pada file urls.py di subdirektori main kita perlu impor fungsi yang baru dibuat pada views.py yaitu fungsi register serta tambahkan path url dari register ke urlpatterns
        **Fungsi Login**
        - Pada views.py di subdirektori main buat fungsi login_user yang menerima parameter  request, lalu tambahkan import authenticate dan login.
        - Pada fungsi login_user ada kode yang perlu ditambahkan yang berfungsi untuk mengautentikasi pengguna yang akan dan ingin login. Kodenya:
            def login_user(request):
            if request.method == 'POST':
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('main:show_main')
                else:
                    messages.info(request, 'Sorry, incorrect username or password. Please try again.')
            context = {}
            return render(request, 'login.html', context)
        - Buat file HTML baru dengan judul login.html pada folder main/templates
        - Pada file urls.py di subdirektori main impor fungsi yang sudah baru dibuat pada views.py yaitu fungsi login_user serta tambahkan path url dari login ke urlpatterns
        **Fungsi Logout**
        - Pada views.py di subdirektori main buat fungsi logout_user yang menerima parameter  request, lalu tambahkan import logout.
        - Pada fungsi logout_user ada kode yang perlu ditambahkan yang berfungsi untuk melakukan mekanisme logout. Kodenya:
            def logout_user(request):
            logout(request)
            return redirect('main:login')
        - Pada file main.html di folder main/templates tampah kode setelah hyperlink tag untuk add new product. Kodenya:
            <a href="{% url 'main:logout' %}">
                <button>
                    Logout
                </button>
            </a>
        - Pada file urls.py di subdirektori main impor fungsi yang sudah baru dibuat pada views.py yaitu fungsi logout_user serta tambahkan path url dari logout ke urlpatterns
        **Merestriksi Akses Halaman Main**
        - Pada views.py pada folder main tambahkan import login_required *from django.contrib.auth.decorators import login_required*, kode ini digunakan untuk mengharuskan pengguna melakukan login sebelum masuk dan mengakses halaman main sebuah web.
        - Masih pada file yang sama tambahkan kode *@login_required(login_url='/login')* di atas fungsi *show_main* agar halaman main hanya dapat diakses oleh pengguna yang telah berhasil login/terautentikasi
    **Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.** 
       **Buat akun**
       - Klik  bagian "register now"
       - Masukkan username yang diinginkan pada section "username"
       - Masukkan password yang diinginkan pada section "password"
       - Konfirmasi password pada section "Password confirmation:
       - Setelah semua diisi klik daftar
       **Login**
       - Masukkan username dan password yang sesuai lalu klik bagian login
       **Menambahkan Produk**
       - Klik bagian add new produk yang akan mengantarkan ke halaman yang berbeda
       - Masukkan nama produk, jumlah, deskripsi, harga, dan kategori sesuai yang diinginkan
       - Jika dirasa sudah sesuai klik add product, produk otomatis tersimpan dan akan kembali kehalaman main
       - Jika ingin melakukan add produk silahkan lakukan hal diatas kembali
    **Menghubungkan model Item dengan User.**
    - Pada models.py di folder main tambah kode yang akan mengimpot model dengan "from django.contrib.auth.models import User"
    - Masih di file yang sama dalam model product tambah kode "user = models.ForeignKey(User, on_delete=models.CASCADE)", kode ini berfungsi untuk menghubungkan satu produk dengan satu user melalui relationship (sebuah produk pasti terasosiasi dengan seorang user)
    - Pada views.py di folder main ubah kode pada fungsi create_product dengan:
        def create_product(request):
        form = ProductForm(request.POST or None)
        if form.is_valid() and request.method == "POST":
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return HttpResponseRedirect(reverse('main:show_main'))
        ...
    Parameter commit=False digunakan untuk mencegah Django agar tidak langsung simpan objek yg dibuat di form langsung ke database (sehingga bisa di modif sebelum di submit).
    - Masih pada file yang sama, ubah fungsi show_main:
        def show_main(request):
            products = Product.objects.filter(user=request.user)

            context = {
                'name': request.user.username,
            ...
            }
    Hal ini dilakukan untuk menampilkan objek produk yang terasosiasi dengan pengguna yang login sehingga akan menyaring seluruh objek dengan hanya mengambil produk yang sesuai dengan user yang login
    - Menyimpan perubahan dengan menjalankan python manage.py makemigrations dan pilih 1 sebanyak 2 kali (untuk menetapkan default value untuk field user pada semua row dan menetapkan user dengan ID 1)
    - Lalu jalankan python manage.py migrate
     
    **Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.**
    - Membuka file views.py pada folder main lalu tambahkan impor datetime (impor HttpResponseRedirect dan reverse sudah ada)
    - Masih di file yang sama di fungsi login_user tambahkan fungsi untuk menambahkan cookie yang bernama last_login untuk melihat kapan terakhir kali pengguna login. Dengan cara mengganti kode pada blok if user is not None:
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
    - Masih pada file yang sama di fungsi show_main, tambah kode 'last_login': request.COOKIES['last_login'] ke dalam variabel context  yang berfungsi menambahkan informasi cookie last_login pada response yang akan ditampilkan di halaman web
    - Masih pada file yang sama di fungsi logout_user dengan :
        def logout_user(request):
            logout(request)
            response = HttpResponseRedirect(reverse('main:login'))
            response.delete_cookie('last_login')
            return response
    response.delete_cookie('last_login') berfungsi untuk menghapus cookie last_login saat pengguna melakukan logou
    - Pada file main.html tambah kode diantara tabel dan tombol logout untuk menampilkan data last login:
    <h5>Sesi terakhir login: {{ last_login }}</h5>
    **Menampilkan cookie**
    - Untuk melihat data cookie last_login, kita perlu akses fitur inspect element dan buka bagian Application -> Storage. Pada bagian cookies kita dapat melihat data cookies yang tersedia selain last_login seperti sessionid dam csrftoken
    - Jika kita logout maka riwayat cookie kita yang sebelumnya hilang.