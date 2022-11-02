import pandas as pd
import math
import scipy.stats as st
from sklearn.preprocessing import MinMaxScaler

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
pd.set_option("display.width", 600)
pd.set_option("display.expand_frame_repr", False)
pd.set_option("display.float_format", lambda x: "%.5f" % x)

df_ = pd.read_csv(r"C:\Users\hakan\PycharmProjects\Türkiye_Deprem_İnceleme\earthquake.csv")
df = df_.copy()
df.head(10)
df.isnull().sum()  # Eksik veri var mı diye bir kontrol yaptık
df.dropna(inplace=True)
df.sort_values("city", ascending=False).head(20)
df.sort_values("richter", ascending=False).head(20)
df.describe().T

df2 = df.groupby("city").agg({"richter": "mean"})
df2 = df.apply(lambda x: x.sort_values(ascending=False).head(5))  # depremlerin ortalamasını sıraladık. ilk 5'e baktık

########################PYTHON İLE VERİ GÖRSELLEŞTİRME##############################

# Değişkenler Kategorik ve Sayısal olmak üzere 2'ye ayrılmaktadır. Ve seaborn ve matplotlib ile görselleşirilebilir. Matplotlib, seaborna göre daha düşük seviyedir. Düşük seviyeden kasıt daha çok işle daha az verim almaya denir.

import seaborn as sns
import matplotlib.pyplot as plt

df.head()
df.info()  # elimizdeki değikenlerin tiplerine bakmak için kullandım. Biliyoruz ki cat ve objectler kategorik olarak geçmektedir.

########Kategorik Deişkenlerin Görselleştirilmesi:###################
# Kategorik değişkenleri görselleştirmek için yalnızca value_counts'u kullanabiliriz. Kategorik görselleştirme denilince aklımıza direkt value_counts gelmeli.
df["city"].value_counts().plot(
    kind="bar")  # Burada city kategorik değişkeninin grafiğini çizdirmek istediğimi söyleyip türünü belirttim (Bar)

plt.show(block=True)  # Daha sonra bu grafiği görmek istediğimi belirttim.(show) ile.

plt.title("Depremlerin Şehirlere Göre Dağılım Grafiği")  # Grafiğime bir başlık verdim.

df["direction"].value_counts().plot(kind="bar")
plt.show(block=True)  # Depremlerin oluş yönerline göre bir grafik çizdrmek istediğimizi söyledik.
plt.title("Depremlerin oluş yönleri")
# Depremlerin oluş yönlerine baktığımızda Batı yönünde bir eğilimin daha fazla olduğunu grafik üzerinden görebilmekteyiz.

# Sayısal Değişkenlerin Görselleştirilmesi:
# Sayısal değişkenlerin görselleştirilmesinde histogram(hist) ve boxplot yöntemi kullanılabilir.

df.info()
plt.hist(df["depth"])  # depthin grafiğini çizdrdik.
plt.show(block=True)
plt.title("Deptin Grafiği")
#
plt.hist(df["dist"])  # distlerin histogram grafiğini çizdirdik.
plt.show(block=True)
plt.title("Distin Grafiği")

# Sadece Boxplotun nasıl yapıldığının görülmesi için yapıyorum.
plt.boxplot(df["richter"])
plt.show(block=True)
plt.title("Richter'ın Boxplot Grafiği")
# Boxplot grafiği aynı histogram(hist) grafiğindeki gibi çizilmektedir. Boxplotun bazı avantajları da söz konusudur: Örneğin aykırı değerleri keşfetme konusunda veriyi inceleyenlere yardımcı olabilmektedir.

###########SUBLOTS#################
# Birden fazla tablonun aynı ekranda gelmesini sağlayabilmektedir. Bu da aynı anda iki farklı tablo incelemek isteyenler için bir kolaylık sağlamaktadır.
# örneğin derinlikle, uzaklığın şiddete nasıl etki ettiğini incelemek adına üçünü birden inceleyelim:
plt.subplot(1, 2, 1)
plt.title("Deptin Grafiği")
plt.plot(df["depth"], df["richter"])

plt.subplot(1, 2, 2)
plt.title("Distin Grafiği")
plt.plot(df["depth"], df["richter"])

################SEABORN İLE VERİ GÖRSELLEŞTİRME###############
#seaborn ile veri görselleştirebilmek için import seaborn as sns yapılmalıdır. Yani seaborn kütüphanesi import edilmelidir. Seaborn matplotun aksine yüksek sevyeli bir görselleştirme kütüphanesidir. Yani daha az çabayla daha çok iş yaptırır.
df.info()
import seaborn as sns
df["city"].value_counts()
sns.countplot(x=df["city"], data = df)
plt.show(block=True)

#seaborn ile sayısal değişkenin görselleştirilmesi:
sns.boxplot(x=df["dist"])
plt.show(block=True)





















