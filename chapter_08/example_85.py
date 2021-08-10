#8.13
def build_profile(fname,lname, **userinfo):
    profile = {}
    profile['fname'] = fname
    profile['lanme'] = lname
    for key,value in userinfo.items():
        profile[key] =value
    return profile

my_profile = build_profile('naeemur','rahman',
                           location = 'kishoregonj',
                           field = 'maths')
print(my_profile)
