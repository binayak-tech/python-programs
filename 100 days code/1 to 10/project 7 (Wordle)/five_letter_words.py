five_letter_words = [
'Abuse', 'Adult', 'Agent', 'Anger', 'Apple', 'Award', 
'Basis', 'Beach', 'Birth', 'Block', 'Blood', 'Board', 'Brain', 'Bread', 'Break', 'Brown', 'Buyer', 
'Cause', 'Chain', 'Chair', 'Chest', 'Chief', 'Child', 'China', 'Claim', 'Class', 'Clock', 'Coach', 'Coast', 'Court', 'Cover', 'Cream', 'Crime', 'Cross', 'Crowd', 'Crown', 'Cycle', 
'Dance', 'Death', 'Depth', 'Doubt', 'Draft', 'Drama', 'Dream', 'Dress', 'Drink', 'Drive', 
'Earth', 'Enemy', 'Entry', 'Error', 'Event', 
'Faith', 'Fault', 'Field', 'Fight', 'Final', 'Floor', 'Focus', 'Force', 'Frame', 'Front', 'Fruit', 
'Glass', 'Grant', 'Grass', 'Green', 'Group', 'Guide', 
'Heart', 'Horse', 'Hotel', 'House', 
'Image', 'Index', 'Input', 'Issue', 
'Japan', 'Judge', 
'Knife', 
'Layer', 'Level', 'Light', 'Limit', 'Lunch', 
'Major', 'March', 'Match', 'Metal', 'Model', 'Money', 'Month', 'Motor', 'Mouth', 'Music', 
'Night', 'Noise', 'North', 'Novel', 'Nurse', 
'Offer', 'Order', 'Other', 'Owner', 
'Panel', 'Paper', 'Party', 'Peace', 'Phase', 'Phone', 'Piece', 'Pilot', 'Pitch', 'Place', 'Plane', 'Plant', 'Plate', 'Point', 'Pound', 'Power', 'Press', 'Price', 'Pride', 'Prize', 'Proof', 
'Queen', 
'Radio', 'Range', 'Ratio', 'Reply', 'Right', 'River', 'Round', 'Route', 'Rugby', 
'Scale', 'Scene', 'Scope', 'Score', 'Sense', 'Shape', 'Share', 'Sheep', 'Sheet', 'Shift', 'Shirt', 'Shock', 'Sight', 'Skill', 'Sleep', 'Smile', 'Smoke', 'Sound', 'South', 
'Space', 'Speed', 'Spite', 'Sport', 'Squad', 'Staff', 'Stage', 'Start', 'State', 'Steam', 'Steel', 'Stock', 'Stone', 'Store', 'Study', 'Stuff', 'Style', 'Sugar', 
'Table', 'Taste', 'Theme', 'Thing', 'Title', 'Total', 'Touch', 'Tower', 'Track', 'Trade', 'Train', 'Trend', 'Trial', 'Trust', 'Truth', 
'Uncle', 'Union', 'Unity', 
'Value', 'Video', 'Visit', 'Voice', 
'Waste', 'Watch', 'Water', 'While', 'White', 'Whole', 'Woman', 'World', 
'Youth', 
]

from random import choice,shuffle

shuffle(five_letter_words)

def fiveLetterLword ():
    """This retruns a random word with 5 letters"""
    chosen = choice(five_letter_words).upper()
    return chosen