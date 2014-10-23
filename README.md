Blog
====
Period 5

David Bang
Jerry Dai
Vanessa Yan
Cindy Wu

This project is a simple blog engine. 

When create.py is run, it will create a database for posts and another one for comments. 
Each post has an id number, starting from 0 and increasing by 1 for each new post. 
Each comment has the same id number as the post that it corresponds to. 
Posts have a name and body attribute and both are text. The name refers to the title of the post and body refers to the content of the post.

When app.py is run, it host a web server. The web server will have index.html as its landing page.
The index page will a text box where you can insert the title of a post. Below the text box is a text area where you can write the contents of the post. Click Submit to post. This will insert the post into the database.
If the post already exists then the post inserted into the database and you will remain on the index page.

The index page also has a list of blog posts below the forms. Initially the list will be empty but as you add posts, there will be a list of links to blog posts.

After clicking a link to a post or submitting a post, you will be redirected to title.html, which will present the post, a text area, and comments. The post will have name or title of the post and the body of the post below it. Below the post will be a form for comments. You can submit comments in this area and it will show up on the blog post page. Comments are listed right below the form.

To go back to the index page, click on the red button with the words Index in it.
