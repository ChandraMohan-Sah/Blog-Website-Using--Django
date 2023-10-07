from django.shortcuts import render
from datetime import date

all_posts = [
    {
        "slug":"hike-in-the-mountains",
        "image": "avatar-5.jpg",
        "author" :"Lina",
        "date": date(2021, 7,21),
        "address": "15 Adr street, 5015, NY",
        "title": "Mountain Hiking",
        "excerpt" : "Lorem ipsum dolor sit amet consectetur adipisicing elit. Est pariatur nemo tempore repellat? Ullam sed officia iure architecto deserunt distinctio, pariatur",
        "content" : """
            Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
            Lorem Ipsum has been the industry's standard dummy text eversince the 1500s,
            when an unknown printer took a galley of type and scrambled it to make a type 
            specimen book. 
            
            It has survived not only five centuries, but also the leap into
            electronic typesetting, remaining essentially unchanged. It was popularised in 
            the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, 
            and more recently with desktop publishing software like Aldus PageMaker including 
            versions of Lorem Ipsum.

        """,
        "note": """
        "Use products from nature for what it's worth - but never too early, nor too late." Fresh is the new sweet.
        """,
    },
    {
        "slug":"nature-is-beautiful",
        "image": "photo-18.jpg",
        "author" :"Sakira",
        "date": date(2021, 3, 20),
        "address": "15 Adr street, 5015, NY",
        "title": "Nature Environment",
        "excerpt" : "Lorem ipsum dolor sit amet consectetur adipisicing elit. Est pariatur nemo tempore repellat? Ullam sed officia iure architecto deserunt distinctio, pariatur",
        "content" : """
            The Cafe was founded in blabla by Mr. Smith in lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

In addition to our full espresso and brew bar menu, we serve fresh made-to-order breakfast and lunch sandwiches, as well as a selection of sides and salads and other good stuff.
        """,
        "note": """
        "Use products from nature for what it's worth - but never too early, nor too late." Fresh is the new sweet.
        """,
    },
    {
        "slug":"Programming-is-fun",
        "image": "photo-13.jpg",
        "author" :"Mira",
        "date": date(2021, 6, 28),
        "address": "15 Adr street, 5015, NY",
        "title": "Programming Is Fun",
        "excerpt" : "Lorem ipsum dolor sit amet consectetur adipisicing elit. Est pariatur nemo tempore repellat? Ullam sed officia iure architecto deserunt distinctio, pariatur",
        "content" : """
            Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
            Lorem Ipsum has been the industry's standard dummy text eversince the 1500s,
            when an unknown printer took a galley of type and scrambled it to make a type 
            specimen book. 
            
            It has survived not only five centuries, but also the leap into
            electronic typesetting, remaining essentially unchanged. It was popularised in 
            the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, 
            and more recently with desktop publishing software like Aldus PageMaker including 
            versions of Lorem Ipsum.

        """,
        "note": """
        "Use products from nature for what it's worth - but never too early, nor too late." Fresh is the new sweet.
        """,
    },
]


def get_date(post):
    return post['date']


# Create your views here.

def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date) # it sorts all_post based on date on existing list
    latest_post = sorted_posts[-3:]

    context ={
        "posts" : latest_post
    }
    return render(request, "blog/index.html", context)



def posts(request):
    context ={
        "all_posts":all_posts,
    }
    return render(request, "blog/includes/posts.html", context)

def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug) 
    #So this will go through all the post in all_post dict, 
    #Look at the slug field . Then if we have the match then 
    #thats the post we want to get basically 

    context ={
        "post": identified_post
    }
    return render(request, "blog/post-detail.html", context)
