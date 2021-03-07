from flask import Flask, render_template, request, jsonify
import regex_check
import SMTP_check
import user_check
import disposable_check
import role_check
import free_mail_check

app = Flask(__name__)  

e_mail=""

@app.route("/")
def status():
	return render_template("status.html")


@app.route("/disposable")
def disposable():
	email=request.args.get("target_email")
	disposable_bool=disposable_check.check_disposable(email)
	if disposable_bool==True:
		color_stat="#ff5722"
		return jsonify(disposable_stat=disposable_bool,color=color_stat)
	elif disposable_bool==False:
		color_stat="#aae237"
		return jsonify(disposable_stat=disposable_bool,color=color_stat)

@app.route("/smtp")
def smtp():
	email=request.args.get("target_email")
	smtp_bool=SMTP_check.check_SMTP(email)
	if smtp_bool==True:
		color_stat="#aae237"
		return jsonify(smtp_status=smtp_bool,color=color_stat)
	elif smtp_bool==False:
		color_stat="#ff5722"
		return jsonify(smtp_status=smtp_bool,color=color_stat)
	elif smtp_bool=="Unknown":
		color_stat="#8080800f"
		return jsonify(smtp_status=smtp_bool,color=color_stat)

@app.route("/existance")
def existance():
	email=request.args.get("target_email")
	existance_bool=user_check.check_mail_existance(email)
	if existance_bool==True:
		color_stat="#aae237"
		return jsonify(user_stat=existance_bool,color=color_stat)
	elif existance_bool==False:
		color_stat="#ff5722"
		return jsonify(user_stat=existance_bool,color=color_stat)	
	else:
		color_stat="#8080800f"
		return jsonify(user_stat=existance_bool,color=color_stat)

@app.route("/acceptall")
def acceptall():
	email=request.args.get("target_email")
	acceptall_bool=user_check.accept_all_check(email)
	if acceptall_bool==True:
		color_stat="#ffeb3b"
		return jsonify(acceptall_stat=acceptall_bool,color=color_stat)
	elif acceptall_bool==False:
		color_stat="#aae237"
		return jsonify(acceptall_stat=acceptall_bool,color=color_stat)	
	elif acceptall_bool=="Unknown":
		color_stat="#8080800f"
		return jsonify(acceptall_stat=acceptall_bool,color=color_stat)



@app.route("/syntax")
def regex():
	email=request.args.get("target_email")
	syntax_bool=regex_check.check_regex(email)
	print(syntax_bool)
	if syntax_bool==True:
		color_stat="#aae237"
		return jsonify(syntax_stat=syntax_bool,color=color_stat)
	elif syntax_bool==False:
		color_stat="#ff5722"
		return jsonify(syntax_stat=syntax_bool,color=color_stat)



@app.route("/role")
def role():
	email=request.args.get("target_email")
	role_bool=role_check.check_role(email)
	if role_bool==True:
		color_stat="#ffeb3b"
		return jsonify(role_stat=role_bool,color=color_stat)
	elif role_bool==False:
		color_stat="#aae237"
		return jsonify(role_stat=role_bool,color=color_stat)

@app.route("/free")
def free():
	email=request.args.get("target_email")
	freemail_bool=free_mail_check.check_free_mail(email)
	if freemail_bool==True:
		color_stat="#ffeb3b"
		return jsonify(free_stat=freemail_bool,color=color_stat)
	elif freemail_bool==False:
		color_stat="aae237"
		return jsonify(free_stat=freemail_bool,color=color_stat)

#&emsp and &nbsp and &ensp




if __name__ == '__main__':  
   app.run(debug = True) 