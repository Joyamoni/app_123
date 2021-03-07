def check_disposable(email):
	import data_list
	global disposable_bool

	domain=email.replace("@"," ").split()[-1]
	if domain in data_list.disposable_domain_list:
		disposable_bool=True
	elif domain not in data_list.disposable_domain_list:
		disposable_bool=False
	return(disposable_bool)
