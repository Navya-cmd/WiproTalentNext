import sys

like_str = sys.argv[1]
dislike_str = sys.argv[2]
given_str = sys.argv[3] 

likes = like_str.split('-') 
dislikes = dislike_str.split('-')
given_numbers = given_str.split('-')

happiness = 0

for num in given_numbers:
    if num in likes:
        happiness += 1
    elif num in dislikes:
        happiness -= 1

print(happiness)
