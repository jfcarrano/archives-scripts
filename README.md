# archives-scripts
Scripts I use(d) for working with archival material

## IA-checker.py
Takes a txt file list of urls and checks the Internet Archive CDX API to see if they've been crawled. Outputs the url, times crawled, first date of crawl, and last date of crawl to a crawl_summary csv file. Currently breaks after a number of queries, but you can edit your url list and run the script again, starting on the url it last failed with.

## InstArch_regex.txt
File with regular expressions for use with bulk_extractor to look for sensitive, private, or confidential records, focusing on MIT Institute Archives collections. Adapted from [Duke's (thanks farrell)](https://github.com/laissezfarrell/rl-bitcurator-scripts/tree/master/be_regex), converted terms from some [ePADD lexicons](https://library.stanford.edu/projects/epadd/community/lexicon-working-group), and additional terms added or modified.

## OldscanRepackr.py
Input a directory and it rearranges the files and folders into a structure that can be properly parsed by Archivematica as digitization output. This works for a bespoke use case for MIT based on improperly structured legacy scanning output. Movement of files defaults to rsync for non-Windows systems and shutil.move for Windows.
