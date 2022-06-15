import cv2

img = cv2.imread("C:\\Users\\C605\\Desktop\\losfotos\\indir.jpg")

cv2.imshow("asd",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


blue, green, red = cv2.split(img)

cv2.imshow('blue', blue)
cv2.imshow('green', green)
cv2.imshow('red', red)



print(blue)
cv2.waitKey(0)

for number in range(0,1199):
    for x in range(0,1080):
        blue[number,x] = 10


cv2.imshow('blue', blue)
asd = cv2.merge([blue,green,red])
cv2.imshow("asd",asd)
cv2.imshow("org",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
