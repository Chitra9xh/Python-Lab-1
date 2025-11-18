def create_blog_post(title,*tags,**metadata):
    print("Title:",title)
    print("Tags:",", ".join(tags))
    for k,v in metadata.items(): print(k,":",v)

create_blog_post("Python Functions Explained","python","tutorial","cse",author="Dr. Mishra",date="2025-10-29",category="Programming")
