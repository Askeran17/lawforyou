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

![Home](/static/images/testing-img/lighthouse-desktop.png)


### Mobile Results

The site showed good scores.

<br>

Home page
<br>

![Home](/static/images/testing-img/lighthouse-mobile.png)


## Manual Testing

I conducted manual testing to ensure the effectiveness and usability of the LawForYou website.

#### Homepage

| Testing  | Action | Expected Result | Grade |  
| - | - | - | - |
| Visitor can view home page | Access the main page of the website | Being able to open and browse without errors | PASS |
| Visitor can click on all button in homepage | Navigation on buttons | Buttons works without errors | PASS |
| Homepage displays featured products posts | Navigation to featured products | Featured products shows without errors | PASS |

#### Profile page

| Testing | Action | Expected Result | Grade |  
| - | - | - | - |
| User can view profile page | Access to the profile page after clicked on link "My account" and choose "My profile" link | Being able view profile page without errors | PASS |
| User can update information about himself | User should navigate to form field and edit information | All fields works correctly and after updated information about himself he will get an success message about it | PASS |


#### Detailed product page

| Testing | Action | Expected Result | Grade |  
| - | - | - | - |
| Visitor can view detailed product page | Access to the product page after either clicked on button "buy" from homepage featured products or after clicked on button "services" and there choose the product | Being able read text without errors | PASS |
| User can add to bag product | User should choose quantity and click on button "add to bag" | All butttons works correctly and if user choosed quantity and clicked on button "add to bag" he get an success message about it and then can go to page "checkout" | PASS |
| Quantity can´t be 0 | User must type at least 1 number | At least 1 number must be set for quantity, otherwise it is impossible to add to bag | PASS |


#### Add review and rating on product page

| Testing  | Action | Expected Result | Grade |  
| - | - | - | - |
| Registered user can leave a review and add rating under product | Log in and leave a review | Leave a review without errors | PASS |
| Reviews appears directly | Leave a review on product | Reviews appears without errors | PASS |
| Rating appears directly | Leave a rating on product | Rating appears without errors | PASS |
| Comment field for review can´t be empty | User must type characters and set rating | If this field is left empty and rating was´nt set, then when sending the form, user will receive a notification that the form is not valid and therefore cannot be sent | PASS |
| If comment field for review is filled but rating is empty? | User must type characters and set rating | If comment field is filled out but rating still empty, then when sending the form, user will receive a notification that the form is not valid and therefore cannot be sent | PASS |
| When review and rating are filled and set | User type characters and set rating | When comment field is filled out and rating has been set, then when sending the form, user will see directly under heading "Reviews" own review with rating he set | PASS |

#### Shopping Bag page

| Testing | Action | Expected Result | Grade |  
| - | - | - | - |
| User can view bag shopping page | Access to the shopping bag page after either clicked on button from message notification "go to secure page" from product detail page or after clicked on icon "bag" from navbar | Being able view shopping bag page without errors | PASS |
| User can uppdate his bag | User should navigate to quantity and click on button "+" or "-" | All butttons works correctly and if user choosed "+" or "-" and clicked on button "update" he get an success message about it and then can go to page "checkout" | PASS |
| User can remove product from his bag | User should click on button "remove" which is under "quantity" | All butttons works correctly and if user clicked on button "remove" he get an success message about it and then can go back to page "services" by clicking button "keep shopping" | PASS |

#### Checkout page

| Testing | Action | Expected Result | Grade |  
| - | - | - | - |
| User can view checkout page | Access to the checkout page after clicked on button "secure checkout" from shopping bag page | Being able view checkout page without errors | PASS |
| User can type his personal information | User should filled the form to do an order | All fields works correctly | PASS |
| User can adjust his bag, going back to shopping bag page | Access to the shopping bag page after clicked on button "adjust bag" from checkpout page | Adjust button works correctly, being able view shopping bag page without errors | PASS |
| Invalid form if user leaves fields with blank spaces | User doesnt filled out fields | If user doesnt filled out fields, and filled out only e-mail, country, and card number - (which is special required fieds), it will get an 500 error | PASS |
| User filled out fields to buy product | User filled out all fields | When user filled out all fields correctly inclusive e-mail, country, and card number - (which is special required fieds), he will get an success message and confirmation mail to his e-mail address | PASS |


#### Add product page

