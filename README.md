# Web-Crawler
website crawler with Selenium

## The two crawler's were used to scrap real-estate information.
The code is intended to be viewed as a web-scraping referrence only.
The essential keys of deploying a successful crawler:
1. reduce the number of unnecessary calls
2. Proxy Rotation
3. user-agent rotation(less important)
4. Do not call the website too fast.
5. leave sometime for the website to render, so you can have the full elements of the target website.

## files explaination
PostCode Crawler and the cash rate crawler are the typical easy crawler's. The idea is more basic, just locate the element by CSS tags
cash rate is published by the RBA, and it is an important feature that we need for our machine learning algorithm which predicts the Real estate market.
crawler 1 is a little bit more complicated
crawler 2 is the an more advanced crawler with proxy rotation, and proxy pre-checking.
