# "https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/daily/more_precip/recent/tageswerte_RR_01046_akt.zip"

file_name = "./tageswerte_RR_01046_akt/produkt_nieder_tag_20200115_20210717_01046.txt"
the_list = []

with open(file_name) as f:
    next(f)
    lines = f.readlines()
    for line in lines :
        item ={}
        detailed_line= line.split()
        for index, value in enumerate(detailed_line):
            if index == 0 :
                item['date'] =  value.split(';')[1]
            if index == 2:
                item['rs'] = value.split(';')[0]

        the_list.append(item)
import pdb; pdb.set_trace()
print(the_list)
