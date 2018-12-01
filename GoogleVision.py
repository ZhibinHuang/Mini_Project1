import io
import os
import PIL
import mysql
import mongodb
import twAPIexample
import getpic

def googlevision(user,twname,picappend):
    # Imports the Google Cloud client library
    from google.cloud import vision
    from google.cloud.vision import types
    from PIL import Image, ImageFont, ImageDraw, ImageFont
    twinum = twAPIexample.get_all_tweets(twname)
    getpic.getpic(picappend)

    tmp_dict = dict()
    x = 0
    path = '/Users/huang/Documents/tw/twipic0'
    path_list=os.listdir(path)
    path_list.sort()
    for filename in path_list:
        tmp_dict[x] = os.path.join(path, filename)
        x = x+1
        #print(os.path.join(path, filename) )
    picnum = (len([name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))]))

    vidaddr = '/Users/huang/Documents/tw/test0.mp4'

    print('You have download %s photos from twitter %s \n' %(picnum-1,twname))

    x = 1
    while (x < picnum):
        st = ''
        # Instantiates a client
        client = vision.ImageAnnotatorClient()

        # The name of the image file to annotate
        file_name = os.path.join(
            os.path.dirname(__file__),tmp_dict[x])

        # Loads the image into memory
        with io.open(file_name, 'rb') as image_file:
            content = image_file.read()

        image = types.Image(content=content)

        # Performs label detection on the image file
        response = client.label_detection(image=image)
        labels = response.label_annotations

        tag = dict()
        y = 0

        for label in labels:
            # print(label.description)
            tag[y] = label.description
            y = y + 1

        im = Image.open(tmp_dict[x])
        #print(im.format, im.size, im.mode)
        ttfront = ImageFont.truetype("/Users/huang/Documents/tw/cmr10.ttf", 50)
        draw = ImageDraw.Draw(im)
        y = 0
        #print(len(tag))
        while(y<len(tag)):
            draw.text((10, 10+50*y), tag[y], fill=(255, 0, 0), font=ttfront)
            if(y == len(tag)-1):
                st = st + tag[y] +'.'
            else:
                st = st + tag[y] +','
            y = y+1

        im.save(tmp_dict[x])

        #print(st)
        mysql.opt_mysql(user,'twitter',x,twname,st,twinum,picnum-1,tmp_dict[x],vidaddr)
        mongodb.opt_mongodb(user,'twitter',x,twname,st,twinum,picnum-1,tmp_dict[x],vidaddr)
        x = x+1

    #im.show()
    #print(tmp_dict[0])
    #print(tag)

if __name__ == '__main__':
    googlevision('Echooo','StephenCurry30',0)
    #mysql.opt_mysql('Echo','twitter',0, 'Josh', 'GAP', 77, 17, 'cpan', 'dpan')
    #mongodb.opt_mongodb('Echo','twitter',7,'Josh','Gap',2,3,'cpan','dpan')
    #os.system("./ffmpeg -y -r 1 -i twipic0/%02d.jpg -vcodec libx264 -r 1 -t 15 -b 200k test0.mp4")