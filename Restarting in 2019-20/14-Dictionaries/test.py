artist = {
    "first": "Neil",
    "last": "Young",
}

#full_name = artist["first"] + " " + artist["last"]
#full_name = "{} {}".format(artist["first"],artist["last"])
full_name = f"{artist['first']} {artist['last']}"

print(full_name)