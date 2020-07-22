# OneLife
A machine learning web app to equip community members with the tools to help people suffering from suicidal and depressive thoughts.

The Get Help Page and Forum Page work best when run locally. Please navigate to the project directory and type `flask run` in order to run our web application!

Try it out! https://onel1fe.herokuapp.com/

## Inspiration
### Problem
Suicide and depression are major national public health issues in countries such as the United States. Just between 1999 and 2014, the average, adjusted for age, annual U.S. suicide rate increased by a staggering 24%. Furthermore, according to NIH, an estimated 17.3 million adults in the United States have at least one major depressive episode. This number represents 7.1% of all U.S. adults. These shocking statistics is what makes suicide and depression a major public health issue across the nation, and it demands a solution to effectively address the problem at this very moment. 

According to research from the WHO, Preventing suicide can have a positive impact on communities by: 
- Promoting health and well-being of community members
- Empowering communities to identify and facilitate interventions
- Building capacity of local health-care providers and other gatekeepers 

### Civic Engagement and Community Importance
Governments all across the world need to take a lead in suicide prevention in order to develop and implement comprehensive multi-sectoral national suicide prevention strategies.  However, research from the WHO suggests that variations in the suicide rates within countries indicate that top-down suicide prevention must go hand-in-hand with local bottom-up processes. Hence, communities play an essential role in suicide prevention when they provide bridges between community needs, national policies and evidence-based interventions that are adapted to local circumstances.

Prevention of suicide cannot be accomplished by one person or institution alone; it requires support from the whole community. The community contribution is essential to any national suicide prevention strategy. Communities can reduce risk and reinforce protective factors by providing social support to vulnerable individuals, engaging in follow-up care, raising awareness, fighting stigma and supporting those bereaved by suicide.

More importantly, communities can help by giving individuals a sense of belonging. It is essential to understand that the community itself is best placed to identify local needs and priorities 

### Solution
Therefore, we decided to create OneLife, a health web application aimed at equipping community members with the necessary tools to help people in their community suffering from suicidal or depressive thoughts. Furthermore, with our get help and forum features, our application fosters a positive and supportive community, which is the key to preventing suicides.

## What it does
OneLife supports people with the tools to help someone in their community suffering from depression and suicidal thoughts, using machine learning to identify suicidal and depressive thoughts in messages, which can be pasted into a text box or uploaded through an image. Through the get help page, the community member or the suicidal person can find local therapists through one quick press of a button. The forum page fosters a collaborative and supportive community for community members to engage in conversations, as well as communicate together with therapists. 

OneLife also has a twitter bot which identifies suicidal and depressive messages from social media chats, and sends consoling messages to victims with the National Suicide Prevention Hotline.

## How I built it
In order to build our web application and twitter bot, we used:
1. Flask
2. HTML/CSS/JS
3. Python
4. Google Cloud: Places and Maps API
5. Machine learning: Bayesian classifier
6. Data scraping from various subreddits to create a custom dataset
7. Socket.io for the real time chat
8. Twitter API for the twitter bot

## Challenges I ran into
The first big challenge we ran into was how to find an appropriate dataset in order to train our machine learning model. After a lot of researching and learning how to web scrape effectively, we were able to scrape information from the r/Depression, r/SuicideWatch, r/CasualConversation, and r/All subreddits. Furthermore, the reddit API only allowed a maximum of 100 posts, so we had to learn how to use a wrapper tool called praw in order to scrape 1000 posts from each subreddit. Another challenge was creating the chat feature in realtime. We learned how to use socket.io to create the forum and chat feature so that people can messages each other in realtime.

## Accomplishments that I'm proud of
We are very proud to have developed a complete working web application. We are also proud to have learned to integrate new technologies such as socket.io, web scraping, and google cloud's Places and Map's API.

## What's next for One Life
We hope to polish off some of the bugs from our code, and conduct more testing of our platform. Then, we plan to deploy it on a server, and release the project for people all over the world to use!
