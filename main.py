import cv2


def variance_fn(var):
    if var < 120:
        s = 'Image is Blurred'
    else:
        s = 'Image is not Blurred'
    return s

# Read the image
img = cv2.imread('image.jpg')

# Convert to greyscale
grey_1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


blurImg = cv2.blur(img,(10,10))
grey_2 = cv2.cvtColor(blurImg, cv2.COLOR_BGR2GRAY)

var_1 = cv2.Laplacian(grey_1, cv2.CV_64F).var()

var_2 = cv2.Laplacian(grey_2, cv2.CV_64F).var()

print("1st image: ",variance_fn(var_1))
