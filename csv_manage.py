import csv

def read_csv(file):
    csv_file = open(file)
    reader = csv.reader(csv_file)
    alpha = list(reader)
    csv_file.close()
    return alpha

def write_csv(file,method,content):
    csv_file = open(file,method,newline='')
    fieldnames = content[0]
    writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(content)
    print('created csv file')
    csv_file.close()

