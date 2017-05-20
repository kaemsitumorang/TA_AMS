# Word Slang Dictionary

Ini merupakan website yang memiliki fungsi sebagai kamus slang Indonesia.
Tujuan website ini adalah untuk memudahkan pengguna dalam mengetahui relasi suatu kata slang dengan kata similar yang lainnya

## Penggunaan

Ada beberapa poin yang perlu diperhatikan setelah meng-clone repo ini:
1. Versi PHP yang dimiliki harus 5.6
2. Pada app > Http > Controller.php, ada beberapa syntax yang harus diubah:
	1. Pada syntax:
		exec("/usr/local/bin/python /Users/Kaemsitumorang/TA_AMS/public/w2v.py '{$slang_word}'", $output, $return);
		Ubah path python serta file w2v.py yang terdapat di folder public
	2. Model yang digunakan pada repo ini (terdapat di Controllers.php) masih menggunakan model yang lama, file yang baru dapat diambil melai drive yang telah kami share. Replace model tersebut, dan rename sesuai nama model yang sebelumnya.
	Model yang baru terlalu besar ukurannya bila disimpan di git.


