import xml.etree.ElementTree as ET


def read_data(data_file):
    # Remove lines
    content = '<kml:kml xmlns:dwd="https://opendata.dwd.de/weather/lib/pointforecast_dwd_extension_V1_0.xsd" xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:xal="urn:oasis:names:tc:ciq:xsdschema:xAL:2.0" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom">'

    for i in range(4):
        with open(data_file, 'r') as file:
            lines = file.readlines()

        with open(data_file, 'w') as file:
            for line in lines:
                if line.strip("\n") != content:
                    file.write(line)
        print(i)
        if i == 1:
            content = '<?xml version="1.0" encoding="ISO-8859-1" standalone="yes"?>'
        if i == 2:
            content = '</kml:kml>'

    # Remove words
    with open(data_file, 'r') as file:
        lines = file.readlines()

    newlines = []
    for line in lines:
        newlines.append(line.replace('dwd:', '').replace('kml:', ''))

    with open(data_file, 'w') as file:
        for line in newlines:
            file.write(line)

    # Parse xml
    tree = ET.parse(data_file)
    root = tree.getroot()

    for child in root:
        print(child)
