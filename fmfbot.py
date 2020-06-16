import praw
import pprint

CLIENT_ID = "m3zlWjWQ9Ahw-w"
CLIENT_SECRET = "_j-spOhcwzl-uTPGy_nPdg_eP40"
# USERNAME = input("Username: ")
PASSWORD = input("Password: ")
USERNAME = "SJayYang"
USER_AGENT = "macos:fmfbot:v0.1.0 (by /u/SJayYang)"


reddit = praw.Reddit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, user_agent = USER_AGENT, username=USERNAME, password=PASSWORD)

fmf = reddit.subreddit("frugalmalefashion")
jcrew_query = "j.crew OR jcrew OR Jcrew OR J.crew"
bono_query = "Bonobos OR bonobos"



def print_links(subreddit, query):
    """
    Subreddit: subreddit instance
    query: expicit query defined
    """
    print("Subreddit: " + str(subreddit))
    for result in subreddit.search(query, sort="new"):
        print("reddit.com/r/" + str(subreddit) + "/comments/" + str(result) + "      " + result.title)

print_links(fmf, jcrew_query)

print("\n")

print_links(fmf, bono_query)
