# ipStackInquiry
This is a simple Python script to call IpStack.com API and extract the latt/long of the specified IP address. Script is aimed for simplicity, and easy expandability if additional fields needed to be extracted.

Some sample use cases:

 % python3 ipStackInquiry.py -h
usage: ipStackInquiry.py [-h] -i IP_ADDRESS

required arguments:
  -i IP_ADDRESS, --ip_address IP_ADDRESS
                        Specific IP address to query for

% python3 ipStackInquiry.py -i 128.4567.78

No latitude or longitude info could be obtained

 % python3 ipStackInquiry.py -i 128.56.78.89

Latitude: 36.92033004760742, Longitude: -76.01876831054688
