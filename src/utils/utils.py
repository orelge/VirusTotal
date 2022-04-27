import base64

def get_url_website_to_url_id(url: str) -> base64:
    url_id = base64.urlsafe_b64encode(url.encode()).decode().strip("=")
    return url_id
