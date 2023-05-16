import json
from datetime import datetime

def calculate_engagement_overlap(influencer1_id, influencer2_id):
    # Load the "engagement.json" dataset
    with open('engagement.json', 'r') as file:
        data = json.load(file)
    
    # Convert date strings to datetime objects for comparison
    start_date = datetime.strptime("2022-04-22", "%Y-%m-%d")
    end_date = datetime.strptime("2022-04-30", "%Y-%m-%d")
    
    # Find engagers of influencer 1
    influencer1_engagers = set()
    for entry in data:
        engaged_dt = datetime.strptime(entry['engaged_dt'], "%Y-%m-%d")
        if (entry['influencer_uid'] == influencer1_id) and (start_date <= engaged_dt <= end_date):
            influencer1_engagers.add(entry['follower_uid'])
    
    # Find engagers of influencer 2
    influencer2_engagers = set()
    for entry in data:
        engaged_dt = datetime.strptime(entry['engaged_dt'], "%Y-%m-%d")
        if (entry['influencer_uid'] == influencer2_id) and (start_date <= engaged_dt <= end_date):
            influencer2_engagers.add(entry['follower_uid'])
    
    # Calculate engagement overlap
    total_engagers = min(len(influencer1_engagers), len(influencer2_engagers))
    overlap_engagers = len(influencer1_engagers.intersection(influencer2_engagers))
    
    if total_engagers > 0:
        engagement_overlap = overlap_engagers / total_engagers
    else:
        engagement_overlap = 0.0
    
    return engagement_overlap
