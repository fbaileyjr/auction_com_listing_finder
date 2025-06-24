import requests
import json

from consts import AUCTION_URL, NORTHEAST_GA_REGION, LARGER_SE_REGION, LARGEST_SE_REGION


number = 0
is_lots = False

while True:
    try:
        print('Select Region: ')
        print('1. Northeast GA')
        print('2. Southeast USA\n')
        print('3. Largest Southeast USA\n')
        user_input = input("Selection: ")
        number = int(user_input)
        # If the input is successfully converted to an integer, break the loop
        if number in [1,2,3]:
          break
    except ValueError:
        print("Invalid input. Please enter value 1, 2, or 3.")

if number == 1:
  payload = NORTHEAST_GA_REGION
elif number == 2:
  payload = LARGER_SE_REGION
elif number == 3:
  payload = LARGEST_SE_REGION
else:
  raise

while True:
    try:
        print('Would you like to display only assets with lots bigger than 10? y/n:\n ')
        user_input = input("Selection: ")
        lots_answer = user_input
        # If the input is successfully converted to an integer, break the loop
        if lots_answer == 'y' or lots_answer == 'n':
          break
    except ValueError:
        print("Invalid input. Please enter value y or n.")

if number == 1:
  payload = NORTHEAST_GA_REGION
elif number == 2:
  payload = LARGER_SE_REGION
elif number == 3:
  payload = LARGEST_SE_REGION
else:
  raise

is_lots = True if lots_answer == 'y' else False

headers = {
  'Content-Type': 'application/json',
  #'Cookie': 'incap_ses_438_2075278=e4rqT8zZ9Qc77bG9ARcUBoeqJGgAAAAA62wDX+WPKtvtSIO9Hihe/Q==; nlbi_2075278=I74uX2j/+VcC+l7WeaK5wwAAAACaTcVXCdjfBLgYqnihjgDa; visid_incap_2075278=RN+pwK58S129DkXW4/USaQonImgAAAAAQUIPAAAAAADeD3vpbGtk79Unw50FWHU8; ADC_APP_UNMATCHED=%7B%22origin_app%22%3A%22resi-auction-graph-api%22%2C%22origin_route%22%3A%22%2Fgraphql%22%7D'
}

def get_response_and_parse():
  response = requests.request("POST", AUCTION_URL, headers=headers, data=payload)
  message = 'Unable to parse response'
  try:
    response_dict = json.loads(response.text)
    if not isinstance(response_dict, dict):
      raise Exception(message)
    data = response_dict.get('data')
    if not isinstance(data, dict):
      raise Exception(message)
    seek_listings_from_filters = data.get('seek_listings_from_filters')  
    if not isinstance(seek_listings_from_filters, dict):
      raise Exception(message)
    content = seek_listings_from_filters.get('content')
    if not isinstance(content, list):
      raise Exception(message)
    # print(content)
    return(content)
  except Exception as err:
    print(f'Got a problem: {err}')

def parse_for_listings(content: list, is_lots: bool):
  if not isinstance(content, list):
    raise Exception('Content is not a list')
  for listing in content:
    if is_lots:
      primary_property = listing.get('primary_property') or {}
      summary = primary_property.get('summary') or {}
      if summary.get('lot_size') and summary.get('lot_size') >= 10:
        listing_id = listing.get('listing_id') or ''
        auction_start_date = listing.get('start_date') or ''
        address = '; '.join(listing.get('formatted_address')) or ''
        is_hot = listing.get('is_hot') or 'No'
        listing_page_path = listing.get('listing_page_path')
        parties = '; '.join([x.get('party_name') for x in listing.get('parties') if x.get('party_name') != None]) or ''
        lot_size = str(summary.get('lot_size')) or ''
        square_footage = summary.get('lot_size') or ''
        structure_type = summary.get('structure_type_group') or ''
        total_bedrooms = summary.get('total_bedrooms') or ''
        total_bathrooms = summary.get('total_bathrooms') or ''
        year_built = summary.get('year_built') or ''
      else:
        continue
    elif not is_lots:
      try:
        listing_id = listing.get('listing_id') or ''
        auction_start_date = listing.get('start_date') or ''
        address = '; '.join(listing.get('formatted_address')) or ''
        is_hot = listing.get('is_hot') or 'No'
        listing_page_path = listing.get('listing_page_path')
        parties = '; '.join([x.get('party_name') for x in listing.get('parties') if x.get('party_name') != None]) or ''
        primary_property = listing.get('primary_property') or {}
        summary = primary_property.get('summary') or {}
        lot_size = str(summary.get('lot_size')) or ''
        square_footage = summary.get('lot_size') or ''
        structure_type = summary.get('structure_type_group') or ''
        total_bedrooms = summary.get('total_bedrooms') or ''
        total_bathrooms = summary.get('total_bathrooms') or ''
        year_built = summary.get('year_built') or ''
      except Exception as reg_err:
        print(f'Problem with fetch: {reg_err}')


    print(f'''Listing: {listing_id}
Auction Start Date: {auction_start_date}
Address: {address}
Is Hot: {is_hot}
URL: https://www.auction.com{listing_page_path}
Parties: {parties}
Lot Size: {lot_size}
Structure Type: {structure_type}
Square Footage: {square_footage}
Total Bedrooms: {total_bedrooms}
Total Bathrooms: {total_bathrooms}
Year Built: {year_built}
\n\n\n
''')

try:
  content = get_response_and_parse()
  if isinstance(content, list):
    parse_for_listings(content, is_lots)
except Exception as wtf:
  print(f'Yo, something did NOT work right: {wtf}')

