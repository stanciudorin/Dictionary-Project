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
* Deployment
* Credits
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

## TESTING