import Image
import sys
import os

absFilePath = os.path.abspath('.')

def blogSize(image,filepath):
    image = image.resize((600,600*image.size[1]/image.size[0]),Image.NEAREST)
    if not os.path.exists(absFilePath + '/blog'):
        os.mkdir(absFilePath + '/blog')
    print filepath
    image.save(absFilePath + '/blog/' + filepath)

def main(argv):
    for arg in argv:
        print arg
    if argv[1] == '-f':
        print 'afile'
        try:
            im = Image.open(absFilePath + '/' + argv[2])
            blogSize(im,argv[2])
        except:
            pass
    else:
        #for root,dirs,files in os.walk(absFilePath.join(argv[1])):
        for name in ['IMG_0896.JPG','IMG_0900.JPG']:
            try:
                im = Image.open(absFIlePath + '/' + name)
                blogSize(im,name)
                print(absFilePath + '/' + name)
            except:
                continue

                     
            
if __name__ == '__main__':
    main(sys.argv)
