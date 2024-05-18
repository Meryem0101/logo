import cv2
import numpy as np
# créer une canevas de couleur blanche
canevas = np.zeros((580, 580, 3), np.uint8)
canevas[:] = 255, 255, 255



#premier A:
pts=np.array([[170,200],[150,200],[170,150],[197,225],[208,225],[170,120],[138,210],[175,210]],dtype=np.int32)


cv2.polylines(canevas, [pts], isClosed=True, color=(0,0,0), thickness=2)

cv2.fillPoly(canevas, [pts], color=(0, 0, 0))
 
#Le I:
pts_rect=np.array([[213,208],[223,208],[223,144],[213,144]])
cv2.polylines(canevas, [pts_rect], isClosed=True, color=(0,0,0), thickness=2)
cv2.fillPoly(canevas, [pts_rect], color=(0, 0, 0))
#deuxieme A:
pts_tr1=np.array([[245,200],[285,200],[265,150]],dtype=np.int32)
pts_tr2=np.array([[233,210],[297,210],[265,120]],dtype=np.int32)

cv2.polylines(canevas, [pts_tr1], isClosed=True, color=(191, 157, 4), thickness=2)
cv2.polylines(canevas, [pts_tr2], isClosed=True, color=(191, 157, 4), thickness=2)

cv2.fillPoly(canevas, [pts_tr2, pts_tr1], color=(191, 157, 4))

#dessiner C:
cv2.ellipse(canevas,(335,174),(30,30),0,40,320,(0,0,0),thickness=14)

# Écrire le texte sur l'image
text="ASIAN INTERNATIONAL ARBITRATION CENTER"
cv2.putText(canevas, text, [130,240],cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0,0,0), thickness=1,lineType=cv2.LINE_AA)
cv2.imshow("canevas", canevas)

cv2.waitKey(0)
cv2.destroyAllWindows()