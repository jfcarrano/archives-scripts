import json
import requests
import time
import csv

fname = input('Enter file name: ')
url_list = open(fname)
crawlsum_csv = 'crawl_summary.csv'
crawlsum = open(crawlsum_csv, "w", newline='')
crawlsum_csv = csv.writer(crawlsum, delimiter=',')

for the_url in url_list:
    results_list = []
    the_apiurl = 'http://web.archive.org/cdx/search/cdx?url=' + str(the_url.rstrip()) + '&output=json'''
    response = requests.get(the_apiurl)
    json_data = json.loads(response.text)
    if not json_data:
        results_list.append([the_url.rstrip(), '0'])
    else:
        times_crawled = []
        for line in json_data:
            if line[4] == '200': times_crawled.append(line[1])
        if times_crawled:
            firstdate = min(times_crawled)
            lastdate = max(times_crawled)
        results_list.append([the_url.rstrip(), len(times_crawled), firstdate, lastdate])
    time.sleep(5)
    crawlsum_csv.writerows(results_list)
