# Unicorn Attractor Issue Tracker 
## project by Alex Thirlwell

Unicorn Attractor’s Issue Tracker is a Django application that will allow users to view, add and give feedback to, a range of different bug and feature requests that may arise out of the use and development of the Unicorn Attractor. The application provides a simple and effective system for users to understand the issues others have experienced, as well as giving them the ability to interact with these issues by commenting or liking the posts, to ensure that the development team for the Unicorn Attractor can prioritise the work they need to complete. The application allows users to make feature requests and asks them for their card details to cover the cost of developing these features. Users can access a blog to receive updates on new features, and general news from Unicorn Attractor. Users can also keep up to date with the bugs and feature requests they have logged themselves on the profile pages.

## UX

For this project, I identified three user stories, each involving a hypothetical user who represented one of three different demographics, namely: unregistered users, registered users, and developers.

### User 1 - An unregistered user of the application who wants information about any issues with the system.

This user will be able to look at the application to see any of the existing issues that have been reported, they will also be looking for a reason to register. They will be someone that uses the Unicorn Attractor and might have an issue they want to report, but do not have a login for the Unicorn Attractor Issue Tracker application.

I have met this user’s needs by providing them with a detailed view of all of the currently open bugs and feature requests, and given them pointers as to why they should login or register. This will help them find the issue they have experienced when using the Unicorn Attractor and therefore see if their issue has been reported already by another user. The Home Page also contains helpful information to enable unregistered users to understand the benefits of the Unicorn Attractor Issue Tracker and the features available once users have registered. 

### User 2 - A registered user who wants to keep updated with the issues they have logged, or features they have paid for.

This user is someone who has already registered with the Unicorn Attractor Issue Tracker and needs to be able to track any bugs they have reported, or features they have requested. They will also want to hear from the company to understand what bugs and feature requests are being prioritised and why they should continue to login and add features to the system.

I have met this user’s needs by providing them with a user profile page that will give them a full list of all of their bugs and features that they have logged and any updates relating to those bugs and feature requests. For example, when their feature request has been listed as “in testing” by the developers the User 2 will be able to see that progress has been made in making their feature request a reality. The blog provides them with the communication they need from the developers of Unicorn Attractor and the community feel of the site gives this user encouragement to keep using their login. They will also get the benefit of having a direct input into the development of the application as they can request any feature they need.


### User 3 - A developer for Unicorn Attractor who needs to understand which bugs and features need to be worked on.

This user will be using the system on a daily basis to check for new bugs and feature requests. They will need to have “Superadmin” controls so they can update any issue they have been working on to keep the users informed on the progress of their bugs or feature requests. They will also need to be able to quickly and easily find issues within the application.

I have met this user’s needs by giving them a system that shows all of the basic information at a glance, and can show a fully detailed view with a click of a link. User 3 will also be able to view any comments written by users and see which bugs have been common and which feature requests are popular. This will help them understand what work to prioritise when working through user issues.

## The Design Process

I designed the project using the wireframes that are available here: https://drive.google.com/open?id=13XeuSf7rnc4y5ugOBmQDoJWjpyIEZpIb

The first page a user will go to is the Home Page, so I needed to take some time to think about the style of this page and the information that it would show. This is important to consider as this is the first impression everyone will get of the application so it needs to tell the user what the application does and why they should use it, while also being helpful for existing users and the development team. My design for this page, seen in the “Home Page Design” wireframes, was created with each of the 3 aforementioned users in mind. User 1 will get an overview of the features of the application and an idea of how the application can be used. This will help give them an incentive to register on the site. User 2 can use the context buttons on the homepage to go directly to the area of the site they need to go to, as there are buttons that display the number of bugs that have been added, and the number of feature requests. User 3 will also be able to use these buttons as they can quickly identify what needs to be prioritised based on the count displayed on the buttons. 

The login and registration pages were designed with simplicity in mind as the user should be able to quickly enter in their information and start using the application as quickly as possible. The login page, which can be seen in the “Login Page Design” wireframes presents two simple boxes with a clear heading that directs the user to enter their details and redirects them straight to the homepage so they can continue navigating the application. The registration page, which can be seen in the “Registration Page Design” wireframes, follows a similar style, by presenting the user with clear instructions to create a login. As soon as they have entered in this information they will again be redirected to the homepage, so they can explore the rest of the site. Each user benefits from this system, User 1 will be able to register very quickly as soon as they have been convinced that a login is beneficial for them. User 2 and 3 are able to access the application very quickly and start using the application in the way that best suits them.

