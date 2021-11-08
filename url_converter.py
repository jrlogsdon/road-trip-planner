
def string_to_url_format(s):
    s = s.replace(" ", "%20")
    s = s.replace("\"", "%22")
    return s