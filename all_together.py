import urllib
import datetime
import os

from sunpy.util import scraper

from corimpsav import extract_dict_sav
from corimptxt import extract_datapoints
from database import start_db, Detection

pattern = "http://alshamess.ifa.hawaii.edu/CORIMP/%Y/%m/%d/cme_kins/cme_kins_{filter}_%Y%m%d_%H%M%S.sav"
tstart = datetime.datetime(2000,1,1)

# database creation
session = start_db()

while tstart < datetime.datetime.utcnow():
    tend = tstart + datetime.timedelta(days=10)
    print(tstart, tend)
    for filter in ['linear', 'quadratic', 'savgol']:
        scrap = scraper.Scraper(pattern, filter=filter)
        urls = scrap.filelist(tstart, tend)
        for url in urls:
            print(url)
            filename_sav = urllib.urlretrieve(url)
            cme_dict = extract_dict_sav(filename_sav[0])
            filename_txt = urllib.urlretrieve(url.replace('sav', 'txt'))
            # add to cme_dict the number of datapoints
            cme_dict['filename'] = os.path.basename(url)
            cme_dict['event_starttime'] = datetime.datetime.strptime(cme_dict['filename'],'cme_kins_'+filter+'_%Y%m%d_%H%M%S.sav')
            cme_dict['datapoints'] = extract_datapoints(filename_txt[0])
            cme_dict['fit_used'] = filter
            detection = Detection(**cme_dict)
            session.add(detection)
        session.commit()
    tstart = tend