| Testing  | Action | Expected Result | Grade |  
| - | - | - | - |
| Admin can add product from website itself | Access to the add product page after clicked on link "Product management" from navbar | Being able to fill out the fields, send it and product will be added directly | PASS |
| Item field can´t be empty | Admin must set at least 1 number | Only numbers accept due to is integerfield, otherwise it is impossible to submit the form| PASS |
| Name field can´t be empty | Admin must type characters | If this field is left empty, then when sending the form, admin will receive a notification that the form is not valid and therefore cannot be sent | PASS |
| Url field can´t be empty | Admin must type valid url without spaces which include alphanumeric + special characters pattern| Admin must type correct validate url, otherwise it is impossible to submit the form | PASS |
| Image uploading from add product page | Opportunity to have a field to upload image to product | Image appears without errors | PASS |
| Description field can´t be empty | Admin must type characters | If this field is left empty, then when sending the form, admin will receive a notification that the form is not valid and therefore cannot be sent | PASS |
| Summary field from add product page | Opportunity to have a field to write summary to product | Summary field appears without errors | PASS |
| Price field can´t be empty | Admin must set at least 1 number | Only numbers accept due to is decimalfield, otherwise it is impossible to submit the form| PASS |

#### Edit product page

| Testing  | Action | Expected Result | Grade |  
| - | - | - | - |
| Admin can edit product from website itself | Access to the edit product page after clicked on button "edit" from product | Being able to update the fields, send it and product will be updatet directly | PASS |
| Edit Item field which can´t be empty | Admin must set at least 1 number | When admin edit this field, only numbers accept due to is integerfield, otherwise it is impossible to submit the form| PASS |
| Edit Name which field can´t be empty | Admin must type characters | When admin edit this field and left this empty, then when sending the form, admin will receive a notification that the form is not valid and therefore cannot be sent | PASS |
| Edit Url field which can´t be empty | Admin must type valid url without spaces which include alphanumeric + special characters pattern| When admin edit this field, it must type correct validate url, otherwise it is impossible to submit the form | PASS |
| Change Image from edit product page | Opportunity to change image for product | Image updates without errors | PASS |
| Delete Image from edit product page | Opportunity to delete image for product | Image deletes without errors | PASS |
| Edit Description field which can´t be empty | Admin must type characters | When admin edit this field and left this empty this, then when sending the form, admin will receive a notification that the form is not valid and therefore cannot be sent | PASS |
| Summary field from edit product page | Opportunity to edit this field for product | When admin edit this field it appears without errors | PASS |
| Edit Price field can´t be empty | Admin must set at least 1 number | When admin edit this field, only numbers accept due to is decimalfield, otherwise it is impossible to submit the form | PASS |

#### Delete product

| Testing  | Action | Expected Result | Grade |  
| - | - | - | - |
| Admin can delete product from website itself | Access to the delete product after clicked on button "delete" from product page | Being able to delete product directly | PASS |

#### Make an appointment

| Testing  | Action | Expected Result | Grade |  
| - | - | - | - |
| Registred and unregistred users can book an appointment | Users must fill in form to book an appointment | Being able to fill out the fields, send it and appointment request will be recieved directly | PASS |
| First Name and Last Name fields can´t be empty | User must type at least 1 letters | Only letter without spaces/numbers/etc/ accept, otherwise it is impossible to submit the form| PASS |
| E-mail field can´t be empty | User must type e-mail which include @ symbol | User must type correct validate e-mail which include @ symbol, otherwise it is impossible to submit the form | PASS |
| Phone Number field can´t be empty | User must type at least 1 number | Only numbers and +/- accept, without spaces/letter/etc/, otherwise it is impossible to submit the form| PASS |
| Request field can´t be empty | User must type at least 5 character | If field is filled out, form will be sent, otherwise it is impossible to submit the form and user will get an error alert| PASS |

#### Manage appointment

| Testing  | Action | Expected Result | Grade |  
| - | - | - | - |
| Admin can accept appointment from website itself | Admin must set date to appointment on manage appointment page | Being able to choose the date and accept appointment, and user will receive an confirmation mail directly | PASS |
| Admin must have max 6 appointments per page | Appointments appears after customer send request | If it appears more than 6 appointments, it appears button "next" and than it goes to the next page | PASS |
| Received appointment can´t be accept without setting the date | Admin must choose the date to meeting with customer| If field for the date is accepted by admin, appointment confirmation will be sent to customer, and admin will get success message, otherwise it is impossible to acccept the appointment and admin will get a title-notification to set the date| PASS |
| Appointments should comming in order by sent date and id| Admin receive in sequence in order all appointments | Manage appointment page must show to admin all of appointments by sent date from customer and id| PASS |


