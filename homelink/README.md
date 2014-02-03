========
HomeLink Spider
========

Spider for HomeLink

V0.1 20140202
   * first commit
   
Spider command
========

### scrapy shell for test xpath

```
scrapy shell "http://beijing.homelink.com.cn/sold/c1111027378318/rs铭科苑/"
```

### crawl homelink without login

```    
scrapy crawl homelink 
```    
    
### crawl homelink without login, store result into json file

```    
scrapy crawl homelink -o items.json -t json
```    

### crawl homelink after login
    
#### modify HOMELINK_USERNAME and HOMELINK_PASSWORD in settings.py
#### crawl homelink use login_spider

```
scrapy crawl login
```

#### crawl homelink use login_spider, store result into csv file

```
scrapy crawl login -o items.csv -t csv
```

