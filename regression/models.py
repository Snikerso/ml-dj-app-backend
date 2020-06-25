from django.db import models
from sklearn.linear_model import LinearRegression
import numpy as np
from matplotlib import image, pyplot
import PIL
from django.core.files import File
import scipy.misc
from io import BytesIO


# Create your models here.
class Image(models.Model):
    title = models.TextField(max_length=32,blank=True,null=True)
    picture_target = models.ImageField(blank=True,null=True)
    picture1 = models.ImageField(blank=True,null=True)
    picture2 = models.ImageField(blank=True,null=True)
    picture3 = models.ImageField(blank=True,null=True)
    picture4 = models.ImageField(blank=True,null=True)
    picture5 = models.ImageField(blank=True,null=True)
    picture6 = models.ImageField(blank=True,null=True)
    picture_predicted = models.ImageField(blank=True,null=True)
    beta = models.CharField(max_length=32,blank=True,null=True)
    classfied = models.CharField(max_length=200,blank=True)
    uploaded = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        try:
            lr = LinearRegression()
           
            picture_target_color = image.imread(self.picture_target)
            picture1_color = image.imread(self.picture1)
            picture2_color = image.imread(self.picture2)
            picture3_color = image.imread(self.picture3)
            picture4_color = image.imread(self.picture4)
            picture5_color = image.imread(self.picture5)
            picture6_color = image.imread(self.picture6)

            picture_list = [picture_target_color, picture1_color, picture2_color, picture3_color, picture4_color, picture5_color, picture6_color]
            list_x = [i.shape[0] for i in picture_list ]
            list_y = [i.shape[1] for i in picture_list ]

            x = [i.shape[0] for i in picture_list ]
            y = [i.shape[1] for i in picture_list ]
            x.sort()
            y.sort()
            shortest_x = x[0]
            shortest_y = y[0]


            picture_target_discolor = picture_target_color[:shortest_x,:shortest_y ,0]
            picture1_discolor = picture1_color[:shortest_x,:shortest_y ,0]
            picture2_discolor = picture2_color[:shortest_x,:shortest_y ,0]
            picture3_discolor = picture3_color[:shortest_x,:shortest_y ,0]
            picture4_discolor = picture4_color[:shortest_x,:shortest_y ,0]
            picture5_discolor = picture5_color[:shortest_x,:shortest_y ,0]
            picture6_discolor = picture6_color[:shortest_x,:shortest_y ,0]
            

            pictures = [picture_target_discolor, picture1_discolor, picture2_discolor,picture3_discolor,picture4_discolor,picture5_discolor,picture6_discolor]

            for i in pictures:
                print(i.shape)
         

            pictures_flatten=[]
            for img in pictures:
                pictures_flatten.append(img.flatten())

            characters = np.vstack((pictures_flatten))
            characters = characters.T
            
            lr.fit(characters[:,1:],characters[:,0])
            beta = lr.coef_
            intercept = lr.intercept_

            predicted_predict = beta[0] *picture1_discolor + beta[1] *picture2_discolor + beta[2]* picture3_discolor + beta[3]* picture4_discolor + beta[4]* picture5_discolor + beta[5]* picture6_discolor + intercept
            pyplot.axis('off')
            
            pyplot.imshow(predicted_predict)
            thumb_io = BytesIO()
            pyplot.savefig(thumb_io, dpi=300, bbox_inches='tight', pad_inches=0)

            im = PIL.Image.open(thumb_io)
            self.picture_predicted = File(thumb_io, name="jpg.png")

            betastring = ' '.join([str(elem) for elem in beta]) 
            self.beta = betastring


            


        except Exception as e:
            print('failed',e)
        super().save(*args, **kwargs)