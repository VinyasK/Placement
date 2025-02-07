ratings=[5,3,3.5,4,4.5,3,4.5]

unique_ratings=set(ratings) //removes the duplicate values
max_count=0
for rating in unique_ratings:
    count=ratings.count(rating) //counts rating value in ratings list
    if count>max_count: 
        max_count=count //updates max count with count
        frequent=rating
print(frequent)        
