import sys
import json
from awsip import find_ip, download_aws_ip_set


ip_to_check = sys.argv[1]
result = find_ip(download_aws_ip_set(), ip_to_check)

sys.stdout.write(json.dumps(result, indent=2))
