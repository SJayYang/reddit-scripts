import praw


CLIENT_ID = "m3zlWjWQ9Ahw-w"
CLIENT_SECRET = "	_j-spOhcwzl-uTPGy_nPdg_eP40"
USERNAME = input("Username: ")
PASSWORD = input("Password: ")
USER_AGENT = "macos:fmfbot:v0.1.0 (by /u/SJayYang)"


reddit = praw.Reddit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, user_agent = USER_AGENT, username=USERNAME, password=PASSWORD)

print(reddit.read_only())
