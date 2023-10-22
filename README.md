# IP Tracking Python Code

This Python code allows you to track and retrieve location information from IP addresses.

## Usage

To use the code, follow these steps:

1. Import the `track` class from the `ip_tracking` module.
2. Set environment variables ipinfo_access_token and mapquest_access_token with your access tokens (ipinfo_access_token is mandatory).
3. Replace `'your_ip_address'` with the IP address you want to track and run the 'track' class.

## Example:
```python
from ip_tracking import track
import os
os.environ['ipinfo_access_token'] = YourToken
os.environ['mapquest_access_token'] = YourToken

track(ip_address = 'your_ip_address')
```

## Prerequisites
* Ipinfo API access token (mandatory)
* MapQuest API access token


## Functionality
The code provides two main functions:

IPTracking(): Retrieves IP address information using the ipinfo library.
get_location_info(): If a MapQuest access token is available, it retrieves location information based on latitude and longitude obtained from IPTracking.

## Output
The code will print the IP address details and, if applicable, the location information. If the MapQuest access token is missing, it will display a message indicating that it can't be used.

For further details and documentation, please refer to the source code.

