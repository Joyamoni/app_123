def check_role(email):
	import data_list
	global role_bool
	user=email.replace("@"," ").split()[0]
	if user in data_list.role_list:
		role_bool=True
	elif user not in data_list.role_list:
		role_bool=False
	return(role_bool)

