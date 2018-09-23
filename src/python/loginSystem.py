import cgi

form = cgi.FieldStorage()
username = form.getvalue('username')
password = form.getvalue('password')


#Test code to check input form
def main()
{
    print("Username: " + username)
    print("Password: " + password)
}