# Kelompok_2
# UAS Pemrosesan Paralel 

Berikut adalah Dokumentasi dari program yang sudah dibuat :
Tujuan program :
  - Program dapat mengirimkan perintah serta dapat menjalankannya ke node-node tujuan melalui controller
  - Controller dapat terkoneksi ke node-node yang tersedia
  
Adapun dalam pembuatan program tersebut terdapat beberapa library yang dibutuhkan, Diantaranya :
  - Controller : System,sys,Paramiko,Json
  - Node       : os,json
  
## Alur
- User memasukkan perintah dengan memilih menu yang sudah tersedia (node,bangun datar, operasi perhitungan)
- Pada saat melakukan inputan, user dapat memilih lebih dari satu pilihan dalam satu kategori dangan delimitry menggunakan ";" (Ex: 1;2)
- Setelah user melakukan inputan, maka iputan tersebut akan di cek validasinya pada setiap kategori, dimana validasi tersebut terdapat pada function validateNode(),validateBd() dan validateFm()
- Apabila inputan benar, maka user akan melakukan proses selanjutnya sesuai dengan urutannya. dan apabila tidak sesuai maka user akan diberikan pilihan untuk mengulangi atau tidak dengan memanggil function loop_app()
- user mamasukkan data bangun datar yang sudah dipilih yang kemudian akan dihitung 
- selanjutnya data akan divalidasi dan kemudian akan dikirm ke node yang dituju yang terdapat pada function prepareData() dan sendRequestToNode()
- pada saat pengiriman, data yang dimasukkan masih dalam bentuk dictionary sehingga data yang diinputkan harus diubah ke dalam tipe string.
- kemudian didalam node, data yang sudah dikirmkan akan diubah kembali kedalam bentuk dictionary
- saat merubah data dari string ke dictionary tersebut, menggunakan library JSON dengan menggunakan json.dumps() kemudian diubah ke bentuk dictionary menggunakan json.loads()

Note :
- username dan password controller dan node sama
