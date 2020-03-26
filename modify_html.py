import os

def modify(filename):
    # load the file
    with open(filename,"r") as idx:
        txt = idx.read()

    dir_list = []

    # cycle through directories in data
    for data_dir in os.listdir('data/'):
        if os.path.isdir(os.path.join('data',data_dir)):
            dir_list.append(data_dir)
        
    fin = sorted(dir_list)
    latest_date = fin[-1]

    for dates in dir_list[:-1]:
        if dates in txt:
            txt = txt.replace(dates, latest_date)

    with open("index.html","w") as idx:
        idx.write(txt)

if __name__=="__main__":
    modify("index.html")