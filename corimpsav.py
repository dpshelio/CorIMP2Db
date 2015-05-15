import datetime
from scipy.io import readsav
from sunpy.time import parse_time

def extract_dict_sav(filename):
    results = readsav(filename)
    cme_prop = results['cme_kins']
    cme_prop_dict = {key.lower():cme_prop[key][0] for key in cme_prop.dtype.names if 'UNIT' not in key}
    cme_prop_dict['event_endtime'] = parse_time(cme_prop_dict['event_endtime'])
    return cme_prop_dict


if __name__ == '__main__':
    date = datetime.datetime(2013,01,16,8,24,5)
    filename = '/tmp/cme_kins_{fit}_{date:%Y%m%d_%H%M%S}.sav'.format(fit='quadratic', date=date)
    print(extract_dict_sav(filename))

