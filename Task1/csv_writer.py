import csv

def write_data_into_csv(filename, rows, mode='w'):
    try:
        with open(filename, mode) as f:
            obj = csv.writer(f, delimiter=',')
            for row in rows:
                obj.writerow(row)
    except Exception as e:
        raise Exception("Fail to write data into CSV: Error: {}".format(e))
