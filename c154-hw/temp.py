import matplotlib.pyplot as plt

data = [[1,2,3,4,5,6,7,8,9,10 ]]
data =  [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,6,6,4,0],
    [0,0,0,0,0,0,0,0,0,0,0,6,0,0,4,0],
    [0,0,0,0,0,0,0,0,0,0,6,0,0,0,4,0],
    [0,0,0,0,0,0,0,0,0,6,0,1,0,0,4,0],
    [0,0,0,0,0,0,0,0,0,6,0,0,0,0,4,0],
    [0,0,0,0,0,0,0,0,6,0,0,0,0,4,0,0],
    [0,0,0,0,0,0,6,6,0,0,0,0,0,4,0,0],
    [0,0,0,0,0,0,6,0,0,0,0,1,0,4,0,0],
    [0,0,0,0,0,6,0,1,0,0,0,0,0,4,0,0],
    [0,0,0,0,6,0,0,0,0,1,0,0,0,4,0,0],
    [0,0,0,0,6,0,1,0,0,0,0,0,4,0,0,0],
    [0,0,0,6,0,0,0,0,0,0,0,1,4,0,0,0],
    [0,0,0,6,0,0,0,0,0,0,0,4,0,0,0,0],
    [0,0,6,0,0,0,1,0,0,0,0,4,0,0,0,0],
    [0,0,6,0,0,0,0,0,4,4,4,0,0,0,0,0],
    [0,0,4,4,4,4,4,4,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]



plt.imshow(data, cmap="nipy_spectral")
plt.show()

#import matplotlib.pyplot as plt

#data=[[4,2,3,4,5,6,7,8,9,40]]

#data=[

 #         [40,40,40,40,40,40,40,40,40,40,5,40,40,40],
#
#          [40,40,40,40,40,40,40,40,40,9,6,5,40],
#
#          [40,40,40,40,40,40,40,40,9,9,9,6,5,40],
#
#          [40,40,40,40,40,40,40,9,9,4,9,9,6,5],
#
#          [40,40,40,40,40,40,9,9,9,9,9,9,6,5],
#
#          [40,40,40,40,40,9,9,9,9,4,9,9,9,6,5],
#
#          [40,40,40,40,9,9,9,9,9,9,9,6,5,5],
#
 #         [40,40,40,9,9,9,9,4,9,9,9,6,5,5],
#
 #         [40,40,9,4,9,4,9,9,9,9,6,5,5,40],
#
 #         [40,5,6,9,9,9,9,9,9,9,9,9,6,5,40,40],
#
 #         [40,40,5,6,6,6,6,6,6,6,5,40,40,40],
#
 #         [40,40,40,5,5,5,5,5,5,5,40,40,40,40]
#
 #     ]
#
#plot.imshow(data,cmap="nipy_spectral")

#plt.show()