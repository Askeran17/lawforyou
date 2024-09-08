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

#### Detailed product page

| Testing  | Action | Expected Result | Grade |  
| - | - | - | - |
| Visitor can view detailed product page | Access to the product page after either clicked on button "buy" from homepage featured products or after clicked on button "services" and there choose the product | Being able read text without errors | PASS |
| Registered user can leave a review and add rating under product | Log in and leave a review | Leave a review without errors | PASS |
| Reviews appears directly | Leave a review on product | Reviews appears without errors | PASS |
| Rating appears directly | Leave a rating on product | Rating appears without errors | PASS |

#### Add product page

| Testing  | Action | Expected Result | Grade |  
| - | - | - | - |
| Admin can add product from website itself | Access to the add product page after clicked on link "Product management" from navbar | Being able to fill out the fields, send it and product will be added directly | PASS |
| Image uploading from add product page | Opportunity to have a field to upload image to product | Image appears without errors | PASS |

#### Edit product page

| Testing  | Action | Expected Result | Grade |  
| - | - | - | - |
| Admin can edit product from website itself | Access to the edit product page after clicked on button "edit" from product | Being able to update the fields, send it and product will be updatet directly | PASS |

#### Delete product

| Testing  | Action | Expected Result | Grade |  
| - | - | - | - |
| Admin can delete product from website itself | Access to the delete product after clicked on button "delete" from product page | Being able to delete product directly | PASS |

#### Make an appointment

| Testing  | Action | Expected Result | Grade |  
| - | - | - | - |
| Registred and unregistred users can book an appointment | Users must fill in form to book an appointment | Being able to fill out the fields, send it and appointment request will be recieved directly | PASS |

#### Manage appointment

| Testing  | Action | Expected Result | Grade |  
| - | - | - | - |
| Admin can accept appointment from website itself | Admin must set date to appointment on manage appointment page | Being able to choose the date and accept appointment, and user will receive an confirmation mail directly | PASS |

#### Delete appointment

| Testing  | Action | Expected Result | Grade |  
| - | - | - | - |
| Admin can delete appointment from website itself | Access to the delete appointment after clicked on button "delete" from manage appointment page | Being able to delete appointment directly | PASS |

#### Forecast

| Testing  | Action | Expected Result | Grade |  
| - | - | - | - |
| Registred and unregistred users can do an forecast | Users must click on start button to start forecast and answer on questions | Being able to answer questions and get an result based on answers directly | PASS |

#### Make an request

| Testing  | Action | Expected Result | Grade |  
| - | - | - | - |
| Registred and unregistred users can send an request | Users must fill in form to book an appointment | Being able to fill out the fields, send it and request will be recieved directly | PASS |

#### About page

| Testing  | Action | Expected Result | Grade |  
| - | - | - | - |
| Visitor can view about page | Access to the about page after clicked on button "About" from navbar | Being able read text without errors | PASS |

#### Registration 

| Testing  | Action | Expected Result | Grade |  
| - | - | - | - |
| User signup page | Click on link "Register" from navbar | Visitor is directed to the signup page | PASS |
| Fill in the registration form with valid and unique user information | Click on button "Sign up" | Success full registration | PASS |

#### Subscribe on newsletter

| Testing  | Action | Expected Result | Grade |  
| - | - | - | - |
| User can subscribe on newsletter | Type email in field to subscribe | Being able to subscribe without errors | PASS |

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
  - No errors for all scripts were returned when passing through the official [JSHint validator](https://jshint.com/)
  - Checkout.js - This script is taken from the Stripe documentation and I decided to ignore these warnings as there was no solution found to fix it.

  ![checkout.js](/static/images/testing-img/checkout-js.png)

  - Countryfield.js - These warnings also do not affect my code, so I ignored them as well. I tried to solve them, but did not find a good solution for them.

  ![countryfield.js](/static/images/testing-img/countryfield-js.png)

  - Reviews.js - the same here, these warnings do not affect my code, so I also ignored them.

  ![reviews.js](/static/images/testing-img/reviews-js.png)

  - Forecast.js - No warnings for this script.

  ![forecast.js](/static/images/testing-img/forecast-js.png)

  - 

- PYTHON
  - No errors were returned when passing through the PEP8 Validator 

### Home app
- Views.py
  ![views.py](/static/images/testing-img/home-views-py.png)

- Urls.py
  ![urls.py](/static/images/testing-img/home-urls-py.png)

### Profiles app
- Forms.py
  ![forms.py](/static/images/testing-img/profiles-forms-py.png)

- Models.py
  ![models.py](/static/images/testing-img/profiles-models-py.png)

- Views.py
  ![views.py](/static/images/testing-img/profiles-views-py.png)

- Urls.py
  ![urls.py](/static/images/testing-img/profiles-urls-py.png)




## Bugs

### Unfixed Bugs
