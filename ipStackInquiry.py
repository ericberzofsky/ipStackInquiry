####################################################
# Script to connect to ipStack.com with specified
# IP address and extract lat/long
####################################################
import argparse
import json
import urllib.request

####################################################
# TODO: Ideally, this access key should be stored
# in a read-only file, and read in by this script,
# so that its use can be controlled
####################################################

ACCESS_KEY = "8be7f45a4cbfd6309f4a0c506e525826"


def call_ipStack(ip_address):
    url = "http://api.ipstack.com/{0}?access_key={1}".format(ip_address, ACCESS_KEY)
    page = urllib.request.urlopen(url)
    page_contents_dict = json.loads(page.read().decode('utf-8'))

    ####################################################
    # We now have a dictionary of all of the attributes
    # returned from the page
    # Example:
    # {'ip': '1.2.3.4', 'type': 'ipv4', 'continent_code': 'OC', 'continent_name': 'Oceania',
    # 'country_code': 'AU', 'country_name': 'Australia', 'region_code': 'QLD',
    # 'region_name': 'Queensland', 'city': 'Brisbane', 'zip': '4000', 'latitude': -27.467580795288086,
    # 'longitude': 153.02789306640625, 'location': {'geoname_id': 2174003, 'capital': 'Canberra',
    # 'languages': [{'code': 'en', 'name': 'English', 'native': 'English'}],
    # 'country_flag': 'https://assets.ipstack.com/flags/au.svg', 'country_flag_emoji': '🇦🇺',
    # 'country_flag_emoji_unicode': 'U+1F1E6 U+1F1FA',   'calling_code': '61', 'is_eu': False}}
    #
    # For now, just extract latitude and longitude
    ####################################################

    ####################################################
    # Catch the case where IP address could not be looked up
    ####################################################
    if 'latitude' not in list(page_contents_dict.keys()) or 'longitude' not in list(page_contents_dict.keys()):
        print("No latitude or longitude info could be obtained")
    else:
        print("Latitude: {0}, Longitude: {1}".format(page_contents_dict['latitude'], page_contents_dict['longitude']))


#### Main body starts here #####
parser = argparse.ArgumentParser()
# Remove the optional --help description in order to get required param section to print first
parser._action_groups.pop()
required = parser.add_argument_group('required arguments')
required.add_argument("-i", "--ip_address", help="Specific IP address to query for", required=True)
optional = parser.add_argument_group('optional arguments')
args = parser.parse_args()

# Verify required parameters specified
if not args.ip_address:
    raise (Exception, "No ip_address specified")
call_ipStack(args.ip_address)
