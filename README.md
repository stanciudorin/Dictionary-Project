<div align="center">
  <img src="https://github.com/stanciudorin/Dictionary-Project/blob/master/static/images/Site%20Preview.png?raw=true" align="center" style="margin: 0;">
</div>

# MILESTONE PROJECT 3: [ABC DICTIONARY](https://dictionary-project.herokuapp.com/)

## SOURCE: [Project Repository](https://github.com/stanciudorin/Dictionary-Project)

## ABOUT THE PROJECT
<p>ABC Dictionary is a platform for parents whose children are at the words-learning stage. My aim with this project was to help children learn their first words quicker as, the project in its core base, it has got the most common words that a child should learn first.

The idea for this project came to me as I am a parent myself as well and we are at the point where our little one is learning his first words. I have also tried to help other parents like myself to let them know what words we are staring learning first and also to give them the opportunity of inputting their knowledge into the ABC Dictionary and grow the words database so that children can learn new words every day.

As I had just completed the Data Centric Development Module, learning about Python and the well-known Flask framework, I decided to implement this framework as well as HTML5, CSS3, JavaScript, Mongo DB and Heroku and create a web app that has the full CRUD functionality, for anyone interested to use the website.
</p>

## TABLE OF CONTENTS
* UX 
    * Main aimns
    * User stories
        * Project stakeholders
        * New users
        * Returning users
        * Tablet users
    * Design process
    * Wireframes
* Features
    * Existing features
    * Existing features accross all pagess
    * Features left to implement
* Technologies Used
    * Languages, libraries and frameworks
    * Code editors
    * Additional tools used
* Testing
    * Testing tools
    * Devices used for testing
    * Devices Simulated With In Chrome Dev Tools
* Deployment
    * Deploying to GitHub
    * Cloning my project
    * User Story Tests
* [Credits][CREDITS]
    * Content
    * Media
    * Acknowledgements

---

## UX

 ### Main aims
I expect that the majority of the users will fall into the following criteria::
* To be a parent
* To be a new parent
* To become a parent soon

### User Stories

* Project stakeholders:
* **Myself**: I am the only creator of this platform and want to see it succeed. I would like to attract users in the hope of making the website easy to use, responsive and well structured.

* **Karen M.**: Being a parent, I want to be able to add more definitions to the website.
* **Michael H.**: I want to be able to update any incorrect words and definitions.
* **Tom D.**: I want the definisions to be sorted in aplhabetical categories.
* **Michael C.**: I was looking at the website and I want it to be simple and visually appealing.

* Returning customers:
* **Carole M.**: I have been using the website twice, for both my children, and it helped us a lot. Not only that we can input the words that we are teaching our children, but we can see what other parents inputted for their little ones to learn.
* **Debbie C.**: The website works well and it is easy to use. Very helpfull and the best part is that we can input words and definitions as well and help out other parents with ideeas of what words should be first thought to their children.

* Tablet Users:
* **Michael C.**: I am using my tablet and smartphone frequently and the website is responsive and has a good UI for every device.
* **Debbie C.**: these days I am using my smartphone and iPad more than my laptop and the platform is well built to work on such devices.

### Design Process

