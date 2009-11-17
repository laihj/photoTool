import Image
import sys
import os
import ImageDraw

ABSFILEPATH = os.path.abspath('.')


def photosave(image, filename, filepath ):
    """
        save a image in files
    """
    if not os.path.exists(ABSFILEPATH + '/'+filename):
        os.mkdir(ABSFILEPATH + '/'+filename)
    print filepath
    image.save(ABSFILEPATH + '/' + filename + '/' + filepath)

def flickrsize(image, filepath):
    """
    resize a photo for flickr upload
    """
    image = image.resize((1600, 1600*image.size[1]/image.size[0]),
                         Image.ANTIALIAS)
    photosave(image, 'flickr', filepath)
    
def blogsize(image, filepath):
    """
    resize a photo for blog post
    """
    image = image.resize((600, 600*image.size[1]/image.size[0]),
                         Image.ANTIALIAS)
    draw = ImageDraw.Draw(image)
    draw.text((0, 0), 'http://www.laihj.net')

    box = (0, image.size[1]*19/20, image.size[0], image.size[1])
    region = image.crop(box)
    region = region.convert('L')
    image.paste(region, box)
    
    del draw
    photosave(image, 'blog', filepath)

def main(argv):
    """
    main loop
    """
    for arg in argv:
        print arg
    if argv[1] == '-f':
        try:
            image = Image.open(ABSFILEPATH + '/' + argv[2])
            blogsize(image, argv[2])
            image.show()
        except Exception:
            print 'cant open'
    elif argv[1] == '-blog':
        for  name in os.listdir(os.getcwd()):
            try:
                if name[-3:] == 'jpg' or name[-3:] == 'JPG' :
                    image = Image.open(ABSFILEPATH + '/' + name)
                    blogsize(image, name)
            except Exception:
                pass        
    elif argv[1] == '-flickr':
        #for root,dirs,files in os.walk(ABSFILEPATH.join(argv[1])):
        for name in os.listdir(os.getcwd()):
            try:
                if name[-3:] == 'jpg' or name [-3:] == 'JPG' :
                    image = Image.open(ABSFILEPATH + '/' + name)
                    flickrsize(image, name)
            except Exception:
                pass
    else:
        print 'unknown parameter!'

                     
            
if __name__ == '__main__':
    main(sys.argv)




