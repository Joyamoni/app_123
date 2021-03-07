

def check_SMTP(email):
	import dns.resolver

	global mail_server_status
	global server_list
	
	domain=email.replace("@"," ").split()[-1]

	server_list=[]
	try:
		stat=dns.resolver.resolve(domain,"MX")	

		for i in stat:
			server_list.append(str(i))

		if server_list==[]:
			mail_server_status=False
		elif server_list!=[]:
			mail_server_status=True

		return(mail_server_status)
		
	except:
		return("Unknown")
