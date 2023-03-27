from flask import Flask, request, jsonify
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from proj_scrap_web_page.proj_scrap_web_page.spiders.spider_scrap_web_page import MySpider
import json
import logging

app = Flask(__name__)

from flask import Flask, jsonify

app = Flask(__name__)

@app.after_request
def add_cors_headers(response):
	# NEED TO ADD SPECIFIC ORGINS LATER 
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET,PUT,POST,DELETE,OPTIONS'
	#response.headers['Access-Control-Allow-Methods'] = '*'
    return response

@app.route('/scrap', methods=['POST'])
def scrapWebpage():
	request_data = request.get_json()
	# MAKE NULL CHECKS LATER
	# RETRIEVE FORM DATA - START
	reqWebsite = request_data['reqWebsite']
	reqPageURL = request_data['reqPageURL']
	url = 'https://www.tachyonsys.com.au/company/about-us'
	process = CrawlerProcess(get_project_settings())
	#spider_args = {'url': 'https://www.tachyonsys.com.au/company/about-us'}
	#spider = MySpider(url='https://www.tachyonsys.com.au/company/about-us')
	process.crawl(MySpider, url='https://www.tachyonsys.com.au/company/about-us')
	#app.logger.info(reqPageURL)
	process.start()
	return jsonify({'resWebsite': reqWebsite},{'resPageURL': reqPageURL})
	
if __name__ == '__main__':
   app.run(debug=True)
    

