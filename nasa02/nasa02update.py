#!/usr/bin/env python3

import requests ## 3rd party URL lookup

## define the main function
def main():
    neourl = 'https://api.nasa.gov/neo/rest/v1/feed?' # API URL
    startdate = "start_date={}".format(input("Enter Start Date as yyyy-mm-dd: ")) ## start date for data
    enddate = '&end_date=END_DATE' ## create a mechanism to utilize enddate
    mykey = '&api_key=DEMO_KEY' ## replace this with our API key

    neourl = neourl + startdate + mykey

    neojson = (requests.get(neourl)).json()

    print(neojson)

def moon_lengths(missdistance):
    m_lengths = 238900

    print(missdistance/m_lengths)

    # return moon_lengths




## call main

main()

moon_lengths(1000000)


