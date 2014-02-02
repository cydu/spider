========
HomeLink Captcha
========

Captcha for HomeLink

V0.1 20140202
   * first commit
   
Captcha command
========

1. get raw images for traning

    #python getimg.py $image_number $target_dir
    python getimg.py 10 ./homelink/raw/
    
1. crop image to letters, prepare for traning

    python captcha.py      
    
1. examine and verify letters
    
    #move every letter image into iconset

1. get images for test

    #python getimg.py $image_number $target_dir
    python getimg.py 10 ./homelink/test/
    
1. crack image

    #python captcha $image_name
    python captcha ./homelink/test/1.jpg

