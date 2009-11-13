import Image
import sys
import os
import ImageDraw

absFilePath = os.path.abspath('.')

def flickrSize(image,filepath)
    image = image.resize((1600,1600*image.size[1]/image.size[0]),Image.ANTIALIAS)
    if not os.path.exists(absFilePath + '/flickr'):
        os.mkdir(absFilePath + '/flickr')
    print filepath
    image.save(absFilePath + '/flickr/' + filepath)

def blogSize(image,filepath):
    image = image.resize((600,600*image.size[1]/image.size[0]),Image.ANTIALIAS)
    draw = ImageDraw.Draw(image)
    draw.text((0,0),'http://www.laihj.net')

    box = (0,image.size[1]*19/20,image.size[0],image.size[1])
    region = image.crop(box)
    region = region.convert('L')
    image.paste(region,box)
    
    del draw
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
    elif argv[1] == '-ff':
        try:
            if name[-3:] == 'jpg' :
                    im = Image.open(absFilePath + '/' + name)
                    flickrSize(im,name)
                    print(absFilePath + '/' + name)
            except:
                print Exception 
        
    else:
        #for root,dirs,files in os.walk(absFilePath.join(argv[1])):
        for name in os.listdir(os.getcwd()):
            try:
                if name[-3:] == 'jpg' :
                    im = Image.open(absFilePath + '/' + name)
                    blogSize(im,name)
                    print(absFilePath + '/' + name)
            except:
                print Exception

                     
            
if __name__ == '__main__':
    main(sys.argv)
