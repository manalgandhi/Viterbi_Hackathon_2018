

def get_device_type(count_unique_domains):
    if(count_unique_domains <= 3):
        return "home_appliances"
    elif count_unique_domains <= 15:
        return "entertainment"
    else:
        return "general_purpose"