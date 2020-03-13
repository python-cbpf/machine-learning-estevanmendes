from mnist import MNIST
import numpy as np
class IMAGES():
    def __init__(self):
        mnist = MNIST('../dataset/MNIST')
        self.x_train, self.y_train = mnist.load_training() #60000 samples
        self.x_test, self.y_test = mnist.load_testing()    #10000 samples
    def IMAGES_IN_ARRAY(self):
        x_train = np.asarray(self.x_train).astype(np.float32)
        y_train = np.asarray(self.y_train).astype(np.int32)
        x_test = np.asarray(self.x_test).astype(np.float32)
        y_test = np.asarray(self.y_test).astype(np.int32)
        return x_train,y_train,x_test,y_test