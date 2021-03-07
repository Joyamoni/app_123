
def check_regex(e_mail):
	import re

	global regex_status
	found = re.findall("^[A-Za-z0-9]+[\._-]*[A-Za-z0-9]*[@]+[A-Za-z0-9]+[.]+[A-Za-z]", e_mail)

	if found==[]:
		regex_status=False
	elif found!=[]:
		regex_status=True
	return regex_status




