# Inspiration
Suicide and depression are major national public health issues in countries such as the United States. Just between 1999 and 2014, the average, adjusted for age, annual U.S. suicide rate increased by a staggering 24%. Furthermore, according to NIH, an estimated 17.3 million adults in the United States have at least one major depressive episode. This number represents 7.1% of all U.S. adults. These shocking statistics is what makes suicide and depression a major public health issue across the nation, and it demands a solution to effectively address the problem at this very moment. Therefore, we decided to create OneLife, a health web application aimed at helping people suffering from suicidal or depressive thoughts, as well as equipping people with the right tools to determine if their loved one is having suicidal or depressive thoughts.

# What it does
OneLife supports people suffering from depression and suicidal thoughts, using machine learning to identify suicidal and depressive thoughts in messages, which can be pasted into a text box or uploaded through an image. OneLife also has a twitter bot which identifies suicidal and depressive messages from social media chats, and sends consoling messages to victims with the National Suicide Prevention Hotline.

# How I built it
In order to build our web application and twitter bot, we used:

Flask
HTML/CSS/JS
Python
Google Cloud: Places and Maps API
Machine learning: Bayesian classifier
Data scraping from various subreddits to create a custom dataset
Socket.io for the real time chat
Twitter API for the twitter bot
Challenges I ran into
The first big challenge we ran into was how to find an appropriate dataset in order to train our machine learning model. After a lot of researching and learning how to web scrape effectively, we were able to scrape information from the r/Depression, r/SuicideWatch, r/CasualConversation, and r/All subreddits. Furthermore, the reddit API only allowed a maximum of 100 posts, so we had to learn how to use a wrapper tool called praw in order to scrape 1000 posts from each subreddit. Another challenge was creating the chat feature in realtime. We learned how to use socket.io to create the forum and chat feature so that people can messages each other in realtime.

# Accomplishments that I'm proud of
We are very proud to have developed a complete working web application. We are also proud to have learned to integrate new technologies such as socket.io, web scraping, and google cloud's Places and Map's API.

# What's next for One Life
We hope to polish off some of the bugs from our code, and conduct more testing of our platform. Then, we plan to deploy it on a server, and release the project for people all over the world to use!
