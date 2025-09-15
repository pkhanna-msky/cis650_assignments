POSTS = [
	"Big sale today!!! #Deals #Sale #sale #Coupons Visit our site.",
    "New arrivals: eco-friendly mugs & bottles. #Sustainability #Eco #Mugs",
    "Coffee lovers unite ☕ #Coffee #Beans #mugs #Deals",
    "Back-to-school bundles: notebooks, pens, backpacks. #BTS #School #Deals",
    "We love local roasters — fresh beans weekly! #coffee #Local #Fresh",
    "Zero-waste gifts 🎁 #Sustainability #Eco #Gifts #Deals",
    "MUGS MUGS MUGS 😍 #Mugs #Sale #Merch",
    # ✅ Added new post
    "New fall flavors are here! #Pumpkin #Coffee #Seasonal #Deals"
]	
    
import re
from collections import Counter
from typing import List, Set

def clean_post(post: str) -> str:
    """Lowercase, replace punctuation with spaces, and collaspe multiple whitespace to one space."""
    post = post.lower()
    post = re.sub(r"[.,!?:;—–-]", " ", post)
    post = re.sub(r"\s+", " ", post)
    return post.strip()

cleaned_posts = [clean_post(post) for post in POSTS]

def extract_hashtags(post: str) -> Set[str]:
    """Return a set of tokens starting with # from a cleand string."""
    return {word for word in post.split() if word.startswith("#")}


def tag_post(cleaned_post: str) -> str:
    tags = extract_hashtags(cleaned_post)
    if {"#eco", "#sustainability"} & tags:
        return "sustainability"
    if {"#coffee", "#beans", "#mugs"} & tags:
        return "coffee"
    if "#deals" in tags or "#sale" in tags:
        return "promotions"
    return "other"

post_topics: List[str] = [tag_post(post) for post in cleaned_posts]


all_tags: Set[str] = set()
for post in cleaned_posts:
	all_tags |= extract_hashtags(post)
     
print("All unique hashtags (unions):")
print(all_tags)


tag_counts = Counter()
for post in cleaned_posts:
	tag_counts.update(extract_hashtags(post))
     
top_3 = sorted(tag_counts.items(), key=lambda kv: (-kv[1], kv[0]))[:3]

print("\nTop 3 hashtags by frequency (by count):")
for tag, count in top_3:
	print(f"{tag}: {count}")
     

