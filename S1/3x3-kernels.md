To process a kernel of 5x5 total 25 parameters to be processed, similarly for 7x7 kernel total of 49 parameters to be processed. As we move towards bigger dimentions the number of parameters to be processed also increases. Once the parameter list is huge the amount of processing time & power required will also be huge. How to reduce this processing requirement?

Use of 3x3 layers reduces the processing time significantly. For e.g. for a 7x7 kernel the 3x3 matrix can be used three times

    Perform 3x3 convolutions operations on 7x7 kernel 
         7x7 > 5x5
         5x5 > 3x3
         3x3 > 1x1
    which is using 9 + 9 + 9 = 27 parameters instead or 49 parameters

(see [7x7.gif](https://github.com/anuragal/deep-learning/blob/master/S1/7x7.gif)) to know convolution happen on 7x7 using 3x3 kernel
