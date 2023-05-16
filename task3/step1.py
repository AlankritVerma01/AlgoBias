import json
from datetime import datetime
def calculate_network_overlap(influencer1_id, influencer2_id):
    # Load the "following.json" dataset
    with open('following.json', 'r') as file:
        data = json.load(file)
    
    # Find followers of influencer 1
    influencer1_followers = set()
    for entry in data:
        if entry['influencer_uid'] == influencer1_id:
            #Todo - need to add the feature to check the with the restrains of the date
            influencer1_followers.add(entry['follower_uid'])
    
    # Find followers of influencer 2
    influencer2_followers = set()
    for entry in data:
        if entry['influencer_uid'] == influencer2_id:
            influencer2_followers.add(entry['follower_uid'])
    
    # Calculate network overlap
    total_followers = min(len(influencer1_followers), len(influencer2_followers))
    overlap_followers = len(influencer1_followers.intersection(influencer2_followers))
    
    if total_followers > 0:
        network_overlap = overlap_followers / total_followers
    else:
        network_overlap = 0.0
    
    return network_overlap