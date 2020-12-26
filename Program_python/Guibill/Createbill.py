import cv2
import argparse
import tldextract

broken_images = []
image_urls = []
templateimg = cv2.imread("/Users/pection/Documents/mn_furniture/Bill/TemplateBill.jpg")
# parser = argparse.ArgumentParser(description='This is Resize image  script')
# parser.add_argument('-i','--in',action='store',dest='input',default=None,help='<Required>image path',required=True)
# parser.add_argument('-o','--out',action='store',dest='output',default=None,help='<Required>image path',required=True)
# parser.add_argument('-wi','--width',action='store',dest='width',default=300,help='<Required>image path',required=False)
# parser.add_argument('-hi','--height',action='store',dest='height',default=300,help='<Required>image path',required=False)
# results = parser.parse_args()
# imgpath = results.input
# savepath= results.output
# width_image=results.width
# height_image=results.height
def resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    # initialize the dimensions of the image to be resized and grab the image size
    dim = None
    (h, w) = image.shape[:2]
    # if both the width and height are None, then return the original image
    if width is None and height is None:
        return image
        # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the dimensions
        r = height / float(h)
        dim = (int(w * r), height)
    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the dimensions
        r = width / float(w)
        dim = (width, int(h * r))
    # resize the image
    resized = cv2.resize(image, dim, interpolation=inter)
    # return the resized image
    return resized


print(templateimg.shape[:2])
# imgdefault=cv2.imread(imgpath,-1)

# img = resize(image=imgdefault,width=int(width_image),height=int(height_image))

# cv2.imwrite(savepath,img)
