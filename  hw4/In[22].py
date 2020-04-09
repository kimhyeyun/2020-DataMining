import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import inline
import numpy as np
from sklearn.decomposition import PCA

numImages = 16
imgData = np.zeros(shape=(numImages,36963))

for i in range(1,numImages+1):
    filename = 'pics/Picture'+str(i)+'.png'
    img = mpimg.imread(filename)
    imgData[i-1] = np.array(img.flatten()).reshape(1,img.shape[0]*img.shape[1]*img.shape[2])

numComponents = 2
pca = PCA(n_components=numComponents)
pca.fit(imgData)

projected = pca.transform(imgData)
projected = pd.DataFrame(projected,columns=['pc1','pc2'],index=range(1,numImages+1))
projected['food'] = ['burger','burger','burger','burger','drink','drink','drink','drink',
                     'pasta','pasta','pasta','pasta','chicken','chicken','chicken','chicken']

colors = {'burger':'b','drink':'r','pasta':'g','chicken':'k'}
markerTypes = {'burger':'+','drink':'x','pasta':'o','chicken':'s'}

for foodType in markerTypes:
    d = projected[projected['food']==foodType]
    a = plt.scatter(d['pc1'],d['pc2'],c=colors[foodType],s=60,marker=markerTypes[foodType])

plt.show(a)
