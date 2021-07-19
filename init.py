# "https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/daily/more_precip/recent/tageswerte_RR_01046_akt.zip"

file_name = "./tageswerte_RR_01046_akt/produkt_nieder_tag_20200115_20210717_01046.txt"
the_list = []

with open(file_name) as f:
    # ignore the first line
    next(f)

    #create a list of the lines where each element is a line
    # e.g [       1046;20200117;    9;   0.2;   4;   0;   0;eor]
    lines = f.readlines()
    for line in lines :
        item = {}
        # use split to divide the line into a list of elements separated by space charecter
        # the result will be something like ['1046;20200625;', '9;', '0.0;', '0;-999;-999;eor']
        detailed_line= line.split()
        # the enumerate will give us a loop with the index
        for index, value in enumerate(detailed_line):
            if index == 0 :
                item['date'] =  value.split(';')[1]
            if index == 2:
                item['rs'] = value.split(';')[0]

        the_list.append(item)

# import pdb; pdb.set_trace()

#the output is a list of objects, each object contains the data and the value of rain level
print(the_list)
