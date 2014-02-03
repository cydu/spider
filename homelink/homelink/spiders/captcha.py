from PIL import Image
from operator import itemgetter
import hashlib
import time
import sys
import os
import math

class VectorCompare:
  def magnitude(self, concordance):
    total = 0
    for word, count in concordance.iteritems():
      total += count ** 2
    return math.sqrt(total)

  def relation(self, concordance1, concordance2):
    relevance = 0
    topvalue = 0
    for word, count in concordance1.iteritems():
      if concordance2.has_key(word):
        topvalue += count * concordance2[word]
    return topvalue / (self.magnitude(concordance1) * self.magnitude(concordance2))

class Captcha:
    def getMonochromeImage(self, img_name):
        im = Image.open(img_name)
        im = im.convert("P")
        outim = Image.new("P", im.size, 255)
        for x in range(im.size[0]):
            for y in range(im.size[1]):
                if 0 == im.getpixel((x, y)):
                    outim.putpixel((x, y), 0)
        return outim
    
    def cropLetter(self, mono_img):
        inletter = False 
        foundletter=False
        start = 0

        letters = []
        for x in range(mono_img.size[0]):
            for y in range(mono_img.size[1]):
                if mono_img.getpixel((x, y)) != 255:
                    inletter = True
            if foundletter == False and inletter == True:
                foundletter = True
                start = x
            if foundletter == True and inletter == False:
                foundletter = False
                letters.append((start, x))
            inletter = False
        
        letters_img = []
        for letter in letters:
            letters_img.append(mono_img.crop((letter[0], 0, letter[1], mono_img.size[1]))) 
        return letters_img
        
    def saveLetterImage(self, letters_img, out_dir):
        count = 0
        for img in letters_img:
            m = hashlib.md5()
            m.update("%s%s" % (time.time(), count))
            name = out_dir + "/%s_%s.gif" % (count, m.hexdigest())
            img.save(name)
            count += 1

    def buildvector(self, im):
        d1 = {}
        count = 0
        for i in im.getdata():
            d1[count] = i
            count += 1
        return d1

    def cropImage(self, img, out_dir):
        im = self.getMonochromeImage(img)
        letter_imgs = self.cropLetter(im)
        self.saveLetterImage(letter_imgs, out_dir)

    def cropImages(self, in_dir, out_dir):
        for img in os.listdir(in_dir):
            if img != "Thumbs.db" and img != ".DS_Store":
                self.cropImage(in_dir + img, out_dir)
    
    imageset = []
    def loadData(self, in_dir):
        iconset = ['0','1','2','3','4','5','6','7','8','9']
        for letter in iconset:
            for img in os.listdir(in_dir + "/%s/" % letter):
                temp = []
                if img != "Thumbs.db" and img != ".DS_Store":
                    name = in_dir + "/%s/%s" % (letter, img)
                    temp.append(self.buildvector(Image.open(name)))
                self.imageset.append({letter:temp})

    def crack(self, imgname, maxlen = 4):
        v = VectorCompare()
        im = self.getMonochromeImage(imgname)
        letter_imgs = self.cropLetter(im)
        candidates = []
        count = 0
        for img in letter_imgs:
            guess = []
            for image in self.imageset:
                for x, y in image.iteritems():
                    if len(y) != 0:
                        guess.append( (v.relation(y[0], self.buildvector(img)), x) )
            guess.sort(reverse=True)
            #print "",guess[0]
            candidates.append((guess[0][0], guess[0][1], count))
            count += 1
        candidates.sort(reverse=True)
        candidates = candidates[0:4]
        return "".join([key[1] for key in sorted(candidates, key=lambda cand: cand[2])])

if __name__ == "__main__":
    c = Captcha()
    if len(sys.argv) <= 1:
        c.cropImages("./homelink/raw/", "./homelink/")
    else:
        c.loadData("./homelink/iconset/")
        print c.crack(sys.argv[1])
