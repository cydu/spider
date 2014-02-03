========
HomeLink Spider
========

Spider for HomeLink

V0.1 20140202
   * first commit
   
Spider command
========

1. scrapy shell for test xpath

```
scrapy shell "http://beijing.homelink.com.cn/sold/c1111027378318/rs铭科苑/"
```

1. crawl homelink without login

```    
scrapy crawl homelink 
```    
    
1. crawl homelink without login, store result into json file

```    
scrapy crawl homelink -o items.json -t json
```    

1. crawl homelink after login
    1. modify HOMELINK_USERNAME and HOMELINK_PASSWORD in settings.py
    1. crawl homelink use login_spider

```
scrapy crawl login
```

    1. crawl homelink use login_spider, store result into csv file

```
scrapy crawl login -o items.csv -t csv
```

