#!/bin/bash
# sends request to URL passed as argument, displays status code
curl -so /dev/null -w "%{http_code}" "$1"
https://github.com/tlvb25/holbertonschool-higher_level_programming.git