* Colours: I have chosen colours based on who I thought, would use my website, basicaly who the website was aimed for. And the answer was PARENTS. Either of single or multiple children, either soon to be parents who are interested to know in advance what words should be first to teach their children. So I went for something neutral, something easy for the eye, not to colorfull and not to sobre. A cream-ish background with some light brown navigation bar to match the theme.
* Structure: Having used the HTML5 as a core structure, I developed four interactive pages for my users. A [Home](https://dictionary-project.herokuapp.com/) page that the user is greated with, showing all categories as the main vied, but when each category is clicked, that particular category expands itself toshow the words that belong to that category of letters. An [Add Word](https://dictionary-project.herokuapp.com/add_word) page, where users can add a word they wish to save in the website's database, the word description and the category of letters the word is part off. An [All Words](https://dictionary-project.herokuapp.com/edit) page, where parents can view all the words saved in our database and finally an [Edit Category](https://dictionary-project.herokuapp.com/get_categories) page where users can edit the category of letters if an existing category get too crowded with words and definitions. Also, good to mention that all these pages have either delete, edit and add word buttons, that function according to their names. The colours used are red for the delete button to evidentiate the "danger" if you are deleting a word, blue for the edit button, a neutral colour that highlights a neutral action of editing and green for save button when saving the word to the database, which indicates a correct and completed action of saving the word.

### Wireframes

* Balsamiq MockUp: I have used this wireframe on all my Milestone Projects and other multiple side project I have worked on, and I find it very easy to use and complex in it's components and functionality to be able to perform professional looking wireframes to show potential clients how their website would look like. In coding my ABC Dictionary, I mostly followed the wireframes created at the beginning, less the search box, which can be implemented at a later stage as the Dictionary gets filled with more words and definitions. All my [Wireframes](https://github.com/stanciudorin/Dictionary-Project/tree/master/wireframes) can be see here.

---

## FEATURES

### Existing features

* Being an open dictionary, we have the ability to add words, add descriptions, add categories, by simply going to [Add Words](https://dictionary-project.herokuapp.com/add_word) page.
* We have edit words, edit description, edit categories by going to [Home Page](https://dictionary-project.herokuapp.com/show_words), chose the category in which the word you want to edit is, look for the word and simply click Edit. thsi will take you to the environment to perform the edit button.
* We also have the ability to delete words.
* We can edit the category names by going to [Edit Categories](https://dictionary-project.herokuapp.com/get_categories) and restructure the categories.
* We have prompt alerts when we are deleting a word, informing us that the word has been deleted.
* We have clickable logo name.
* We have shadows applied to the categories element.
* We have collapsable elements when they are clicked.
* All pages are responsive.
* We have hoover over effects on elements in the body and the nav bar.
* We have pulse effect on buttons such as [Add Word](https://dictionary-project.herokuapp.com/add_word), [Edit Category](https://dictionary-project.herokuapp.com/edit_category/5f3301caf7f7b210e58a6ab9) and [Save](https://dictionary-project.herokuapp.com/edit_words/5f15f8059fe3070e816b812e).

### Existing features accross all pages:
* The website is structured on four pages and all of them can be reached through the navigation bar. The nevigation bar is responsive and is present on all pages and containes buttons that direct the user to all pages. We also have a Logo and the project name ABD Dictionaty which, clicking it, will take you to Home Page.
* Each page keeps the same background, which is a pleasant cream that brings a calmless environment.
* The body is structured in such a way to match its aspect on every page.
* Buttons, collapsable elements and pulsing button effects can be seen througout our pages.
* The same colour scheme on every page.


### Features left to implement
* When the word database grows in such manner that, it would be easier for someone to look for a word to see if its exists before adding it, a search box will definately be added as ouur users would benefit from it better at that stage.
* After growing our community, we can implement a log in function to be able to coordinate the words added, where for each word we can see who added it and when.

---

## TECHNOLOGIES USED

### Languages, libraries and frameworks
* [HTML5](https://en.wikipedia.org/wiki/HTML5): The project uses HTML5 to provide the content and structure.
* [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets): The project uses CSS3 for styling.
* [jQuery](https://jquery.com) and [JavaScript](https://www.javascript.com): The project uses them for interactive elements.
* [Python](https://www.python.org): The project uses Python to run the application.
* [Materialize](https://materializecss.com): The project uses Materialize for layout, responsiveness and elements.
* [Material Icons](https://materializecss.com): The project uses Material Icons for icons.
* [Flask](https://flask.palletsprojects.com/en/1.1.x/quickstart/): The project uses Flask as the framework.
* [Jinja](https://jinja.palletsprojects.com/en/2.11.x/): The project uses Jinja as the templating language.
* [MongoDB](https://www.mongodb.com/cloud): The project uses MongoDB to host the database.
* [GitHub](https://github.com/stanciudorin?tab=repositories): The project uses GitHub to host the repository.
* [Heroku](https://www.heroku.com/): The project is hosted on Heroku.

### Code Editors
* [GitPod](https://www.gitpod.io/): The project was developed in GitPod.

### Additional tools used
* Balsamiq: for developing my wireframes.
* Adobe Lightroom: for developing the logo.  
_No links provided due to both softwares being installed directly on my laptop_

---

## TESTING

### Testing tools

The website has been tested with different tools and on different devices to check its responsiveness, functionality and overall structure.
The following tools and devices have been used to test the website in several different scenarios.

*  Google Chrome Developer Tools: The project used Google Chrome Developer Tools to test responsiveness, styles, and different layouts throughout development. This also allowed the site to be tested on several other mobile devices.

### Devices used for testing

* [Apple MacBook Air](https://www.amazon.co.uk/Apple-dual-core-10th-generation-Intel-Core-i3-processor/dp/B08633F581/ref=sr_1_3?crid=Y6V4SM2K3QKH&dchild=1&keywords=macbook+air+2018&qid=1597952568&sprefix=macbook+air+2018%2Caps%2C202&sr=8-3): the entire project was developed on a 2018 MacBook Air that runs on macOS Catalina.
* [Apple iPad Air 2nd Generation](https://www.amazon.co.uk/Apple-iPad-Air-10-5-inch-Wi-Fi-64GB/dp/B07NHQQ27K/ref=sr_1_16?crid=26JWMWRCVIBDE&dchild=1&keywords=ipad+air+2nd+generation&qid=1597952866&sprefix=ipad+air+2nd%2Caps%2C212&sr=8-16): for testing it's responsivenes on iPads and screens smaller than a regula laptop, I used my iPad Air connected to my lapop wirelesslly. The results were positive as all its functiones worked as normal.
* [Apple iPhone 7](): havig all three Apple devices connected to my iCloud Account, I managed to phisically test my website on my iPhone 7 without any issues. The website was responsive and all its functions worked as normal.

### Devices Simulated With In Chrome Dev Tools.

* Samsung Galaxy S9/S9+
* iPhone 6/7/8
* iPhone X
* iPad

I used the following web browsers on both desktop (macOS) and mobile (iOS) where available.
* Google Chrome: Version 84.0.4147.125 (Official Build) (64-bit)
* Safari: Version 13.1.2 (15609.3.5.1.3)

The project was run through both [HTML Validation](https://validator.w3.org) and [CSS Validation](https://jigsaw.w3.org/css-validator/) with no errors found.

* HTML and CSS tests carried out have been documented and visualised [here](https://github.com/stanciudorin/Dictionary-Project/blob/master/Testing/HTML-CSS%20Testing%20results.png?raw=true).
* JavaScript tests carried out have been documented and visualised [here](https://github.com/stanciudorin/Dictionary-Project/blob/master/Testing/JavaScript%20Test%20results.png?raw=true).
* Python tests carried out have been documented and visualised [here](https://github.com/stanciudorin/Dictionary-Project/blob/master/Testing/Python%20Testing%20results.png?raw=true).

---

## DEPLOYMENT

I created my project on GitHub and used GitPod's development environment to write my code. Use the following link to view my live project: [ABC Dictionary](https://dictionary-project.herokuapp.com/show_words).

### Deploying to Heroku

To deploy this page to Heroku from its GitHub [repository](https://github.com/stanciudorin/Dictionary-Project), the following steps were taken:

1. Go to the Heroku Dashboard and create a New App with the region set to Europe.
2. In the Settings tab of your app click Reveal Config Vars.
3. Enter the required environment variables, IP, PORT and MONGO_URI.
4. In your IDE of choice create a env.py containing the MONGO_URI and add it to the .gitignore
5. In your IDE of choice create a requirements.txt by using the command pip freeze -local > requirements.txt
6. In your IDE of choice create a Profile by using the command echo web: python app.py > Procfile
7. Go to the Deploy tab and select Heroku Git.
8. In your IDE of choice use the command git push heroku master.

Note: You will need the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) downloaded and installed to push from the command line.

Further reading and troubleshooting on deploying to Heroku can be found [here](https://devcenter.heroku.com/categories/deployment).

### Cloning my project

If you would like to work on my project further you can clone it to your local machine using the following steps:

1. Scroll to the top of my repository and click on the "clone or download button"
2. Decide whether you want to clone the project using HTTPS or an SSH key and do the following:
    * HTTPS: click on the checklist icon to the right of the URL
    * SSH key: first click on 'Use SSH' then click on the same icon as above
3. Open the 'Terminal'
4. Change the current working directory to the location where you want the cloned directory
5. Type 'git clone', and then paste the URL you copied earlier.
6. Press 'Enter' to create your local clone.

* You can find both the source of this information and learn more about the process on the following link: [Cloning a Repository](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository).


### User Story Tests

1. Site is simple and visually appealing:
    * The feedback I have received so far indicates that this is true.
2. The words are sorted by categories:
    * Go to the "Home" page.
    * Four alphabetical categories are visible.
    * Click on one of the categories, the corresponding words are now visible.
3. Update incorrect Words:
    * Go to the "Home" page.
    * Click on a category from which the word you want to update is part of.
    * Choose the term you wish to edit and click on the "Edit" button.
    * Make the desired changes.
    * Click on "Save".
    * Click on the category of words storing the word you updated to view the changes.
4. Add words to the site:
    * Go to the "Add Word" page from the menu in the navbar.
    * Chose a category.
    * Enter the details.
    * Click on "Add Word".
    * View new word by clicking on the category you placed it in.
5. Delete words:
    * Go to "Home" pane.
    * Click on a category which you want the word to delete from.
    * Click on "DEL" button.
    * You will be redirected to "Home" page so you can check if the word has been deleted.
6. Edit Categories:
    * Click on "Edit Categories" button from the menu bar at the top of the website.
    * Select the category you want to edit by clicking on the "Edit" button.
    * Chance it to the desired letter or group of leters.
    * Click on Edit Category.
    * View the edited category.

#### All tests performed with no errors found.

## CREDITS

### Content
* The project uses [Materialize](https://materializecss.com) elements.

### Media
* The Logo was created by myself using Adobe Lightroom.

### Acknowledgements
* My Mentor __@Owonikoko Oluwaseun__ for helping me through the project with her advice and guidance.
* Slack Community for their replies and good advices.
* Tutor Support for answering my questions and explaiing a few things step by step.