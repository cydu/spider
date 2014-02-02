========
HomeLink Spider
========

Spider for HomeLink

V0.1 20140202
   * first commit
   
Spider command
========
    
    #scrapy shell for test xpath
    scrapy shell "http://beijing.homelink.com.cn/sold/c1111027378318/rs铭科苑/"

    #crawl homelink  
    scrapy crawl homelink 
    
    #crawl homelink & store result to json
    scrapy crawl homelink -o items.json -t json

