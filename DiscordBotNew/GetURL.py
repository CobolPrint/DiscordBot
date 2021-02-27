import re

pattern = "http(?:s?):\/\/(?:www\.)?youtu(?:be\.com\/watch\?v=|\.be\/)([\w\-\_]*)(&(amp;)?‌​[\w\?‌​=]*)?"

def checkForYoutube(userLink):
    if(re.search(pattern, userLink)):
        return userLink
    else:
        return 0





