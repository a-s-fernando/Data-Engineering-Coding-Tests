import csv
import requests

# A team of analysts wish to discover how far people are travelling to their nearest
# desired court. We have provided you with a small test dataset so you can find out if
# it is possible to give the analysts the data they need to do this. The data is in
# `people.csv` and contains the following columns:
# - person_name
# - home_postcode
# - looking_for_court_type

# The courts and tribunals finder API returns a list of the 10 nearest courts to a
# given postcode. The output is an array of objects in JSON format. The API is
# accessed by including the postcode of interest in a URL. For example, accessing
# https://courttribunalfinder.service.gov.uk/search/results.json?postcode=E144PU gives
# the 10 nearest courts to the postcode E14 4PU. Visit the link to see an example of
# the output.

# Below is the first element of the JSON array from the above API call. We only want the
# following keys from the json:
# - name
# - dx_number
# - distance
# dx_number is not always returned and the "types" field can be empty.

"""
[
    {
        "name": "Central London Employment Tribunal",
        "lat": 51.5158158439741,
        "lon": -0.118745425821452,
        "number": null,
        "cci_code": null,
        "magistrate_code": null,
        "slug": "central-london-employment-tribunal",
        "types": [
            "Tribunal"
        ],
        "address": {
            "address_lines": [
                "Victory House",
                "30-34 Kingsway"
            ],
            "postcode": "WC2B 6EX",
            "town": "London",
            "type": "Visiting"
        },
        "areas_of_law": [
            {
                "name": "Employment",
                "external_link": "https%3A//www.gov.uk/courts-tribunals/employment-tribunal",
                "display_url": "<bound method AreaOfLaw.display_url of <AreaOfLaw: Employment>>",
                "external_link_desc": "Information about the Employment Tribunal"
            }
        ],
        "displayed": true,
        "hide_aols": false,
        "dx_number": "141420 Bloomsbury 7",
        "distance": 1.29
    },
    etc
]
"""

# Use this API and the data in people.csv to determine how far each person's nearest
# desired court is. Generate an output (of whatever format you feel is appropriate)
# showing, for each person:
# - name
# - type of court desired
# - home postcode
# - nearest court of the right type
# - the dx_number (if available) of the nearest court of the right type
# - the distance to the nearest court of the right type


def get_data(filename: str) -> dict:
    """Turn a csv file into a dict."""
    data = []
    with open(filename, mode='r', encoding='UTF-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    return data


def generate_combined_data(data_in: list):
    """"""
    data_out = data_in
    for index, query in enumerate(data_out):
        r = requests.get(
            f"https://courttribunalfinder.service.gov.uk/search/results.json?postcode={query['home_postcode']}")
        courts = r.json()
        for court in courts:
            if query['looking_for_court_type'] in court['types']:
                data_out[index]['nearest_court_name'] = court['name']
                data_out[index]['nearest_court_distance'] = court['distance']
                if 'dx_number' in court and court['dx_number'] is not None:
                    data_out[index]['nearest_court_dx_number'] = court['dx_number']
                break
    return data_out


if __name__ == "__main__":
    data = get_data('people.csv')
    combined_data = generate_combined_data(data)
    for row in combined_data:
        print(row)


def test_get_data():
    assert get_data('people.csv')[0] == {'person_name': 'Iriquois Pliskin',
                                         'home_postcode': 'SE17TP',
                                         'looking_for_court_type': 'Crown Court'}
    assert get_data('people.csv')[9] == {'person_name': 'Guido Van Rossum',
                                         'home_postcode': 'NR162HE',
                                         'looking_for_court_type': 'County Court'}


def test_generate_combined_data():
    # Valid as of 6th April 2023 (new courts may be added in future)
    val = generate_combined_data([{'person_name': 'test',
                                   'home_postcode': 'LS63AB',
                                   'looking_for_court_type': 'County Court'}])[0]
    assert val == {'person_name': 'test',
                   'home_postcode': 'LS63AB',
                   'looking_for_court_type': 'County Court',
                   'nearest_court_name': 'Leeds Combined Court Centre',
                   'nearest_court_distance': 1.76,
                   'nearest_court_dx_number': '703016 Leeds 6'}