#### Delete appointment

| Testing  | Action | Expected Result | Grade |  
| - | - | - | - |
| Admin can delete appointment from frontend, without go to admin panel | In appointment card there is a button "delete" which must clicked to go to delete page | If admin clicked on the button "delete" it will go to delete appoointment page| PASS |
| Delete appointment | Admin must confirm to delete page from delete appointment page | When admin confirm to remove appointment, it delete directly and admin goes back to manage appointment page| PASS |

#### Forecast

| Testing  | Action | Expected Result | Grade |  
| - | - | - | - |
| Registred and unregistred users can do an forecast | Users must click on start button to start forecast and answer on questions | Being able to answer questions and get an result based on answers directly | PASS |
| Start Button | Directs the user to the forecast display, clicked on button | Forecast opens to area | Pass |
| Answer Button | After selecting an answer option, pressing the answer button should move the participant to the next question | When the visitor has selected an answer and clicked on the button, he moves on to the next question | Pass |
| Try again Button | Takes the user to the beginning of the start screen forecast | Taken to the beginning of the start screen forecast there user need to click on start button | Pass |
| Displayed message | The final message with the result should be shown | If users score is good, it will congratulated and score is displayed. If result is ok or bad, then it also receive a message which displays result. | Pass |

#### Make an request

| Testing  | Action | Expected Result | Grade |  
| - | - | - | - |
| Registred and unregistred users can send an request | Users must fill in form to book an appointment | Being able to fill out the fields, send it and request will be recieved directly | PASS |
| Name field can´t be empty | User must type at least 1 letters | Only letter without spaces/numbers/etc/ accept, otherwise it is impossible to submit the form| PASS |
| E-mail field can´t be empty | User must type e-mail which include @ symbol | User must type correct validate e-mail which include @ symbol, otherwise it is impossible to submit the form | PASS |
| Phone Number field can´t be empty | User must type characters | If this field is left empty, then when sending the form, user will receive a notification that the form is not valid and therefore cannot be sent | PASS |
| Subject field can´t be empty | User must type at least 1 letters | Only letter without spaces/numbers/etc/ accept, otherwise it is impossible to submit the form| PASS |
| Message field can´t be empty | User must type characters | If this field is left empty, then when sending the form, user will receive a notification that the form is not valid and therefore cannot be sent | PASS |

#### About page

| Testing  | Action | Expected Result | Grade |  
| - | - | - | - |
| Visitor can view about page | Access to the about page after clicked on button "About" from navbar | Being able read text without errors | PASS |

#### FAQ page

| Testing  | Action | Expected Result | Grade |  
| - | - | - | - |
| Visitor can view FAQ page | Access to the FAQ page after clicked on link "FAQ" from footer | Being able read text without errors | PASS |

#### Privacy Policy page

| Testing  | Action | Expected Result | Grade |  
| - | - | - | - |
| Visitor can view Privacy Policy page from new window | Access to the Privacy Policy page after clicked on link "Privacy And Policy" from footer | Page opens in new window, user being able read text without errors | PASS |

#### Registration 

| Testing  | Action | Expected Result | Grade |  
| - | - | - | - |
| User sign-up page Step 1 | Click on link "My account"-"Register" from navbar | User is directed to the signup page | PASS |
| User sign-up page Step 2 | Fill in the registration form with valid and unique user information, click on button "Sign up" | Successfull registration | PASS |

#### Sign in

| Testing  | Action | Expected Result | Grade |  
| - | - | - | - |
| User sign-in page Step 1| Click on link "My account"-"Login" from navbar | User is directed to the sign-in page | PASS |
| User sign-in page Step 2 | Fill in the form with valid and unique user information, click on button "Sign in" | Successfull sign in | PASS |

#### Reset password

| Testing  | Action | Expected Result | Grade |  
| - | - | - | - |
| User reset password Step 1 | Click on link "My account"-"Login" from navbar, and click on "Forgot Password" | User is directed to the password reset page | PASS |
| User reset password Step 2 | Fill in the form with valid e-mail, click on button "Reset My Password" | Successfull reset, mail confirmation on users-email | PASS |

