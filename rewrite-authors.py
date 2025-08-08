def replace_author_name_email(commit):
    if commit.author_name == b"DakshSammi":
        commit.author_name = b"shashigupta315"
    if commit.author_email == b"daksh21459@iiitd.ac.in":
        commit.author_email = b"guptashashi0315@gmail.com"
    if commit.committer_name == b"DakshSammi":
        commit.committer_name = b"shashigupta315"
    if commit.committer_email == b"daksh21459@iiitd.ac.in":
        commit.committer_email = b"guptashashi0315@gmail.com"
