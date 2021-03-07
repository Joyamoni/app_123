def check_free_mail(email):
	import data_list
	global free_mail_bool

	domain=email.replace("@"," ").split()[-1]

	if domain in data_list.free_mail_list:
		free_mail_bool=True
	elif domain not in data_list.free_mail_list:
		free_mail_bool=False
	return(free_mail_bool)
