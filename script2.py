import pandas as pd
import requests
from bs4 import BeautifulSoup
import itertools
import json
import os.path

save_path = 'E:\Python\FiverrWork\BBCHeadLines\BBCHead\local'

url = "https://web.archive.org/__wb/calendarcaptures?url=http%3A%2F%2Fwww.bbc.com%2Fnews&selected_year=2018"
lm_json = requests.get(url)
j = lm_json.json()
count = 0
for m in range(0, 11):
    for w in range(0, 4):
        for d in range(0, 6):
            if j[m] is not None and j[m][w] is not None and j[m][w][d] is not None:
                ts = j[m][w][d]
                if ts != None:
                    try:
                        length = len(ts.get('ts'))
                    except:
                        continue
                    for n in range(length):
                        try:
                            merged = ts.get('ts')[n]
                            BASE_URL = "https://web.archive.org/web/%s/http://www.bbc.com/news" % merged
                            print(BASE_URL)
                            r = requests.get(BASE_URL)
                        except:
                            continue
                        c = r.content
                        soup = BeautifulSoup(c, "html.parser")
                        # findall ".gel-pica-bold,.gel-great-primer-bold,.gel-paragon-bold"
                        topst = soup.select(
                            '.nw-c-top-stories h3.gel-paragon-bold,.nw-c-top-stories h3.gel-pica-bold,.nw-c-top-stories h3.gel-great-primer-bold')
                        relatetop = soup.select('.nw-c-related-story span.gs-u-align-bottom')
                        mustc = soup.select('.nw-c-must-see h3.gel-double-pica-bold,.nw-c-must-see h3.gel-pica-bold')
                        mwatched = soup.select('.nw-c-most-watched span.gel-pica-bold')
                        fstory = soup.select(
                            '.nw-c-full-story h3.gel-pica-bold,.nw-c-full-story h3.gel-double-pica-bold')
                        longr = soup.select('.nw-c-cluster3 h3.gel-pica-bold')
                        mostr = soup.select('.nw-c-most-read span.gel-pica-bold')
                        abbc = soup.select(
                            '.nw-c-around-the-bbc h3.gel-pica-bold,.nw-c-around-the-bbc h3.gel-double-pica-bold')
                        sport = soup.select('.nw-c-sport h3.gel-pica-bold,.nw-c-sport h3.gel-double-pica-bold')
                        newsbeat = soup.select('.nw-c-Newsbeat h3.gel-pica-bold')

                        # get the headlines from html element
                        headlines = [a.getText() for a in
                                     itertools.chain(topst, relatetop, mustc, mwatched, fstory, longr, mostr, abbc,
                                                     sport, newsbeat)]

                        # remove default bbc broadcast text
                        # headlines.remove('BBC World News TV')
                        # headlines.remove('BBC World Service Radio')

                        # convert it pandas dataframe
                        df = pd.DataFrame({'HeadLines': headlines})
                        # os.path.join(save_path, name_of_file + ".txt")
                        df.to_csv(os.path.join(save_path, "2018"+str(count)+ ".txt"))
                        count += 1