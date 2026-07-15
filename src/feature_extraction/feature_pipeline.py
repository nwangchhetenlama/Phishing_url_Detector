from .url_features import extract_url_features
from .html_features import extract_html_features
from .whois_features import extract_domain_age

from urllib.parse import urlparse

def extract_features(url):

    url_features=extract_url_features(url)

    html_features=extract_html_features(url)

    domain=urlparse(url).netloc.replace("www.","")

    whois_features={
        "domain_age":extract_domain_age(domain)
    }

    features={
        **url_features,
        **html_features,
        **whois_features
    }
    return features

