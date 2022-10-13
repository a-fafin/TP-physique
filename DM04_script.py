import numpy as np

# Distance objet - écran en mm
D=np.array([ 500.,  553.,  605.,  658.,  711.,  763.,  816.,  868.,  921.,
        974., 1026., 1079., 1132., 1184., 1237., 1289., 1342., 1395.,
       1447., 1500.])

#Précision de mesure
Delta_D = 0.1

# Distance x1 entre l'objet et la lentille en mm
x1=np.array([143., 135., 130., 124., 116., 120., 114., 111., 112., 108., 114.,
       115., 112., 110., 111., 114., 114., 104., 106., 106.])
#Précision de mesure
Delta_x1=10

# Distance x2 entre l'objet et la lentille en mm
x2=np.array([ 357.,  418.,  475.,  534.,  595.,  643.,  702.,  757.,  809.,
        865.,  913.,  964., 1020., 1074., 1125., 1176., 1228., 1291.,
       1341., 1394.])
#Précision de mesure
Delta_x2=10
