# Data-Centric Project
## Curiousity Skills

This website is a database project aiming to receive its own data from the community. It will take in accounts of people's experiences in work and educational settings while also allowing them to search for other people's experiences. Users are able to upload their experiences during work with clients and colleagues, or their experiences as a student or a teacher. With these uploads, data can be collated and extrapolated. For instance, a very useful metric would be the salary search tool, where users can use to check the pay rates of everyone else in a particular job level in a particular industry of their interest. Target users would particularly be aimed towards those living in Singapore as the salary currency has been standardised to Singapore Dollars.

Note: THe rest of this readme file will refer to Work as "W", and Education as "Edu"

#### UX:
**<u>Strategy</u>**

A platform understands the importance of unity of the common folk. We need to work together, regardless of which industry or job position we hold. We cannot allow corporations to take advantage of us, while we keep quiet and accept whatever they tell us for fear of losing our jobs. A platform is needed for the all the common folk to voice their opinions, share their stories and information so that everyone can learn what is going on everyday to everyone else. If we are more informed, the better choices we can make for ourselves whether is it to increase our performance at work or to fight for working rights. 

This platform also serves to collate a range of data such as age range, job levels, roles, education subjects which can be used further down the road which can be cleaned and modelled down the road to reveal more interesting and possibly nexpected results. 

Below are some real-life user stories, which this platform might have the potential to overcome and be increasingly useful in the future as more data is collected over time.


User 1 Story: "I can't find anywhere indicating how much a particular job pays their junior level or entry level employees. Even the bigger websites take statistics of only a handful of salaries into account and that is mainly based in the United States, which is not as relevant for someone living in Asia."

User 2 Story: "I have been working in my company for over 30years and I think I've been underpaid as compared to my ex-colleagues and ex-classmates who are working in the same industruy and have similar job hierarchy as me. Is it me that is underpaid or is it them that are overpaid? There isnt enough transparency for companies to disclose this information to prove that they are paying their workers enough."

User 3 Story: "I have been struggling in my banking job for a while, both with clients and my colleagues where there is so much politics involved at every stage. I want to know how others do it, but I don't expect anyone at work to share their secrets with me. And I dont want to reveal to my superiors that I am struggling. I wonder if there is anyone else in my position who managed to overcome this."



**<u>Scope</u>**

Create: Able to create 2 types of experiences, W experience and Edu Experiences, from the home page. In order to avoid asking for too much information from the user, I decided to zero in on a limited number of questions to be asked from users based on what users in turn might what to see. 
A work profile is always asked as a standard for both W and Edu experiences to set the context. It includes 3 pieces of information: 

1) Job Category - People would be interested in experiences in their own industry and what differences there are across different companies. The category list is created with its content obtained from a source which covered a strong amount of every industry so that anyone can contribute to the website. The source is (recruiter.com)[https://www.recruiter.com/careers/]
2) Job Level - Job level list is obtained from the most common job hierarchy to cover most aspects of a company's organisational chart. The list is from (bizfluent)[https://bizfluent.com/info-8386051-five-types-jobs-levels.html]
3) Salary - Everyone's salary can differ ever so slighlty, if an average or any calculatation was to be needed in future, specific integers will ive us the most accurate numbers. 

Data Fields to collect from both W and Edu experiences: 
1) Age range is important as the way we interact with others may be considerably affected by the other party's age. By obtaining the age_range of the interaction, the search engine has potential to further optimise in the future. 
The only difference between the work and education's age range's context is whose age range it is referring to. W experience entries refer to the colleague/client's age, while Edu experience refers to the age of student/teacher depending on the chose role of the author. Age range categories was obtained from (SingStat)[https://www.singstat.gov.sg/find-data/search-by-theme/population/elderly-youth-and-gender-profile/visualising-data]

2) Title and Details: Since we are collecting real-life stories, it is natural to collect a title and the details whether is it a W or a Edu experience. 

3) A date is also collected to provide context into the experience. For example, if the experience was from 20years ago, work and education cultures would be siginifcantly different then as comapred to today. That would hold true in many years from now as well. 

** A field of data to be collected that are specific to the W experience is the Gender: The way we behave and interact can be drastically across different genders. Knowing the gender of the other party would give better insight into the situation

Fields are data specific to Edu experiences include:
1) Education Role: It is important to categorise whether the author is the teacher or the student. While that would be information that we will find out after reading the stories, when we have an abundant about of experiences, the search engine will be easily optimisable to incude for e.g only teacher or only student experiences. 
2) Education Institute Type: Different types of educatin settings can have massive influences on the situation. For e.g if one were a teacher or student in a public school, he/she might be more interested in finding out what its like to teach or study in other public schools to find out similarities and differences. 
3) Education Level: The methods we use to teach or study must take into account the education level. For e.g A university student might not be interested in seeing how a student in priamry school prepares for exams. 
4) Subject: Different education subjects will require different methods of teaching. If one were teaching Geography, he/she might not be interested in how a Mathematics teacher teaches calculus. 

**Note: All these fields are long term goals to be used to help optmsie the search engine to include more filters so users can find the stories they want to see as conveniently as possible. 

Read: Search Engine to assist users in finding the the experiences they want to read about based on search criterias - Job Category, Job Level, Experiences only or Salary only. Within the results page, another search tab will be available to those who want to search all experiences by title only. This is to provide stronger search specificity as the database grows. 

Update: Once the user has found an experience of interest. He/she can click to view all the details, followed by having the option to edit it. 

Delete: Once the user has found an experience of interest. He/she can click to view all the details, followed by having the option to delete it. 

**<u>Structure</u>**

