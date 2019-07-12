from PIL import Image
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import cv2
from skimage import data
from skimage.filters import threshold_otsu, threshold_adaptive
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt 
import os
import convolucion as ced
from PIL import Image

    
def rgb2gray(rgb):

    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b

    return gray

def load_data(dir_name = 'input/SURPRISE/'):    
    
    for filename in os.listdir(dir_name):
        if os.path.isfile(dir_name + '/' + filename):
            
            image = img = cv2.imread(dir_name + '/' + filename,0)
            global_thresh = threshold_otsu(image)
            binary_global = image > global_thresh
            
            block_size = 35
            binary_adaptive = threshold_adaptive(image, block_size, offset=15)
            
            fig, axes = plt.subplots(nrows=3, figsize=(7, 8))
            ax0, ax1, ax2 = axes
            plt.gray()
            
            #ax2.imshow(binary_adaptive)
            #ax2.set_title('Adaptive thresholding')
            #imgs.append(img)
            plt.imsave('output/'+ 'F'+filename, np.array(binary_adaptive), cmap=cm.gray)
            for ax in axes:
                ax.axis('off')
            

load_data()
