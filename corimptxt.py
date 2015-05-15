# Read files from

def extract_datapoints(filename):
    with open(filename, 'r') as result:
        all_lines = result.readlines()

    datapoints = [a for a in all_lines if not a.startswith('#')]
    return len(datapoints)
# starttime = datetime.datetime.strptime(os.path.basename(filename), 'cme_kins_%Y%m%d_%H%M%S.txt')
# endtime = parse_time(' '.join(all_lines[-1].split()[0:2]))
# values = [a.splitlines()[0] for a in all_lines if a.startswith('#') and a.count(':')]
# event = {aa.rsplit(':')[0].split('# ')[1]:aa.rsplit(':')[1] for aa in values}
# print(values)

if __name__ == '__main__':
    filename = '/tmp/cme_kins_20130116_101206.txt'
    print(extract_datapoints(filename))
