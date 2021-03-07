import regex_check
import SMTP_check
import user_check
import disposable_check
import role_check
import free_mail_check


def run(email):
	internet_error="unknown [due to slow internet connection]"
	try:
		regex_bool=regex_check.check_regex(email)
		print(f"email format is = {regex_bool}")
	except:
		print(f"email format is = {internet_error}")

	try :
		SMTP_bool=SMTP_check.check_SMTP(email)
		print(f"SMTP existance is = {SMTP_bool}")
	except:
		print(f"SMTP existance is = {internet_error}")

	try:
		role_bool=role_check.check_role(email)
		print(f"role email is = {role_bool}")
	except:
		print(f"role email is = {internet_error}")

	try:
		mail_existance_bool=user_check.check_mail_existance(email)
		print(f"user existance is = {mail_existance_bool}")
	except:
		print(f"user existance is = {internet_error}")

	try:
		disposable_bool=disposable_check.check_disposable(email)
		print(f"chance of disposability is = {disposable_bool}")
	except:
		print(f"chance of disposability is = {internet_error}")

	try: 
		accept_all_bool=user_check.accept_all_check(email)
		print(f"accept all mail is = {accept_all_bool}")
	except:
		print(f"accept all mail is = {internet_error}")

	try:
		free_mail_bool=free_mail_check.check_free_mail(email)
		print(f"chance of free mail is = {free_mail_bool}")
	except:
		print(f"chance of free mail is = {internet_error}")




run("brian.karoly@schroders.com")