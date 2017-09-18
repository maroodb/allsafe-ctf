

def generate_email(name, username):
    greetings = "<h2>Hello " + name + " !</h2><br>"
    body = "<p>Your account has been successfully activated.</p>"
    link = "<p>You are able to login to members dashboard <a href ='https://www.allsafeclub.info/accounts/login'>here</a></p>"
    auth = "<p> username : <strong>" + username + "</strong>"
    regards = "<p>AllSafe Team</p> <br><p>Regards,</p>"
    email_body = greetings + body + link + auth + regards
    return email_body
