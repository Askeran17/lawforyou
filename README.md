<h1 align="center"> LawForYou - your guidehelp in law</h1>

![The LawForYou on a variety of screen sizes](/static/images/readme-img/adaptability-size.png)

### Live Site

- Go to live site - [LawForYou](https://lawforyou-4899488e19b1.herokuapp.com/)

### Repository

- Go to the repository for this project - [Repository-LawForYou](https://github.com/Askeran17/lawforyou.git)

---

## [Contents](#contents)

- [Overview](#overview)
- [User Experience (UX)](#user-experience-ux)
  - [Project Goal](#project-goal)
  - [User Stories](#user-stories)
  - [Agile](#agile)
  - [Design](#design)
    - [Wireframes](#wireframes)
    - [Database](#database)
- [Features](#features)
    - [Existing Features](#existing-features)
- [Marketing](#marketing)
    - [Facebook Business](#facebook-business)
    - [SEO Optimization](#seo-optimization)
- [Technologies Used](#technologies-used)
  - [Languages Used](#languages-used)
  - [Frameworks, Libraries & Programs Used](#frameworks)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)
  - [Content](#content)
  - [Media](#media)

## Overview

This site is dedicated to legal assistance to people who need to protect their rights. On this site you will find a variety of legal services, thanks to which the visitor has a large choice of options for solving their problems. For example, the user can order a free consultation with a lawyer, where the user and the lawyer will analyze the problem together, the user is also given the opportunity to make a brief forecast of his case, what is the probability of a positive or negative decision.

The scope of paid services includes, for example, writing a contract, appealing a decision in government agencies and court, a notary seal, filing a petition, etc. Under each service, the user can leave a review and evaluate the offered service. The user also has the opportunity to follow the company's news via Facebook, by subscribing to the company's Facebook page, as well as subscribing to the mailing list.


## User Experience

### Project Goal

The purpose of the site is to provide visitors with the opportunity to easily obtain legal assistance online using web development.


### User Stories

### Agile

The project used a Agile methodology that tracked the process of creating the project. An issue was created for each user story.

Visitors can read posts and view video in posts but not to add a comment under this. Registred users can add a comment under posts. Administrator of site can adding, updating & deleting comments. A project Kanban board was used to track progress, with user stories moved between 'ToDo', 'In Progress' and 'Done' columns as appropriate.

Here is link to Agile [User Stories](https://github.com/users/Askeran17/projects/9).

### Design

- The design of the site should be consistent with the theme, and since the theme of the site is the provision of legal services, the design of the site should be focused on a combination of strict colors, so jurisprudence, in my opinion, is visually felt well when there are strict tones diluted with a little light, for example, blue.

#### Colors

- The color scheme predominantly consists of a variety of greys, blacks, whites and blues. The use of gray and white creates a background tone, and the blue is refreshing and correlates with the color of hope, which in my opinion corresponds to the light-soft color that is blue, which corresponds to the theme of the site. The red color enlivens the dark colors, and also characterizes some details in the website. The black color clearly marks the bottom panel of the site.

![image](/static/images/readme-img/color-palette.png)

#### Fonts




### Wireframes
I used program "Balsamiq Wireframes" to draw a page layout.

Home page
<br>

![image](/static/images/readme-img/wireframe-home.png)

Services page
<br>

![image](/static/images/readme-img/wireframe-services.png)

Forecast page
<br>

![image](/static/images/readme-img/wireframe-forecast.png)

About page
<br>

![image](/static/images/readme-img/wireframe-about.png)

Manage appointment page
<br>

![image](/static/images/readme-img/wireframe-manage-appointment.png)

Product detail page
<br>

![image](/static/images/readme-img/wireframe-product-detail-page.png)

My profile page
<br>

![image](/static/images/readme-img/wireframe-profile.png)

### Database
The project uses the relational database PostgreSQL to store the data. I used PostgreSQL because it is considered one of the recommended databases on the Heroku platform.


### Models in "Services" app

**Product model:**

The model consists of the following parts:

- [x] **item**: models.CharField(max_length=254, null=True, blank=True) - Indicates the item of the product with 254 characters length
- [x] **name**: models.CharField(max_length=254) - Indicates the name of the product with 254 characters length
- [x] **url**: models.SlugField(max_length=300, unique=True) - creates a 300-character address bar path based on the product name
- [x] **image**: models.ImageField(null=True, blank=True) - fiel for upload images
- [x] **description**: models.TextField() - detailed description of the product
- [x] **summary**: models.TextField(blank=True) - short description of the product
- [x] **price**: models.DecimalField(max_digits=6, decimal_places=2) - price of the product

**Review model:**

The model consists of the following parts:

- [x] **product**: models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="reviews") - indicates that a review will be attached to the product
- [x] **user**: models.ForeignKey(
        User, on_delete=models.CASCADE) - indicates who is the author of the review
- [x] **comment**: models.TextField(max_length=500) - field for writing a review with a maximum length of 500 characters
- [x] **rating**: models.IntegerField(choices=RATINGS, null=True, blank=True) - the ability to rate a product by placing a rating along with a review
- [x] **created_at**: models.DateTimeField(auto_now_add=True) - review publication date


### Model in "Appointment" app

**Appointment model:**

The model consists of the following parts:

- [x] **first_name**: models.CharField(max_length=50) - Indicates the first name of a person with 50 characters length
- [x] **last_name**: models.CharField(max_length=50) - Indicates the last name of a person with 50 characters length
- [x] **email**: models.CharField(max_length=50) - Indicates the email of a person with 50 characters length
- [x] **phone**: models.CharField(max_length=50) - Indicates the phone number of a person with 50 characters length
- [x] **request**: models.TextField(blank=True) - Field for request from customer
- [x] **sent_date**: models.DateField(auto_now_add=True) - Indicates the date when request was send from a customer
- [x] **accepted**: models.BooleanField(default=False) - Field if date of appointment will accepted
- [x] **appointment_date**: models.DateField(null=True, blank=True) - Field for appointment date


### Model in "Forecast" app

**RequestHelp model:**

The model consists of the following parts:

- [x] **name**: models.CharField(max_length=100) - Indicates the first name of a person with 100 characters length
- [x] **email**: models.EmailField() - Indicates the email of a person
- [x] **phone**: models.CharField(max_length=20) - Indicates the phone number of a person with 20 characters length
- [x] **subject**: models.CharField(max_length=150) - The field where a person writes the name of his request with 150 characters length
- [x] **message**: models.TextField(blank=True) - Field for request there customer describe his resquest


### Model in "Profiles" app

**UserProfile model:**

The model consists of the following parts:

- [x] **user**: models.OneToOneField(User, on_delete=models.CASCADE) - Indicates on user and if profile will be deleted, all information will be deleted also
- [x] **default_phone_number**: models.CharField(max_length=20, null=True, blank=True) - Indicates the phone number of a user with 20 characters
- [x] **default_country**: CountryField(blank_label='Country *', null=True, blank=True) - Indicates of the user country there user will choose
- [x] **default_postcode**: models.CharField(max_length=20, null=True, blank=True) - Field for postcode with 20 characters
- [x] **default_town_or_city**: models.CharField(max_length=40, null=True, blank=True) - Field for town or city with 40 characters
- [x] **default_street_address1**: models.CharField(max_length=80, null=True, blank=True) - Field for users street address with 80 characters
- [x] **default_street_address2**: models.CharField(max_length=80, null=True, blank=True) - Field for another users street address with 80 characters
- [x] **default_county**: models.CharField(max_length=80, null=True, blank=True) - Field for users county with 80 characters


### Model in "Checkout" app

**Order model:**

The model consists of the following parts:

- [x] **order_number**: models.CharField(max_length=32, null=False, editable=False) - Indicates the order number with 32 characters
- [x] **user_profile**: models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders') - indicates user profile
- [x] **full_name**: models.CharField(max_length=50, null=False, blank=False) - Indicates the full name of a person with 50 characters length
- [x] **email**: models.EmailField(max_length=254, null=False, blank=False) - Indicates the email of a person
- [x] **phone_number**: models.CharField(max_length=20, null=False, blank=False) - Indicates the phone number of a user with 20 characters
- [x] **country**: CountryField(blank_label='Country *', null=True, blank=True) - Indicates of the user country there user will choose
- [x] **postcode**: models.CharField(max_length=20, null=True, blank=True) - Field for postcode with 20 characters
- [x] **town_or_city**: models.CharField(max_length=40, null=True, blank=True) - Field for town or city with 40 characters
- [x] **street_address1**: models.CharField(max_length=80, null=True, blank=True) - Field for users street address with 80 characters
- [x] **street_address2**: models.CharField(max_length=80, null=True, blank=True) - Field for another users street address with 80 characters
- [x] **county**: models.CharField(max_length=80, null=True, blank=True) - Field for users county with 80 characters
- [x] **date**: models.DateTimeField(auto_now_add=True) - Field for date
- [x] **order_total**: models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0) - Field for order total
- [x] **grand_total**: models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0) - Field for grand total order
- [x] **original_bag**: models.TextField(null=False, blank=False, default='') - Field for original bag
- [x] **stripe_pid**: models.CharField(max_length=254, null=False, blank=False, default='') - Field for stripe pid, i.e for each order a key

**OrderLineItem model:**

The model consists of the following parts:

- [x] **order**: models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems') - Field for order
- [x] **product**: models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE) - Field for order product
- [x] **quantity**: models.IntegerField(null=False, blank=False, default=0) - Field for quantity
- [x] **lineitem_total**: models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False) - Field for item total price





## Features

### Existing Features

__Header__

- The header has an adaptive navigation bar on the right. There are six links there for registered/unregistered users: home, services, forecast, about, my account and bag. The visitor can easily navigate through these links thanks to the responsive bar. Also, in the mobile or medium screen extension version, there will be a “hamburger” icon on the right side of the adaptive panel, which means that the same links are hidden behind it. This is very convenient and allows you to take up less page space.

![Navbar Desktop](/static/images/readme-img/nav-menu-desktop-visitor.png)
![Navbar Mobile](/static/images/readme-img/nav-menu-mobile-visitor.png)


- For admin, the navbar will look like this:

![Navbar Admin](/static/images/readme-img/nav-menu-admin.png)

- On the left side of navbar there is a logo that can be clicked and it will return the visitor to the main page.

- When user is logged in, it appears message at the top:

![User logged in](/static/images/readme-img/message-sign-in.png)

- When user is logged out, it appears message at the top:

![User logged out](/static/images/readme-img/message-sign-out.png)


__Main content__

- On the main page, the user is given the opportunity at the top to immediately proceed to ordering a service - an appointment. To do this, click on the "Book an appointment" button located in the middle of the picture.
![Homepage](/static/images/readme-img/homepage.png)

- Below the picture is a description with keywords so that the site is well ranked and promoted in search engines.

![SEO Description](/static/images/readme-img/seo-description.png)

- Further below the text are recommended services, of which there are four. The user can choose any of them by clicking on the "Buy" button and will immediately go to the detailed product page.
![Homepage](/static/images/readme-img/.png)

__Services page__

- On the service page, several types of services are offered, 6 of them on each page. In total, the service page offers 8 services, namely: draw up a testament, a power of attorney, write a letter to an opponent, notarize any document, get help in filling out a application, help in dividing property, help in appealing a decision, and also the ability to draw up a contract.
![Services Page](/static/images/readme-img/.png)

__Product detail page__

- On the product page, any user, even unregistered, can buy a service. By specifying how many services he wants to order and then clicking the buy button, his service goes to the cart.
![Product Detail Page](/static/images/readme-img/.png)

- Registered users also have the ability to leave comments, edit them and delete them. Also, registered users can rate the service by placing their rating.
![Product Detail Page](/static/images/readme-img/.png)

- After the user has rated and left a rating, his review appears immediately.
![Product Detail Page](/static/images/readme-img/.png)

- The admin can edit the product, as well as delete it directly without going to the admin panel.
![Product Detail Page](/static/images/readme-img/.png)

__Shopping Bag page__

- On the shopping bag page, the user can delete the ordered product or, for example, increase its quantity.
The user can also return to shopping or continue placing the order.
![Shopping Bag Page](/static/images/readme-img/shopping-bag-page.png)

__Checkout page__

- On the checkout page, the user fills in the specified fields and makes a purchase by clicking the order button.
![Checkout Page](/static/images/readme-img/checkout-page.png)

- After the purchase, the user is taken to the order confirmation page, where the purchased service is described, and the user also receives a confirmation email to his email that the service has been purchased with a notification in the mail that the user will be contacted shortly.
![Checkout Success Page](/static/images/readme-img/checkout-success-page.png)

__Profile page__

- On the profile page, the user can see all of their orders, as well as their personal data.
![Profile Page](/static/images/readme-img/profile-page.png)

__Forecast page__

- By clicking on the Forecast button in the top panel, the user is taken to the forecast page.
![Forecast Button](/static/images/readme-img/forecast-button.png)

- On this page, the user is asked to take a short test of 5 questions, which will reveal the probability of a positive or negative decision regarding a case that is under consideration in one of the government agencies, such as the Migration Service, the Tax Service, the Social Insurance Service, and so on.
![Forecast Page](/static/images/readme-img/forecast-request-page.png)

- If, for example, the user receives a positive answer, then he can be calm and most likely does not need to contact lawyers.
![Forecast Question](/static/images/readme-img/forecast-question.png)
![Forecast Good Result](/static/images/readme-img/forecast-good-result.png)

- If the user receives an average or especially negative answer, then he is recommended to contact lawyers by filling out a request
![Forecast Bad Result](/static/images/readme-img/forecast-bad-result.png)

- Having filled in all the contact fields, the user sends it and the legal team receives this request, after which they will contact him as soon as possible
![Request Form](/static/images/readme-img/request-form-fill.png)
![Request Success Page](/static/images/readme-img/request-success-page.png)

__Appointment page__

On the Meeting page, you can order a meeting with a lawyer. To do this, the user needs to fill out the form and click the send button.
![Appointment Page](/static/images/readme-img/book-appointment.png)

__Manage Appointment page__

- The admin, in turn, will see each sent request directly from the frontend on the management page, without going to the admin panel, and can process the request, choosing a suitable date for the meeting.
![Manage-Appointment Page](/static/images/readme-img/manage-appointment.png)

- After the admin approves the request by specifying the date, the user will receive an email that the request has been approved and will be contacted shortly.
![Acceppt Appointment](/static/images/readme-img/accept-appointment.png)

- The admin can also delete the request directly without going to the admin panel.
![Delete Appointment Page](/static/images/readme-img/delete-appointment.png)

__About page__

- This page contains brief information about the company, as well as what the company does
![About Page](/static/images/readme-img/about-page.png)

__Footer__

- In the footer I have placed a link to Facebook, Instagram, Twitter and YouTube. The link opens in a separate tab and the visitor is taken to socialmedia he choose, while the site remains open. It is very comfortable. Then I add schedule of opening hours, contacts and oppotunity to subscribe. And at the bottom I placed copyright.

![Footer](/static/images/readme-img/footer.png)

__Error pages__

- If the user incorrectly specified the page path or clicked on a non-existent page, then he is taken to a 404 page. This page contains a link to return to the main page.

![404 Page](/static/images/readme-img/error-page-404.png)

- The similar pages I did for pages 403 and 500.


## Marketing

- For good promotion of products, and especially online services, the site that offers its services for this must be well SEO optimized. For this, all possible means were used to promote the legal services that the site offers, namely: a beautifully designed site design, which in turn entices the visitor to visit the site again and again, well-structured web pages, removal of unnecessary code, adaptability and the ability to use the site on all possible devices. Google AdWords was also used to find key queries for the site's subject matter.

- The site also offers to subscribe to the newsletter using Mail Chimp, which in turn will increase the flow of returning visitors and from the incoming visitors will become regular customers, receiving new and high-quality offers.

### Facebook Business

- Since social networks play a big role today, having the most popular social network Facebook will significantly increase the reach of the audience, among which there will be potential clients. The best marketing move is a well-promoted page on the social platform Facebook, where we can reach an audience not only in our region, but also beyond its borders, which will lead to the popularity of our site. Considering that our legal services operate online with the help of proper marketing, especially using Facebook, we can receive requests from clients from all over the world.
![Facebook Page](/static/images/readme-img/facebook-page.png)

## Technologies Used

I did all the work in GitPod platform.

### Languages Used

HTML, CSS, JavaScript, Python, Django

### Frameworks, Libraries & Programs Used

* [Django](https://pypi.org/project/Django/4.2.11/) - To start project in Python.

* [Bootstrap](https://getbootstrap.com/) - To create the front-end design.

* [GitHub](https://github.com/) - To save and store the files for the website.

* [GitPod](https://gitpod.io/) - To use as IDE to commit and push the project to GitHub.

* [Google Fonts](https://fonts.google.com/) - To import the fonts used on the website.

* [Google Developer Tools](https://developers.google.com/web/tools) - To troubleshoot and test features, solve issues with responsiveness and styling.

* [IloveImg](https://www.iloveimg.com/) - To resize images.

* [Convertio](https://convertio.co/) - To convert images to webp format.

* [Favicon.io](https://favicon.io/) - To create favicon.

* [Balsamiq](https://balsamiq.com/) - Used to create wireframes.

* [Am I Responsive?](http://ami.responsivedesign.is/) - To show the website image on a range of devices.

* [Emojipedia](https://emojipedia.org/) - Emoji for history timeline.

* [Coolors](https://coolors.co/) - Colours palette.

* [Stripe](https://stripe.com/) - To ability to accept payment.

## Testing

To view testing go here [TESTING.md](TESTING.md)

## Deployment

### How to deploy on Heroku

The project was deployed to Heroku in the following manner:

1. Firstly you need to sign up on the Heroku website.
2. There after choose new and "create New App", give the app a name, choose a region: Europe
3. Go to deploy, see Deployment Method and select GitHub.
4. At section "Deployment method", click "GitHub" and connect your account with Heroku.
4. To connect your Heroku app to your code in a Github repository, you need to enter the name of your repository and click on the "Search" button. After that click on button “Connect” when it appears.
5. Go to manual deploy, select the branch from which you want to build your application and click to "Deploy Branch".
6. You have to wait until the app is build. When it wiil be done it will appear an “App was successfully deployed” message and after that you will see a "View" button. When you click on this button you will see your app deployed.

### How to fork

To fork do do the following steps:

1. You have to log in/register on GitHub.
2. Go to the repository for this project [LawForYou](https://github.com/Askeran17/lawforyou).
3. Click the "Fork" button in the top right corner.

### How to clone

To clone do the following steps:

1. You have to log in/register on GitHub.
2. Go to the repository for this project [LawForYou](https://github.com/Askeran17/lawforyou).
3. To clone the repository using HTTPS, under "HTTPS", click to copy button. To clone the repository using an SSH key, including a certificate issued by your organization's SSH certificate authority, click SSH, then click to copy button. To clone a repository using GitHub CLI, click GitHub CLI, then click to copy button.
4. Open terminal, change the current working directory to the location where you want the cloned directory.
5. Type git clone, and then paste the URL you copied earlier. Press Enter to create your local clone.

## Credits

- I was inspired by the "Boutique Ado" project at the Code Institute. I watched YouTube tutorial about how to fix appointments opportunity for customers: (https://www.youtube.com/watch?v=3_3q_dE4_qs) 

- The icons was taken from [Font Awesome](https://fontawesome.com/)

### Content 

- All text content for the site was written by myself.

### Media

- The images in site I took from open source, i.e. google.