The next decision I needed to make was how I would design the user facing representation of bug reporting and feature requests that had been recorded on the system. I settled on the concept that this information would be presented in a table, as it allowed for a lot of information to be presented very simply to the user. The final design choice for this view can be seen in the “Bug/Feature Request Page Design” wireframes. This allowed me to present 10 rows of data that could be easily filtered and searched through to provide the best user experience. User 1 can easily see if there has been an issue reported that is similar to theirs on the system. User 2 will be able to see any of their bugs and feature requests, and go directly to the relevant page so they can get an update on how their bug is being fixed or how their feature request is being added to the Unicorn App Tracker. User 3 can see an overview of where bugs are along the development lifecycle and this will enable them to prioritise their work.

The blog is an important element of the application and brings together the community feel that I implemented into the application. Adding in a way the development team can interact with the user base helps tie the two together and builds a sense of trust and an understanding that issues will be resolved and the users will be well informed. If this element was not involved, it would be difficult for the development team to interact with the whole user base and could cause bugs to go unreported. The design of the blog, seen in the “Blog Page Design” wireframes was focused around making each post clear and easy to read/engage with. User 1 will not be able to see the blog content, but will see that it is a feature through the home page and will be intrigued by the idea of it and will want to register. User 2 will be interested in hearing about the development plans of the Unicorn Attractor development team and would appreciate any hints or solutions detailed in blog posts that might help them overcome the issues they have faced when using the Unicorn Attractor. User 3 will be able to directly contribute towards helping users by creating content that will resolve user issues.

## Features

### Current Features

Authentication - The authentication system enables users to access the system, add and edit bugs and features, as well as view blog posts and the “Stats” page. If a user is not logged in they do not have access to the key areas of functionality including: 
adding bug reports/ feature requests;
commenting on bug reports/ feature requests;
logging that they have experienced a bug already reported on the app; and 
logging their interest in a feature that has previously been requested on the app. 

Adding Bugs - simple forms that enable users to add the details of the bugs they have experienced when using the Unicorn Attractor application.

Adding Features - simple forms that enable users to add a request for a new feature to be added to the Unicorn Attractor application. 
 
Paying for features - feature requests can only be added once payment has been made. Payment is made through a basic Stripe Library system which collects the user’s card details.

Interacting with bug reports/ feature requests - allows users to interact with a community to help and share problems and solutions by logging the fact that a user has also experienced a bug that has already been reported or would be interested in a feature that has already been requested.

Commenting - creates user interactivity to help them and the developers understand issues associated with the Unicorn Attractor application and the potential solutions/ new features that could enhance the application.

Statistics - helps the user see the benefit of using the system as they can see how quickly the development team move through issues that have been logged on the system.

Editing bug reports and feature requests - enables users to amend typos and add/remove details as needed.

A Blog - helps the development team engage with the user base to help the users understand the new features, fixes and explanations behind what has been developed and what will be developed in the near future.

User Profile - enables the user to track all of their outstanding issues and keep up-to-date with the progress the development team have been making with their bug reports and feature requests.


### Features to add

Email system – a system that informs users when their bug has been resolved or their requested feature has been developed. This will help users engage with the software.

Images for the blog - a nice visual element to engage users with the Unicorn Attractor Issue Tracker application and provides a higher quality of content.

Editing comments - currently there is no way of editing a comment, so more comments have to be made to provide clarity or rectify typos. Editing would make these rectifications clearer and quicker.

Like and dislike comments - this helps strengthen the community aspect of the application as it allows users to promote solutions, or problems that have been raised by the user base or the development team.

## Technologies used

Django, Python, HTML, CSS, JavaScript, Bootstrap, Pygal and Stripe

Django and Python - helped create the full backend logic that was able to seamlessly integrate with the frontend views. The Django ORM helped provide the admin and database for the application. I was also able to use inbuilt Django modules such as Paginator and Messages to further improve the use of the Unicorn Attractor Issue Tracker application.

HTML, CSS and Bootstrap - helped provide the frontend styling of the application, working with Python and Django to display the information from the database.

Pygal -this was used to create dynamic charts based on what has been logged onto the system.

Stripe - used to process the payments for new feature requests created by users.

Javascript - a simple clock application was added to the system to help users and the development team to track how long an issue had been left open. 

## Testing

