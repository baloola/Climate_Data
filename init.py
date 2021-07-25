import os
import urllib
import zipfile
import datetime
stations = ["01048","01050","01051","01693"]
st_id = 0 # starting from the first station
while st_id < len(stations):
    # for every station there is a different url containing the station's ID
    url = f"https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/daily/more_precip/recent/tageswerte_RR_{stations[st_id]}_akt.zip"
    # creating a folder that contains a sperate file for each weather station zip data downloaded
    file_path = os.path.join("Climate Data", f"Precipitation_{stations[st_id]}")
    os.makedirs(file_path, exist_ok= True)
    zip_path = os.path.join(file_path, f"produkt_nieder_tag_{stations[st_id]}")
    urllib.request.urlretrieve(url,zip_path)
    # unzipping downloaded data
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(file_path)
    # the file name changes everyday with by including the date of yesterday
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    yesterday = yesterday.strftime('20%y%m%d') # formating
    yesterday = str(yesterday)
    file_name = f"produkt_nieder_tag_20200122_{yesterday}_{stations[st_id]}.txt"
    file_name = str(file_name)
    the_list = []
    with open(file_path + "\\" + file_name) as f:
        next(f)
        lines = f.readlines()
        for line in lines :
            item = {}
            detailed_line= line.split(";")
            detailed_line = [x.strip(' ') for x in detailed_line] 
        # use split to divide the line into a list of elements separated by ; and striping away space
        # the enumerate will index all lists items
            for index, value in enumerate(detailed_line):
                if index == 1 :
                    item['date'] = value.split()[0]
                if index == 3:
                    item['rs'] = value.split()[0]
                the_list.append(item)
    st_id = st_id + 1
    print (file_name)
    #print(the_list)
# # import pdb; pdb.set_trace()
#the output is a list of objects, each object contains the data and the value of rain level
