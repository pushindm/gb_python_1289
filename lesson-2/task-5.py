# simple rating
def simple_rating(user_val, rating_vals):
    user_val = int(user_val)
    print(f"Old ratings: {rating_vals}")
    rating_vals.reverse()
    not_inserted = True
    insertion_pos = 0                  # used for printing the position of user_val in list
    for pos, val in enumerate(rating_vals):
        if user_val <= val:
            rating_vals.insert(pos, user_val)
            insertion_pos = (len(rating_vals) - 1) - pos
            not_inserted = False
            break
    if not_inserted:                   # used only when user_val is more than all values in rating_vals
        rating_vals.append(user_val)
        insertion_pos = 0
    rating_vals.reverse()
    print(f"New ratings: {rating_vals}. New value {user_val} is on {insertion_pos} position.")

# main
current_ratings = [7, 5, 3, 3, 2]
user_rating = input("Enter rating: ")
simple_rating(user_rating, current_ratings)
