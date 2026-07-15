import whois
from datetime import datetime

def extract_domain_age(domain):

    try:
        domain_info=whois.whois(domain)

        creation_date=domain_info.creation_date

        if isinstance(creation_date,list):
            creation_date=creation_date[0]
    
        if creation_date is None:
            return 0

        today=datetime.now(creation_date.tzinfo)

        age_days=(today-creation_date).days
        return age_days

    except Exception:
        
        return 0
