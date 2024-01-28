## Testing

- I confirmed that this project is responsive and looks good on various common screen sizes by using the devtools devices toolbar.
- I have confirmed that the username input validation works. There is an error message if the field is not filled out correctly.
- I checked that the modal opens upon clicking "How to Play" and can be closed by either clicking the little X, or anywhere on the page outside the modal.
- I ensured that the timer works correctly, starting at 30 seconds for each new question and stoping once an answer is selected.
- I made sure that the answer buttons give a correct colour-coded feedback upon selecting and clicking on an answer: red for incorrect, green for correct.
- I ensured that the "Play again" button takes the user to the start of the quiz, while the "Home" button takes the user to the start page.
- I confirmed that header and footer are easily readable and understandable.

### Fixed Bugs

- When creating my categories, the site did not display correctly when appending /category/one-of-my-categories to the url even though the url was constructed correctly. The solution was that in the class CatListView(ListView), the variable template_name was incorrectly set to 'category.html', while the correct path was template_name = 'blog/category.html'.
- When creating my categories-dropdown in the navbar, the categories did not display. The reason was that I had used data-toggle="dropdown", which came from older Bootstrap versions. Fixed by changing to data-bs-toggle="dropdown", which is the correct attribute under Bootstrap 5.
- There were underscores between the icons in the footer. Fixed by removing whitespaces between the Font Awesome icons and their anchor tags.
- When a logged in user clicked on "Add to favourites" on a post which they had previously already favourited, then the post was removed from the user's favourites. Fixed by changing the content of the button so a user would know that clicking the button again would result in "Remove from Favourites".

### Unfixed Bugs


- On mobile view, if the blog post title was too long, the Add to/Remove from Favourites button was not or only partly visible.

### Validator Testing

- HTML ([W3C Validator](https://validator.w3.org/))
    - 1 error found: "Section lacks heading. Consider using h2-h6 elements to add identifying headings to all sections, or else use a div element instead for any cases where no heading is needed."
    - Solution: introduced h4-element to the section and set it to display = none.

- CSS ([Jigsaw](https://jigsaw.w3.org/css-validator/))
    - No error found.

- JS ([JS Hint](https://jshint.com/))
    - 1 error found: one unnecessary semicolon.
    - Solution: deleted unnecessary semicolon.

- Performance, Accessibility, Best Practices, SEO (Lighthouse Chrome Dev Tools)
    - Accessibility is at a still high 94 due to some color contrasts not being as strong as they could be. After discussing with my group facilitator and mentor, it was decided to keep it as is.<br>
    - ![Lighthouse rating](assets/images/readme-images/performance-lighthouse.png)<br>

### Browser Testing (section adapted from Kay Welfare, results are my own)

**Layout:** Testing layout and appearance of site for consistency throughout browsers.

**Functionality:** Ensuring all links, navigation and form submit functions as expected throughout browsers.

| Browser     | Layout      | Functionality |
| :---------: | :----------:| :-----------: |
| Chrome      | ✔          | ✔             |
| Edge        | ✔          | ✔             |
| Firefox     | ✔          | ✔             |
| Safari*     | ✔          | ✔**           |
| IE          |deprecated by Microsoft, not tested|

The timer seems to start with a slight delay. In order to optimize the timer's start, the respective function was placed far up in the code to prevent as much as possible that other code is executed before it. Since the slight delay only means that on the one hand, the user gets a bit more time, and on the other hand, the user's attention gets drawn to the time-pressure more, it was deemed acceptable. Also, the lighthouse report revealed a performance rating of 99.

*Only available to me on iPhone. My mentor kindly reviewed the site for me in Safari on desktop.<br>
**On mobile (which I reviewed), modals (error message or rules) can only be closed by clicking on the little X, not by clicking on the screen outside the modal. As there are two options for the same result, and one works completely fine, it was deemed acceptable.

### Manual Testing (section adapted from Kay Welfare, results are my own)

| Feature     | Expect      | Action        | Result |
| :---------: | :----------:| :-----------: | :-----:|
| **Username input field**   | As a user, I can input my chosen username   | Various usernames were put in  | Username inputs were accepted |
| **Let's Start! Button w/o username filled in**  | When clicked, an error message will appear prompting the user to fill in a name  | Clicked Let's Start! without putting in a username | Error message appeared |
| **Let's Start! Button with username filled in** | When clicked, the game will start  | Filled in a username and clicked "Let's start!" | Game starts |
| **How to play Button** | When clicked, a modal will open with the rules | Click How to play | Modal containing the rules of the game opens |
| **Rules modal and error message** | Rules/Error message will close when clicking the little X, or outside of the modal | Clicked X, and outside the modal | The modal closed |
| **Timer - select answer** | Timer will countdown the seconds. Upon selection of an answer, the timer stops | Selected an answer within the 30 seconds countdown | Timer stopped |
| **Timer - not select answer** | Timer will countdown the seconds. Upon expiry of the time, answer options get disabled | Let the countdown run out | Answer options got disabled |
| **Answer buttons** | When clicked, receive feedback on whether answer was correct/incorrect | Clicked various answer buttons | Buttons highlight orange when hovered over. Upon clicking, buttons get disabled and the correct answer is highlighted green. Incorrect answer, if chosen, is highlighted red |
| **Next button** | Take user to next question | Click the button | Next question is displayed. After the last question, final score is displayed. |
| **Play again button** | Take user back to first question and reset the score | Click the button | First question is displayed. After answering all questions, new score is displayed. |
| **Home button** | Take user back to the home page | Click the button | Home page is displayed. User can choose new username |
| **LinkedIn icon in footer** | LinkedIn will open in a new tab | Click the icon | LinkedIn profile of the page's author opens in new tab |

### Testing User Stories (section adapted from Kay Welfare, results are my own)

| Expectation                         | Result                          |
| :---------------------------------: | :------------------------------:|
| I want to know what this site offers at a glance. | As a visitor, I can see the header which tells me the topic of the site, and a message telling me that this is a game |
| I want to see a responsive design which looks good on mobile devices as well as on larger screens. | As a visitor, I have a good view of the site on mobile device without overflow or side-scrolling |
| I want to be guided through the site by an intuitive design, and not be distracted by unnecessary elements. | As a visitor, all options I can choose from, such as inputting a username, or learning the rules of the game, or choosing an answer, are displayed on one page |
| I want to have a positive, joyful experience. | As a visitor, I am greeted by a joy- and colorful design which is consistent throughout the game |
| I want to get feedback on my actions such as inputting a username or answering questions. | As a visitor, I get an error message if I forgot to put in a username. I also get color-coded feedback whether my chosen answer is correct or not |
| I want to learn about Indian weddings. | As a visitor, I can take my time to read through the answers and learn about different functions of Indian weddings |
| I want to see how much time is left for answering a question. | As a visitor, I see a countdown showing the seconds left for answering a question. |
| I want to see my final score. | As a visitor, I see my final score after answering all questions |
| I want to be able to play again, or let a friend play on the same device after I am finished. | As a visitor, I can choose to play again after finishing the quiz, or choose a new username by going back to the home page |
