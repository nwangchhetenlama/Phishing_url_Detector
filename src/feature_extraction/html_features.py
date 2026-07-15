import requests
from bs4 import BeautifulSoup

from urllib.parse import urlparse

#function to check whether domain appear in webpage title

def extract_domain_in_title(soup, domain):
    try:
        title = soup.title.text.lower()

        domain_name = (
            urlparse("https://" + domain).hostname
            .replace("www.", "")
            .split(".")[0]
            .lower()
        )

        return int(domain_name in title)

    except Exception as e:
        print(e)
        return 0

# Function to count phishing keywords

def extract_phish_hints(soup):

    phishing_words = [
        "action required",
        "account suspended",
        "security alert",
        "suspicious activity",
        "verify your account",
        "confirm your identity",
        "payment failure",
        "password expired",
        "unauthorized login attempt",
        "claim your reward"
    ]
    text=soup.get_text().lower()

    count=sum(text.count(word) for word in phishing_words)
    return count

# Function to calculate hyperlink features
def extract_hyperlink_features(soup,domain):
    links=soup.find_all("a")

    total_links=len(links)
    if total_links ==0:
        return 0,0,0
    
    internal=0
    external=0
    safe=0
    for link in links:

        href=link.get("href")
        if not href:
            continue

        #safe anchors ->#
        if href.startswith("#"):
            safe+=1
        
        # internal links -> google.com/about

        elif href.startswith("/") or domain in href:
            internal+=1

        #external
        else:
            external+=1
        
    ratio_internal=internal/total_links
    ratio_external = external / total_links

    safe_anchor = (safe / total_links)*100
    return (ratio_external,ratio_internal,safe_anchor)
    

# Function to calculate external redirects

def extract_redirection_ratio(response,domain):

    redirects=response.history

    if len(redirects)==0:
        return 0
    
    external_redirects=0
    for redirect in redirects:
        redirect_domain=(urlparse(redirect.url).netloc)
    
        if redirect_domain.replace("www.", "") != domain.replace("www.", ""):

            external_redirects+=1
    
    return (external_redirects/len(redirects))


# Main HTML feature extraction function
def extract_html_features(url):
    domain=(
        urlparse(url).netloc
    )
    try:
        response=requests.get(
            url,
            timeout=10,
            headers={
                "User-Agent":
                "Mozilla/5.0"

            }
        )

        soup=BeautifulSoup(response.text,"html.parser")

        ratio_extHyperlinks, \
        ratio_intHyperlinks, \
        safe_anchor = \
            extract_hyperlink_features(
                soup,
                domain
            )
        return {
            "phish_hints":
            extract_phish_hints(soup),

            # Percentage of external links
            "ratio_extHyperlinks":
                ratio_extHyperlinks,

            # Percentage of internal links
            "ratio_intHyperlinks":
                ratio_intHyperlinks,

            # Percentage of safe anchors
            "safe_anchor":
                safe_anchor,

            # Percentage of redirects to other domains
            "ratio_extRedirection":
                extract_redirection_ratio(
                    response,
                    domain
                ),

            # Whether domain appears in title
            "domain_in_title":
                extract_domain_in_title(
                    soup,
                    domain
                )


        }

    except Exception as e:

        
        return {
            "phish_hints": 0,
            "ratio_extHyperlinks": 0,
            "ratio_intHyperlinks": 0,
            "safe_anchor": 0,
            "ratio_extRedirection": 0,
            "domain_in_title": 0
        }



