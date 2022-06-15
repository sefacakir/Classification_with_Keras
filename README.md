# Python Tensorflow.Keras ile Görüntü Sınıflandırma
Python programlama dili ve Tensorflow kütüphanesi ile görüntülerin sağ göz kırpma, sol göz kırpma ve gözlerini kapatma gibi göz hareketlerini algılayan; sağ göz kırpıldıpında ses açıp, sol göz kırpıldığında sesi kısan, gözlerin kapalı olması durumunda ise sesi tamamen açan veya kapatan bir proje geliştirilmiştir.

Proje de VGG16 mimarisi kullanılarak imagenet veriseti ile transfer öğrenme yapılmış, daha sonra eklenen bir ara katman ve çıktı katmanı ile de model oluşturulmuştur. Modelin eğitiminde stock fotoğraflar ve kameradan çekilen fotoğraflar kullanılmıştır.

![Closed (2)](https://user-images.githubusercontent.com/55946046/173818981-70de168e-80f6-4ea0-bba7-0f74261161ae.jpg) ![Left (4)](https://user-images.githubusercontent.com/55946046/173819204-964bb7d2-4c9d-46af-b5c0-0f773ca04038.jpg) ![Right (3)](https://user-images.githubusercontent.com/55946046/173819442-6a240619-d0c2-4605-a04f-c057e737701f.jpg)

Göz kırpma durumlarında sesin açılıp kapanmaması için belirli bir miktar gözleri kapalı tutmak gerekiyor.

### Sağ Göz Kırpılma Durumu
![sağ](https://user-images.githubusercontent.com/55946046/173820494-c3c61fed-9040-4f14-9406-c5d106f85a8f.jpg)

### Sol Göz Kırpılma Durumu
![sol](https://user-images.githubusercontent.com/55946046/173820566-fd51eb2d-a8a5-4395-a809-879343b0f21e.jpg)

### Göz Kırpma Durumunda Görüntü
![kapalı](https://user-images.githubusercontent.com/55946046/173822728-1ee398d8-7b71-4563-815d-a62825d56297.jpg)

### Gözlerin Kapatılması Durumunda Görüntü
![kapali](https://user-images.githubusercontent.com/55946046/173822945-3ca42c59-fac0-4e2b-88af-aa3728d3d80d.jpg)
