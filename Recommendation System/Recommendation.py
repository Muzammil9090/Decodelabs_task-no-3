# SIMPLE RECOMMENDATION SYSTEM

# 1. Welcome Message
print("SIMPLE RECOMMENDATION SYSTEM")

# 2. Recommendation Data
recommendations = {
    "action": [
        "Avengers",
        "John Wick",
        "Mad Max"
    ],

    "comedy": [
        "The Mask",
        "Friends",
        "Brooklyn Nine-Nine"
    ],

    "romance": [
        "Titanic",
        "The Notebook",
        "La La Land"
    ],

    "technology": [
        "The Social Network",
        "Steve Jobs",
        "Silicon Valley"
    ],

    "sports": [
        "Rocky",
        "Creed",
        "Rush"
    ]
}

print("\nAvailable Interests:")

# 3. Display Available Interests
for interest in recommendations:
    print("-", interest)


# 4. Take User Input
user_interest = input("\nEnter your interest: ").lower().strip()


# 5. Match User Preference
if user_interest in recommendations:

# 6. Display Recommendations
    print("\nRecommended items for you:")

    for item in recommendations[user_interest]:
        print(item)

else:

# 7. If Interest Does Not Exist
    print("\nSorry! No recommendations found.")
    print("Please choose an interest from the list.")

# 8. End Message
print("Thank you for using the system!")
