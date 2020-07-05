from .models import Song
import csv

def load_csv_file(path):
    with open(path) as file_obj:
        reader = csv.reader(file_obj)
        data = []
        for row in reader:
            flag = 0
            if data == []:
                data.append(row)
                continue
            for d in data:
                if row[0] in d:
                    mid = row[1].split("|")
                    for i in mid:
                        if i in d[1] and row.count("") > d.count(""):
                            flag = 1
                            break
            if flag == 0:
                for d in data:
                    if row[0] in d:
                        data.remove(d)
                        break
                data.append(row)
        for d in data:
            if "title" in d[0]:
                continue
            try:
                Song.objects.get_or_create(
                    title = d[0],
                    contributor = d[1],
                    iswc = d[2]
                )
            except:
                continue  