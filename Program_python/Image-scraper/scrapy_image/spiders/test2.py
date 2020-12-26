from url_parser import parse_url, get_url, get_base_url


url = parse_url(
    "https://open.prospecta.app/my_user_login?user=url-parser&password=H3ll0"
)  # returns url sections as a dict
url_object = get_url(
    "https://open.prospecta.app/my_user_login?user=url-parser&password=H3ll0"
)  # Does the same, bur returns a object
basic_url = get_base_url(
    "https://open.prospecta.app/my_user_login?user=url-parser&password=H3ll0"
)  # Returns just the main url

print(url["domain"])  # Outputs -> prospecta
print(url_object.domain)  # Outputs -> prospecta
print(basic_url)  # Outputs -> https://open.prospecta.app