### Automated Testing

I implemented some automated scripts to check that the urls resolved properly by utilising the Django in-built test suite. This helped me make sure the routing for the website worked effectively. The application is connected in a variety of ways as there are multiple apps connecting the application together. For any failing tests, I was able to find the error and quickly resolve it before moving into the next section of the application. Without using this, development time could have been a lot longer.

### Manual Testing

Most of the processes within the Unicorn Attractor Issue Tracker application were best tested through manual, “in-browser” testing. The homepage was tested by viewing the page locally and using the chrome developer tools to make sure that the elements on the page were properly styled. A similar approach was taken when developing the blog as the look and feel of this feature is important to the user. For both of these aspects of the application it was also important to make sure that the content on the page was spelt correctly. 

For the majority of processes within the Unicorn Attractor Issue Tracker application, the best way of testing them was to try adding new issues and comments to the application to see how the application would display the information to the user when it had been recorded. This approach helped me test that the issues were being ordered by date, and were showing on the correct pages. This was clear evidence that the search functionality was working as intended. Another aspect that was useful to test in this way was the routing between recording a new bug or feature, and the next page that a user would see once their bug report/ feature request has been added.  It made the most sense to direct this to the relevant view page for bugs or features. A decision had to be made about where it would be best to redirect to once a comment had been added. Again, I took the decision to ensure the comments would redirect to the view page, showing the user the comment they had just added to the system. 

Another aspect to test was the likes and dislikes system. Across the application the buttons for this feature work the same way, a like is positive feedback, while a dislike is negative feedback. However, the terms Like and Dislike did not make sense when they were being applied to bugs or feature requests, so I needed to make sure these buttons made sense. For example, on a bug report, the ‘Like’ button is labelled, ‘I have this too’ and once this has been pressed, it will display a message to the user. The wording of this message had to be carefully considered, to ensure it made the most sense when the user reads it. In this case the message reads, ‘Thank you for reporting that you have this bug’.

In adding a payment option to the system, I needed to ensure that a user had to pay for the feature request before adding it to the database. To do this I used some JQuery that would disable the “Save” button, and only activate it once the payment information had been added into Stripe. This feature also extends to editing a feature request, and this was done deliberately to make sure that users contacted the development team if they need to go over any details and make any amendments to their feature request. This also helps avoid a situation where a user can request multiple features within a single feature request payment.

In testing the application, I came across an issue with comments for the blog which meant I had to remove them from the system, as the issue seemed more complicated than others that had materialised. I plan to resolve this issue in the future and hope to have this aspect of the application working soon. To overcome this issue, I decided that the best way of dealing with the issue was to create a second branch within the repository, make the necessary changes to my code, and then add the clean code to the master branch of the repository. 

## Deployment

This project has been deployed to Heroku, and can be found at the following URL:

https://online-issue-tracker.herokuapp.com/

The login details for the application are:

Username: admin

Password: mainuser

Feel free to register your own user as well.

Deploying a Django app to Heroku proved to be quite a tricky process as there are a few issues that can arise. One issue I found was in how my static files were configured in the settings panel. I had to make sure these were perfectly correct, otherwise the build would fail completely. Another issue that arose was a database issue. Heroku does not support sqlite, so the database needs to be transferred to Postgres for the application to work properly. I eventually found a helpful guide that took me through the full steps of how to deploy a Django application to Heroku.

https://medium.com/@BennettGarner/deploying-django-to-heroku-connecting-heroku-postgres-fcc960d290d1

After I had followed these steps, the application worked without an issue.

## Credits

Stackoverflow and medium articles to help me to deploy the application and solve bugs throughout the development of this application.

https://www.youtube.com/channel/UCWEHue8kksIaktO8KTTN_zg - I used some of these tutorial videos to implement features into the application such as Paginator and searching within the site.

The specific videos are listed below:

Pagination - https://www.youtube.com/watch?v=q-Pw7Le30qQ&list=PLEsfXFp6DpzQFqfCur9CJ4QnKQTVXUsRy&index=27

Searching - https://www.youtube.com/watch?v=eyAIAZr5Q3w&list=PLEsfXFp6DpzQFqfCur9CJ4QnKQTVXUsRy&index=37

Bennet Garner for his Medium post on deploying to Heroku - the link can be found in the deployment section.

## Media

Banner image on the home page pf the application- https://pixabay.com/photos/team-team-building-success-computer-3373638/
