# archives-scripts
Scripts I use(d) for working with archival material

IA-checker.py - Takes a txt file list of urls and checks the Internet Archive CDX API to see if they've been crawled. Outputs the url, times crawled, first date of crawl, and last date of crawl to a crawl_summary csv file. Currently breaks after a number of queries, but you can edit your url list and run the script again, starting on the url it last failed with.
