========
HomeLink Captcha
========

Captcha for HomeLink

V0.1 20140202
   * first commit
   
Captcha command
========
    #get raw images for traning
    #python getimg.py $image_number $target_dir
    python getimg.py 10 ./homelink/raw/
    
    #crop image to letters, prepare for traning
    python captcha.py      

    #get images for test
    #python getimg.py $image_number $target_dir
    python getimg.py 10 ./homelink/test/
    
    #crack image
    #python captcha $image_name
    python captcha ./homelink/test/1.jpg

