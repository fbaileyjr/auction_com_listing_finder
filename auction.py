import requests
import json

url = "https://graph.auction.com/graphql"

payload = json.dumps({
  "query": "\n        query resiSearch_blueprint_seekListingsFromFilters(\n          $filters: ListingCompatabilityFilters!,\n          $aggregationFields: [String!]!,\n          $hasAuthenticatedUser: Boolean!,\n          $requiresAggregation: Boolean!\n        ) {\n          seek_listings_from_filters(filters: $filters) {\n            total_count\n            total_pages\n            size\n            current_page\n            aggregation(fields: $aggregationFields) @include(if: $requiresAggregation)\n            content {\n                ...ListingCardFields\n                ...ListingPopupCardFields\n            }\n          }\n        }\n        \n  fragment ListingCardFields on Listing {\n    listing_id\n    urn\n    listing_status_group\n    listing_status\n    listing_status_label(intent: SEARCH)\n    primary_photo\n    primary_property_id\n    listing_photos_count\n    listing_page_path\n    reserve_price\n    is_hot\n    formatted_address(format: DOUBLE_LINE)\n    listing_configuration {\n      product_type\n      is_reserve_displayed\n      broker_commission\n      financing_available\n      buyer_premium_available\n      interior_access_allowed\n      occupancy_status\n      asset_type\n      is_first_look_enabled\n      is_direct_offer_enabled\n      is_third_party_online\n    }\n    attribution_source {\n      origin_code\n    }\n    external_identifiers {\n      data_source\n      external_identifier\n    }\n    venue {\n      venue_type\n    }\n    event {\n      event_code\n      trustee_sale\n    }\n    valuation {\n      seller_current_value_amount\n    }\n    strategy {\n      selling_method_attributes {\n        online_segment_type\n      }\n    }\n    seller_property {\n      street_description\n      municipality\n      country_primary_subdivision\n      country_secondary_subdivision\n      postal_code\n    }\n    program_configuration {\n      program_enrollment_code\n    }\n    primary_property {\n      property_id\n      summary {\n        total_bedrooms\n        total_bathrooms\n        square_footage\n        lot_size\n        year_built\n        valuation\n        structure_type_code\n        structure_type_group\n        address {\n          coordinates {\n            lon\n            lat\n          }\n        }\n      }\n      is_currently_saved @include(if: $hasAuthenticatedUser)\n      is_newly_listed\n      current_user_tracking_state {\n        is_seen\n        is_updated\n      }\n    }\n    auction {\n      start_date\n      end_date\n      starting_bid\n      is_online\n      visible_auction_start_date_time\n      bid_instruction {\n        nos_amount\n      }\n    }\n    parties {\n      party_role\n      party_name\n    }\n    marketing_tags {\n      tag\n    }\n    online_auction_segment(resolvePolicy: CACHE_ONLY) {\n      __typename\n      segment_type\n      reserve_status\n      current_highest_bid {\n        bid_amount\n      }\n    }\n    open_houses {\n      local_date\n      start_time\n      end_time\n    }\n    live_auction_segment(resolvePolicy: CACHE_ONLY) {\n      current_highest_bid {\n        bid_amount\n      }\n      configuration {\n        state_deposit_rule\n      }\n    }\n    listing_summary {\n      is_remote_bid_enabled\n      is_remote_before_and_during_auction_enabled\n      show_opening_bid\n    }\n    external_information(resolvePolicy: CACHE_ONLY) {\n      collateral {\n        summary {\n          estimated\n          low\n          high\n          type\n        }\n      }\n    }\n  }\n  fragment ListingPopupCardFields on Listing {\n    listing_id\n    formatted_address_line_1: formatted_address(format: SINGLE_LINE)\n    listing_summary {\n      is_remote_bid_enabled\n      is_remote_before_and_during_auction_enabled\n      show_opening_bid\n    }\n    listing_status_group\n    listing_page_path\n    primary_photo\n    reserve_price\n\n    listing_configuration {\n      product_type\n      asset_type\n      is_third_party_online\n    }\n\n    event {\n      event_code\n    }\n\n    seller_property {\n      street_description\n      country_secondary_subdivision\n      municipality\n      postal_code\n    }\n\n    program_configuration {\n      program_enrollment_code\n    }\n\n    primary_property {\n      property_id\n      summary {\n        total_bedrooms\n        total_bathrooms\n        square_footage\n        address {\n          coordinates {\n            lat\n            lon\n          }\n        }\n      }\n      is_newly_listed\n      current_user_tracking_state {\n        is_seen\n        is_updated\n      }\n    }\n\n    auction {\n      starting_bid\n      is_online\n      bid_instruction {\n        nos_amount\n      }\n    }\n\n    online_auction_segment(resolvePolicy: CACHE_ONLY) {\n      listing_id\n      __typename\n      start_date\n      segment_type\n      initial_end_date\n      current_time\n      reserve_status\n      configuration {\n        is_match_bidding_enabled\n        is_registration_deposit_required_enabled\n        bid_again_count\n        should_bid_again\n      }\n      starting_bid_amount\n      subject_to_status\n      current_highest_bid {\n        bid_amount\n        type\n      }\n      segment_status\n      current_reserve_amount\n      current_increment_amount\n      bid_count\n      result {\n        winning_bid_amount\n      }\n    }\n\n    live_auction_segment(resolvePolicy: CACHE_ONLY) {\n      current_highest_bid {\n        bid_amount\n      }\n    }\n  }\n\n      ",
  "variables": {
    "filters": {
      "geo_location_box": "34.36603326668873,-84.1790361945071,35.1175852129408,-82.84282403630398",
      "listing_type": "active",
      "sort": "auction_date_order,resi_sort_v2",
      "limit": 500,
      "usecode_product_type": "resi_ft",
      "version": 1,
      "offset": 0
    },
    "hasAuthenticatedUser": False,
    "aggregationFields": [],
    "requiresAggregation": False
  }
})
headers = {
  'Content-Type': 'application/json',
  #'Cookie': 'incap_ses_438_2075278=e4rqT8zZ9Qc77bG9ARcUBoeqJGgAAAAA62wDX+WPKtvtSIO9Hihe/Q==; nlbi_2075278=I74uX2j/+VcC+l7WeaK5wwAAAACaTcVXCdjfBLgYqnihjgDa; visid_incap_2075278=RN+pwK58S129DkXW4/USaQonImgAAAAAQUIPAAAAAADeD3vpbGtk79Unw50FWHU8; ADC_APP_UNMATCHED=%7B%22origin_app%22%3A%22resi-auction-graph-api%22%2C%22origin_route%22%3A%22%2Fgraphql%22%7D'
}

def get_response_and_parse():
  response = requests.request("POST", url, headers=headers, data=payload)
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

def parse_for_listings(content: list):
  if not isinstance(content, list):
    raise Exception('Content is not a list')
  for listing in content:
    listing_id = listing.get('listing_id')or ''
    auction_start_date = listing.get('start_date') or ''
    address = '; '.join(listing.get('formatted_address')) or ''
    is_hot = listing.get('is_hot') or 'No'
    listing_page_path = listing.get('listing_page_path')
    parties = '; '.join([x.get('party_name') for x in listing.get('parties')]) or ''
    primary_property = listing.get('primary_property') or {}
    summary = primary_property.get('summary') or {}
    lot_size = str(summary.get('lot_size')) or ''
    square_footage = summary.get('lot_size') or ''
    structure_type = summary.get('structure_type_group') or ''
    total_bedrooms = summary.get('total_bedrooms') or ''
    total_bathrooms = summary.get('total_bathrooms') or ''
    year_built = summary.get('year_built') or ''

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
    parse_for_listings(content)
except Exception as wtf:
  print('Yo, something did NOT work right')