#### Subscribe on newsletter

| Testing  | Action | Expected Result | Grade |  
| - | - | - | - |
| User can subscribe on newsletter | Type email in field to subscribe | Being able to subscribe without errors | PASS |

#### Footer

| Testing  | Action | Expected Result | Grade |  
| - | - | - | - |
| Social media link opens with new tab | Click on link "Facebook, Instagram, Twitter or Youtube" from footer | Visitor is directed to the new window for selected socialmedia | PASS |
| Privacy and policy link opens with new tab | Click on link "Privacy and policy" from footer | Visitor is directed to the new window | PASS |

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
    ![HTML validation](/static/images/testing-img/html-validation.png)

- CSS
  - No errors were found when passing through the official [(Jigsaw) validator](http://jigsaw.w3.org/css-validator/)
    ![CSS validation](/static/images/testing-img/css-validation.png)

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

### Checkout app
- Admin.py
  ![admin.py](/static/images/testing-img/checkout-admin-py.png)

- Forms.py
  ![forms.py](/static/images/testing-img/checkout-forms-py.png)

- Models.py
  ![models.py](/static/images/testing-img/checkout-models-py.png)

- Views.py
  ![views.py](/static/images/testing-img/checkout-views-py.png)

- Urls.py
  ![urls.py](/static/images/testing-img/checkout-urls-py.png)

- Signals.py
  ![signals.py](/static/images/testing-img/checkout-signals-py.png)

- Webhooks.py
  ![webhooks.py](/static/images/testing-img/checkout-webhooks-py.png)

- Webhook handler.py
  ![webhook-handler.py](/static/images/testing-img/checkout-webhook-handler-py.png)

### Bag app
- Views.py
  ![views.py](/static/images/testing-img/bag-views-py.png)

- Urls.py
  ![urls.py](/static/images/testing-img/bag-urls-py.png)

- Contexts.py
  ![contexts.py](/static/images/testing-img/bag-contexts-py.png)

### Appointment app
- Context processors.py
  ![context-processors.py](/static/images/testing-img/appointment-context-processors-py.png)

- Models.py
  ![models.py](/static/images/testing-img/appointment-models-py.png)

- Views.py
  ![views.py](/static/images/testing-img/appointment-views-py.png)

- Urls.py
  ![urls.py](/static/images/testing-img/appointment-urls-py.png)

### Services app
- Forms.py
  ![forms.py](/static/images/testing-img/services-forms-py.png)

- Models.py
  ![models.py](/static/images/testing-img/services-models-py.png)

- Widgets.py
  ![widgets.py](/static/images/testing-img/services-widgets-py.png)

- Views.py
  ![views.py](/static/images/testing-img/services-views-py.png)

- Urls.py
  ![urls.py](/static/images/testing-img/services-urls-py.png)

### Forecast app
- Forms.py
  ![forms.py](/static/images/testing-img/forecast-forms-py.png)

- Models.py
  ![models.py](/static/images/testing-img/forecast-models-py.png)

- Views.py
  ![views.py](/static/images/testing-img/forecast-views-py.png)

- Urls.py
  ![urls.py](/static/images/testing-img/forecast-urls-py.png)

### FAQ app
- Forms.py
  ![forms.py](/static/images/testing-img/faq-forms-py.png)

- Models.py
  ![models.py](/static/images/testing-img/faq-models-py.png)

- Views.py
  ![views.py](/static/images/testing-img/faq-views-py.png)

- Urls.py
  ![urls.py](/static/images/testing-img/faq-urls-py.png)


## Bugs

At the beginning of my project I tried to test which storage platform is better to work on Cloudinary or Amazon. At first I used Cloudinary, but then I decided to try Amazon. Using Amazon for several days I received messages from them that my free limit had already reached 85%, and then I realized that perhaps this was due to the fact that I deployed the site many times. For this reason I returned back to Cloudinary, configured it correctly and the site began to work much faster and I did not receive any messages from Cloudinary like from Amazon. I think that Cloudinary platform is much better than Amazon.

### Unfixed Bugs

The disadvantage of Cloudinary was that when I added images, special characters from the Cloudinary were automaticaly added to the name of the images, I consider this a downside for SEO, but I did not find the right guide to how to fix this bug. 
