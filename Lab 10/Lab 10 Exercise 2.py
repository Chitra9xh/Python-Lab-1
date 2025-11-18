def activate_user(profile_dict):
    profile_dict["status"]="active"

user_profile={"username":"s_kumar","email":"s_kumar@juet.ac.in"}
activate_user(user_profile)
print("Updated profile:",user_profile)
