
Amacı:

Normalizasyon: Veri değerlerini belirli bir aralığa veya dağılıma sığdırmak için kullanılır. Genellikle veri değerlerini [0, 1] veya [-1, 1] gibi belirli bir aralığa dönüştürmeyi hedefler.
Standardizasyon: Veri değerlerini merkezileştirmek ve standart sapmaya göre ölçeklendirmek için kullanılır. Ortalamayı 0 yapar ve standart sapmayı 1 yapar.


Yöntemi:

Normalizasyon: Veri değerlerini ölçeklendirirken genellikle Min-Max ölçeklendirme veya Z-score normalizasyonu gibi yöntemler kullanılır.
Standardizasyon: Veri değerlerini ölçeklendirirken genellikle Z-score standardizasyonu veya mean normalization gibi yöntemler kullanılır.

Değerlerin Dağılımı:

Normalizasyon: Veri değerlerini belirli bir aralığa sığdırırken, orijinal veri dağılımını korumaya çalışır.
Standardizasyon: Veri değerlerini dağılımı değiştirir ve standart sapma ölçeğinde merkezileştirir.

Aykırı Değerlerin Etkisi:

Normalizasyon: Aykırı değerlerin etkisi normalizasyon işlemi sırasında daha belirgindir, çünkü değerler belirli bir aralığa sığdırılmaya çalışılırken aykırı değerler bu aralığın dışında kalabilir.
Standardizasyon: Aykırı değerlerin etkisi standardizasyon işlemi sırasında daha azdır, çünkü veri değerleri merkezlenir ve standart sapmaya göre ölçeklendirilir, bu nedenle aykırı değerlerin etkisi azalır.

Kullanım Alanları:

Normalizasyon: Makine öğrenimi algoritmalarında (örneğin, sinir ağları gibi) girdi verilerini ölçeklendirmek için sıklıkla kullanılır.
Standardizasyon: Özellik mühendisliği, PCA (Principal Component Analysis) gibi teknikler ve parametrik modeller gibi alanlarda tercih edilir.