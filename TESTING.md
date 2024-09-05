# Testing

## Сontents

* [Introduction](#introduction)
    * [Lighthouse](#lighthouse)
* [Manual Testing](#manual-testing)
* [Validator Testing](#validator-testing)
* [Bugs](#bugs)
    * [Unfixed Bugs](#unfixed-bugs)

## Introduction

Throughout the development of the site, I used Google's developer tools to identify and fix any problems along the way.

I've thoroughly tested each page using Google Chrome's developer tools to ensure each page is responsive on a variety of screen sizes and devices.

### Lighthouse

I used Lighthouse within the Chrome Developer Tools to test the performance, accessibility, best practices and SEO of the website.

### Desktop Results

The site showed good scores.

<br>

Home page
<br>

![Home](/static/images/readme-img/desktop-index.png)


### Mobile Results

The site showed good scores.

<br>

Home page
<br>

![Home](/static/images/readme-img/mobile-index.png)


## Manual Testing

I conducted manual testing to ensure the effectiveness and usability of the FootBrazil website.

#### Homepage

| Testing  | Action | Expected Result | Grade |  
| - | - | - | - |
| Visitor can view home page | Access the main page of the website | Being able to open and browse without errors | PASS |
| Visitor can click on all button in homepage | When hover over the button, the button darkens a little| Buttons works without errors | PASS |
| Homepage displays posts | Navigation from background image to posts | Posts shows without errors | PASS |

#### About page

| Testing  | Action | Expected Result | Grade |  
| - | - | - | - |
| Visitor can view about page | Access to the about page after clicked on button "About" from navbar | Being able read text without errors | PASS |

#### Registration 

| Testing  | Action | Expected Result | Grade |  
| - | - | - | - |
| User signup page | Click on button "Register" from navbar | Visitor is directed to the signup page | PASS |
| Fill in the registration form with valid and unique user information | Click on button "Sign up" | Success full registration | PASS |

#### Footer

| Testing  | Action | Expected Result | Grade |  
| - | - | - | - |
| Social media link opens with new tab | Click on link "Facebook, Twitter, Instagram or Youtube" from footer | Visitor is directed to the new window for selected socialmedia | PASS |

#### Navbar

| Testing  | Action | Expected Outcome | Grade |  
| - | - | - | - |
| Navbars link testing | Each link will be working correctly | The user can open any link to view the web page | PASS |

#### Admin panel

| Testing  | Action | Expected Outcome | Grade |  
| - | - | - | - |
| Superusers features | Superuser will be able to create, delete and update | Superuser can create, delete and update content | PASS |

## Validator Testing 

- HTML
  - No errors were returned when passing through the official [W3C validator](https://validator.w3.org/)

- CSS
  - No errors were found when passing through the official [(Jigsaw) validator](http://jigsaw.w3.org/css-validator/)

- JAVASCRIPT
  - No errors were returned when passing through the official [JSHint validator](https://jshint.com/)

- PYTHON
  - No errors were returned when passing through the PEP8 Validator 

- Admin.py
  ![admin.py](/static/images/readme-img/admin-py.png)

- Models.py
  ![models.py](/static/images/readme-img/models-py.png)

- Views.py
  ![views.py](/static/images/readme-img/views-py.png)

- Urls.py
  ![urls.py](/static/images/readme-img/urls-py.png)

- Forms.py
  ![forms.py](/static/images/readme-img/forms-py.png)


## Bugs

### Unfixed Bugs
