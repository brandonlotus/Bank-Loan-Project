# Bank Loan Status Prediction
<img src="https://github.com/brandonlotus/FinalProject-BankLoan/blob/main/templates/images/loan.jpg">

## Background
Meningkatnya pengajuan pinjaman di bank dapat mengakibatkan masalah karena memiliki resiko yaitu Non-performing loan (NPL) atau kredit macet. NPL masih menjadi masalah utama di sektor perbankan dalam kurun waktu beberapa dekade terakhir.
Penyebab paling sering tingginya NPL adalah kegagalan bank untuk mengidentifikasi serta memberikan keputusan debitur mana yang pantas dan mampu diberikan pinjaman.
Di sisi lain, bank yang terlalu mengejar target penyaluran kredit menyebabkan pihak bank kurang memperhatikan aspek analisis kredit, seperti pengelolaan informasi yang kurang baik, kurang efektifnya kebijakan dalam pemberian kredit, dan SOP analisis kredit yang buruk.
## Problems
* Apakah faktor-faktor yang dapat mengidentifikasi peminjam yang bisa / tidak melunasi pinjamannya?
* Bagaimana mengurangi resiko kerugian bank yang disebakan oleh peminjam yang tidak melunasi pinjamannya?
## Goals
* Mengidentifikasi faktor-faktor seorang peminjam bisa / tidak melunasi pinjamannya.
* Membuat model untuk memprediksi apakah peminjam akan membayar kembali pinjamannya berdasarkan fitur target 'Loan Status' dalam dataset.
## Workflow
* Data Cleaning and Preprocessing (Handle Missing Values, Outliers)
* Exploratory Data Analysis and Visualization (Univariate, Multivariate, Insights)
* Feature Engineering and Selection (Encoding, Handle imbalance, Scaling)
* Machine Learning Modelling (Logistic Regression, Random Forest, XGBoost, Hyperparameter Tuning)
* Evaluation Metrics and Comparison 
* Create Dashboard (Prediction, Dataset, Visualization)
* Conclusion and Recommendation
## Dataset
<img src="https://github.com/brandonlotus/FinalProject-BankLoan/blob/main/templates/images/data.jpg" width="800">

## Evaluation Matrix Comparison
<img src="https://github.com/brandonlotus/FinalProject-BankLoan/blob/main/templates/images/eval_01.jpg" width="800">
<img src="https://github.com/brandonlotus/FinalProject-BankLoan/blob/main/templates/images/eval_02.jpg" width="800">

## Conclusion
1. 26,7% dari peminjam tidak melunasi pinjamanan, dibandingkan 73,3% yang lunas.
2. 75% jumlah pinjaman berada dalam range 100-250 ribu. Semakin besar jumlah pinjaman, semakin besar juga kemungkinan pinjaman tidak lunas.
3. 49% penghasilan tahunan peminjam berada di range 1-1,5 juta. Semakin besar penghasilan tahunan peminjam, semakin besar kemungkinan pinjaman lunas.
4. 64% peminjam memiliki riwayat kredit 15 tahun keatas. Semakin lama riwayat kredit peminjam, semakin besar kemungkinan pinjaman lunas.
5. Mayoritas pinjaman bersifat short term (74%) dibandingkan pinjaman long term (26%). Pinjaman berjangka panjang / long term (38%) lebih tinggi tingkat charged off dibanding short term (23%).
6. Mayoritas peminjam berada dalam kategori credit score Good 670-739 (76,5%), hanya 5,3% dalam kategori Fair 580-669. Persentase charged off di kategori credit score Good (29%), lebih rendah dari kategori Fair yang mencapai 43%. Semakin tinggi credit score peminjam semakin besar kemungkinan pinjaman lunas.
7. Hampir setengah peminjam (49%) menjadikan rumahnya sebagai jaminan pinjaman, sedangkan 42% masih menyewa rumah. Peminjam yang menjaminkan rumahnya memiliki kemungkinan charged off (24%), lebih rendah dari yang menyewa rumah (30%)
8. Sebagian besar tujuan pinjaman adalah untuk konsolidasi hutang (79%).
9. Secara keseluruhan, indikasi suatu pinjaman tidak dilunasi memiliki faktor-faktor berikut: jumlah pinjaman diatas 500 ribu, penghasilan tahunan dibawah 500 ribu, credit history rendah, pinjaman jangka panjang, credit score fair dan peminjam masih menyewa rumah.
10. Model machine learning Random Forest setelah dilakukan hyperparameter tuning memiliki Precision Score 0,8 (80%) dan nilai False Positive paling rendah. Evaluation metric yang difokuskan adalah Precision Score karena yang diutamakan adalah meminimalisir False Positive (aktual charged off, tetapi diprediksi fully paid). Hal ini untuk menghindari resiko kerugian bank apabila peminjam tidak dapat melunasi pinjamannya.
## Recommendation
Model machine learning dapat diterapkan pada dashboard divisi peminjaman bank untuk membantu proses assessment pinjaman sebelum disetujui. Model akan melakukan klasifikasi antara peminjam yang akan melunasi pinjaman atau yang akan menjadi pinjaman gagal. Penggunaan machine learning dapat mempercepat proses assessment dan mengurangi resiko pinjaman yang tidak lunas.
## Dashboard
<img src="https://github.com/brandonlotus/FinalProject-BankLoan/blob/main/templates/images/dash_dat.jpg" width="800">
<br>
<img src="https://github.com/brandonlotus/FinalProject-BankLoan/blob/main/templates/images/dash_pred.jpg" width="800">
<br>
<img src="https://github.com/brandonlotus/FinalProject-BankLoan/blob/main/templates/images/dash_res.jpg" width="800">
<br>

