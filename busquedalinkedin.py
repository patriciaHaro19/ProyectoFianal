# Script para buscar información de un empleado en Linkedin usando google

import const
from apiclient.discovery import build
import pprint

# your google hacking query
query=''
query_params=''

doquery=query+query_params

service = build("customsearch","v1",developerKey=const.cse_token)

res = service.cse().list(
	q=doquery,
	cx=const.cse_id,
	num=10).execute()

pprint.pprint(res)

# VULNEX EOF