Navigation Bar will always be available on every page for users to return back to the homepage where the main search bar is located. 

Search Bar results will return a template with Single Page Application where the user can navigate to choose between displaying W experiences or Edu experience based on their previous input on the homepage. Within this page, there is another search tab to search by title. The page will refresh based on the user's input to immediately display search results. 

Clicking on each search result will bring the user to another template where he/she can view all the details of that experience entry.

From the viewing template of each entry chosen from a search results list, the user can choose to edit or delete this record, which will then redirect the user back to the search results. 

Defensive Programming with if else statements are constructed to help ensure that the program returns an error template instead of crashing the website. 


**<u>Skeleton</u>**

###### Search Functions:
Home Page Search Engine: searches by (job category AND job level) AND a radio input for (salary OR work experiences)

Title Search Bar: searches all experiences created by title.

###### Create Entries portion:
Forms are displayed with simplicity in mind, with dropdowns to choose from a set of categories in order to standardise search results. 

###### Display Results portion:

If user chose the salary radio button: Results from main search engine are arranged in ascending order based on salary amount. Only job category, job level and salary are displayed for easy-to-see comparisons. 

If user chose the work and education experiences radio button: Results from main search engine and search bar are arranged in alphabetical order of the job category. After reaching the results page, users can navigate to either see work experiences or educational experiences. In each result item, three categories are shown: 
1) Work Profile
2) Background - also includes a snippet of the title of the experience so the user has a sense of what to expect if he/she chose to ciew the details of the entry.
3) Action - only has a view function, so a user cannot delete entries at a whim. 

###### Individual Experiences portion: 
Individual experiences includes the remaining details that were not shown before such as the date of the experience, full title and entire details of the experience. It will also provide the option for the user to edit or delete the entry. 
1) Display: Shows all the details: work profile, background, title, details and date. 
2) Delete Button - If the user chooses to delete an entry, a modal will pop up to warn the user as well as to prompt for a second time in case the button was clicked on by accident. There will be an option to exit, or one to proceed to delete. 
3) Edit Button- If the user wants to edit the entry, the last entered entry will be provided on the left side of the webpage for reference. This will assist the user who could either copy and paste all the details followed by making small edits, or he/she could rewrite the experience while refering to previous entry without having to open two tabs and constantly switching between them. More often than not, the first document we write isn't the best version of itself. 

**<u>Surface</u>**

A dark theme with light colored image used to portray a professional look as this website is aimed toward self-improvement. Font is standardise to one easy-to-readfont, and to provide conistency throughout the UX. Body of the UX remains mostly white colored except for the salary results where some color contraast was made to highlight the salary amount. Tables are used to showcase search results to provide a good structure and alignment for easier interpretation. 


#### Features
1) Search Engine to filter for articles of interest
2) Template to navigate through search results and choose to view an article of interest
3) Ability to create a record and store it in a database. 
4) Ability to edit the record
5) Ability to delete the record

##### Features left to implement:

- add flash message when an entry has been created
- add a login functionality so that users can create their own account, and only account users can delete their own entries.
- addition of comments section to each page to allow for community discussions
- further refine search engine to provide better filtering


#### Technologies used
- HTML
- CSS (only used in the Jinja document)
- JAVASCRIPT (only used in the Jinja document)
- jQuery (only used in the Jinja document)
- BOOTSTRAP
- FLASK
- MYSQL
- BEAVERDB
- PHPMYADMIN
- HEROKU (for deployment)
- Git Hub (for version control)
- Google fonts
- Cloud9 (IDE)


#### Testing 

** no automated testing for this project
** manual testing conducted

Quickly reloading the page multiple times causes a lag.
Navigation through webpage, tested and working.
Uploading of both W and Edu experiences tested and working
Editing of both W and Edu experiences tested and working 
Deleting of both W and Edu experiences tested and working. 
Search functionality is tested for every job category with every job level, tested and working.


#### Issues
- using hardcoded methods to retrieve id number of the dropdown options obtained from database. 
- this is followed by If else statements with hard-coded information such as "." and index numbers were used to resolved issues with double digit options in drop down selectables. If options list were to go past 2 digits, a new strategy will be needed to resolve this. 
- using hardcoded methods to retrieved "-Any-" option in dropdowns. 
- using multiple if else statements to optimise search engine filtering. Not very efficient, may have to look into Object Oriented Programming to clean up the code at a later stage. 


#### Deployment

Github repository named "Curiousity Skills" was created for this project. Regular commits were made to display progress of the website over a period of time. In the first 0-20 commits, significant changes were made to the code to accommodate for mySQL database changes due to foreign keys mistakes. 

The site is deployed directly from the Heroku App, where ClearDB is the specific SQL database and Heroku uses the installed DBeaver to access the database. 

Link to the webpage can be found [here.](https://jtxcuriosityskills.herokuapp.com/)


#### Credits

##### Acknowledgements:

-list of job categories for work profile by [recuiter.com](https://www.recruiter.com/careers/)

-list of job levels for work profile by [bizfluent](https://bizfluent.com/info-8386051-five-types-jobs-levels.html)

-list of age ranges from [singstat](https://www.singstat.gov.sg/find-data/search-by-theme/population/elderly-youth-and-gender-profile/visualising-data)

list of education topics:
- [timeshigheducation](https://www.timeshighereducation.com/student/subjects)
- [MOE SG GOV 1](https://beta.moe.gov.sg/secondary/courses/express/)
- [MOE SG GOV 2](https://www.moe.gov.sg/education/pre-university/gce-a-level-curriculum)
- Hero Image by [pexels](https://www.pexels.com/photo/man-holding-white-teacup-in-front-of-gray-laptop-842567/)

