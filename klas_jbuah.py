# coding: utf-8

# **IMPORT LIBRARY**

# In[1]:


import numpy as np
import pandas as pd
from sklearn import neighbors
from termcolor import colored
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from matplotlib.colors import ListedColormap, BoundaryNorm


# **Mengambil File Data nya**

# In[2]:


file_data = pd.read_table('fruit_data.txt')  # File data jenis buah


# **Menampilkan 10 data dari tabel**

# In[3]:


print(file_data.shape)
file_data.head(10)


# **Membuat key pair (fruit_label dan fruit_name)**

# In[4]:


key_pair = dict(zip(file_data.buah_label.unique(), file_data.buah_nama.unique()))   
print(key_pair)


# **Split, Build and Train Data Jenis Buah**

# In[5]:


#explanatorynya adalah massa, lebar dan tinggi.
#Targetnya adalah fruit_label.

X = file_data[['massa', 'lebar', 'tinggi']]
y = file_data['buah_label']


# In[6]:


#Split menjadi 80% train data
#Split menjadi 20% test data 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=0)


# **Check Hasil Setelah Di Split**

# In[7]:


#Mengecek X_train, X_test, y_train, y_test kedalam bentuk dimensi array
print('X_train = ', X_train.shape)
print('X_test  = ', X_test.shape)
print('y_train = ', y_train.shape)
print('y_test  = ', y_test.shape)


# In[8]:


#Menampilkannya dalam bentuk tabel

print('Data X_train\n')
X_train.head()


# In[9]:


print('\nData y_train\n')
y_train.head()


# In[10]:


print('\nData X_test\n')
X_test.head()


# In[11]:


print('\nData y_test\n')
y_test.head()


# In[12]:


#Build model object dan train data jenis buah dengan memprediksi jarak dari 5 titik terdekat menggunakan data training

knn = KNeighborsClassifier(n_neighbors = 5)
knn.fit(X_train, y_train)


# **Mengecek besar akurasi skor menggunakan Data test**

# In[13]:


knn.score(X_test, y_test)


# **Plot batas pengklasifikasi K-NN (Visualisasi)**

# In[14]:


def plot_fruit_knn(X, y, n_neighbors, weights):
    X_mat = X[['tinggi', 'lebar']].to_numpy()
    y_mat = y.to_numpy()

    # Pewarnaan Map
    cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF','#AFAFAF'])
    cmap_bold  = ListedColormap(['#FF0000', '#F37A48', '#F7C015','#FAFA33'])

    clf = neighbors.KNeighborsClassifier(n_neighbors, weights=weights)
    clf.fit(X_mat, y_mat)
    
    mesh_step_size = .01  # Ukurang langkah
    plot_symbol_size = 50
    
    x_min, x_max = X_mat[:, 0].min() - 1, X_mat[:, 0].max() + 1
    y_min, y_max = X_mat[:, 1].min() - 1, X_mat[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, mesh_step_size),
                         np.arange(y_min, y_max, mesh_step_size))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

    # Meletakkan hasil kedalam warna plot
    Z = Z.reshape(xx.shape)
    plt.figure()
    plt.pcolormesh(xx, yy, Z, cmap=cmap_light)

    # Plot training poin
    plt.scatter(X_mat[:, 0], X_mat[:, 1], s=plot_symbol_size, c=y, cmap=cmap_bold, edgecolor = 'black')
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())

    patch0 = mpatches.Patch(color='#FF0000', label='Buah Apple')
    patch1 = mpatches.Patch(color='#F37A48', label='Buah Mandarin')
    patch2 = mpatches.Patch(color='#F7C015', label='Buah Orange')
    patch3 = mpatches.Patch(color='#FAFA33', label='Buah Lemon')
    plt.legend(handles=[patch0, patch1, patch2, patch3])

        
    plt.xlabel('Tinggi (cm)')
    plt.ylabel('Lebar (cm)')
    
    plt.show()


# In[15]:


#Plot berdasarkan height dan weight
# n_neighbors = 5 / Jarak titik terdekat | menggunakan matplotlib
plot_fruit_knn(X_train, y_train, 5, 'uniform')  


# **TESTING DATA**

# In[16]:


# prediksi jenis buah  dengan kunci itemnya -> massa Xgram, lebar Ycm and height Zcm
buah_prediksi = knn.predict([[160, 6, 8]])
print('Prediksi hasil jenis buah adalah ' + colored(key_pair[buah_prediksi[0]].upper(),'red',attrs=['bold']))


# In[ ]:




