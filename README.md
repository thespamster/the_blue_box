
![](static/img/readme_img/amiresponsive.png)

# The Blue Box Shop

This is my final project for Code Institute's Full-stack Level 5 Diploma in web application development. It is a Django based full e-commerce solution allowing users to browse and purchase from the shop without creating an account or the option to create an account to store info such as delivery address and order history plus future access to 'coming soon' features.

Bootstrap5.3, jQuery3.7.1 plus custom code from myself powers a site dedicated to allowing users to buy Dr. WHo related merchandise. Running on the Heroku platform with ElephantSQL managing the database this site has a clean modern uncluttered look with a sophisticated search ability meaning that a user can quickly find the items that interest them the most.

## Table of Contents

1. [The Blue Box Shop](the-blue-box-shop)
2. [User Stories](#user-stories)
3. [Creator Stories](#)
4. [Social Account Login](#social-account-logins)
5. [Initial Setup of IDE and Github](#initial-setup-of-ide-and-github)
6. [The Build](#the-build)
7. [Testing](#testing)
8. [Problems, Bugs and Fixes](#problems-bugs-and-fixes)
9. [Future Developments](#future-developments)

## User Stories

There are are two main user stories. Firstly the site admin's story and secondly a visitor to the site's story. 

### The Admin Story

- The site admin needs access to the admin site
- The site admin needs full CRUD access to the main site. This means...
    - An ability to create new database entries for the site incl. users, categories, doctors and orders
    - An ability to access current database entries, incl. users, categories, doctors and orders
    - They can edit existing database entries either to correct an error or add new information
    - They also have an option to delete database entries or where applicable zero them
- As an admin their must be an ability to act as a site wide moderator
- Options to suspend or render inactive a user's account when deemed necessary
- When the message boards and fan art sections go live have an option to remove content deemed inappropriate

### The user story

This is broken down into two subsections...

- The casual visitor who does not want to create an account
- The visitor that wants more interaction with the site and creates an account to enable this

### The casual visitor

- Easily view the site's rules on the homepage
- Should have access to the shop and all the listings therein
- Should be able to use the search option to narrow down the products that are on screen
- Should have the option to create an account if they decide on more detailed interactions
- Should be able to add items to the cart
- Should be able to edit the contents of the cart by increasing or decreasing the quantity
- Should be able to delete items from the cart 
- There should be easily visible totals for the items in the cart, both number of items and total price plus the individual item price must also be displayed
- There should be an easy way back to the shop either via a dedicated button or through the navbar
- Any purchases should have a unique order reference and be confirmed via email for the users records

### The buyer

Must be able to do everything that the casual visitor can do plus:

- Create and maintain a profile that enables a login so that the user can access the site features easily and with a minimum of fuss
- Has stored delivery details to make the purchasing process quicker and simpler
- Will have access to dedicated messaging boards with the ability to create topics and post/rate responses. This feature is discussed in the section Future Developments
- Will have access to to a Fan Art section where user's own art can be uploaded to a gallery. This feature is discussed in the section Future Developments

## Social Account Logins

To enable a simpler signup process and encourage users to create an account a Google login option has been added to the login screen meaning that if a user has an existing Google account they can use this to create a profile for the shop.
As most phones are either Android or iOS most people will have already created either a Google account or Apple ID plus many more use Google services such as email and therefore also have an account. See the acknowledgements section for a link to the video from Tech with Tim which was a great help in getting this to work. The Apple login requires that you have a developer account with Apple at a cost of £79 per annum. This feature is discussed further in the section Future Developments. For the purposes of this project just the Google login is offered.

## Initial Setup of IDE and Github

To create a new repo:

first go to https://github.com/ and create a new repo, then in the terminal:

- echo "# test" >> README.md
- git init
- git add README.md
- git commit -m "first commit"
- git branch -M main
- git remote add origin https://github.com/thespamster/the_blue_box.git
- git push -u origin main

In VS Code in the terminal create a virtual environment:

- python -m venv venv -- creates virtual environment

- venv\Scripts\Activate.ps1 -- activates virtual environment

Add a  .gitignore file and MIT LICENSE, then create an assets folder and subfolders for CSS, Javascript and images with a separate subfolder for the README images.

With the virtual environment activated the Django project is created by first installing Django

- pip3 install django

Start the new project

- django-admin startproject blue_box

Test launch in Chrome from 127.0.0.1:8000

![Django Initial Screen](static/img/readme_img/django_initial_screen.png)

Run initial migrations

- python manage.py migrate

Create an Admin (superuser)

- python manage.py createsuperuser

Add username, email address and password

Install django-allauth for user authentication

- pip3 install django-allauth

Copy default allauth templates into custom templates folder for styling

- pip3 show django-allauth to get location of default templates
- cp -r < Filepath to allauth templates >* ./templates/allauth


Creating individual apps for the project is done using the following line of code in the terminal

- python manage.py startapp < name_of_app >

- pip3 install django-crispy-forms to style forms with Bootstrap.(installed at checkout stage)

[Back to top](#the-blue-box-shop)

## The Build

### base.html

The first page built was the base.html page that would be used as the template for all pages through to the checkout stage. The checkout and allauth pages are built using a different base.html template.
The header information, links to CDN's, navbar, off-canvas menu and footer were all built using Bootstrap5 and custom CSS. A element links and button elements were all given '#' addresses and would be updated throughout the project build. The search options in the off-canvas menu bar would be added to during the build. The footer required a small piece of custom CSS to fix it to the bottom of the content or screen whichever is lower. The colors used for the site are mostly TARDIS blue, pantone 2955c or rgba(0, 59, 111, 1.0). By varying the opacity a range of complimentary blues can be used giving the site a very consistent look.

The ability to search for items on the site is provided by a customised Bootstrap off-canvas menu. By clicking shop in the navbar a menu providing comprehensive search options slides in from left of screen and gives options to visit the shop and then search either from the search bar or by category, by Doctor, by price range or by ratings.

Later in the build additional HTML, CSS and Javascript were added to enable a 'back to top' button and a 'back to all items' button allowing for easier navigation of the site. Shop all was added to off-canvas menu bar.

### home app

A modular approach encouraged by Django's software provided the ideal environment for manual testing of each app before linking them together through base.html. The first app built was the home app.
After enabling the app through urls.py and adding to 'INSTALLED_APPS' in settings.py the home page at index.html was built. Using 'base.html' as a template the required Bootstrap and custom CSS was added. The development server was started and the homepage loaded. The addition of a 'featured' section on the homepage allowed for checking of the basic item look using Bootstrap cards and custom CSS for styling. 
This also confirmed that the static folder was being recognised and images displayed correctly.

### products app

With the homepage working the next app built allows the user to visit the shop and view the products.html page listed in price order from lowest to highest. Using base.html as a templates each item is rendered as a stylised Bootstrap card. The use of Bootstrap allows for a very responsive mobile first approach to the build and the final page scaled correctly across various different screen resolutions. See testing for more detail.

When clicked on the Bootstrap cards will link to the product_detail.html page where the item can be viewed in more detail. A full description rather than a truncated one is available along with other relevant information such as price, rating and category. The item or multiples can be added to the shopping cart and there is an option to return to the shop. Across the site there is the option to hover your mouse over an image and view it enlarged. Any user is notified through Toast message of adding an item or items to the shopping cart. The cart in the navbar has the total cost of the items currently in the cart displayed as a badge next to it. Again to make searching as easy as possible a series of tags are attached to each item and if clicked on provide a search based on the tag. This ensures that it is easy to find related items to the one currently being viewed.

### cart app

The cart was built from an initial idea of how it should look and built entirely from scratch. The idea was to have each item in the cart appear on its own line with a couple of shared features incl. a trashcan icon for deletion and the option to update the quantity of each item by selecting a value and clicking an update arrow icon. Also setting the quantity of an item to zero will delete the item from the cart. Rather than having confirmation requirements through either buttons or entirely separate pages simple toast messages confirm actions and if an item is deleted accidentally it is no problem to quickly navigate to it and re-add it to the cart. All of this provides a slick straight forward purchase process with a minimum of interruptions. When ready to complete the order a checkout option is available.

### checkout app

The checkout app is a modified version of the Boutique Ado's checkout app. The styling is specific to this site and is supplied mainly from base.html with further additional custom css. This maintains the look of the site throughout the whole purchase process and the Bootstrap5 library provides a responsive design across all popular screen sizes. This site only ships to UK addresses and any international shipping needs to prearranged via contact with the site using the supplied email address. In order to limit orders to UK only addresses the postcode field is required for the delivery address. This effectively prevents anyone without a UK address from completing a purchase. See the section Future Developments for further discussion.  When adding delivery address details it is possible to enter a different country. this is ignored by the Stripe test payment. It is editable by an admin and for the purposes of this project is deemed ok. However in a live situation I would personally use the Stripe provided complete checkout solution that can be easily configured to handle international shipping. See the section Future Developments for further discussion.

### profile app

The profile app is a modified version of the Boutique Ado profile app. With custom Bootstrap styling the app provides access to a default delivery address that is updatable and a order history that allows the account holder to view current/previous orders. See the Future Developments section for further discussion.

### database schema and erd

![](/static/img/readme_img/erd_sqllite3_editor.png)

The ERD is generated by the SQLite3 Editor extension installed in VS Code

Doctors:
    name = models.CharField(max_length=254)
    with a meta class verbose_name_plural = 'Doctors'

Orders:
    order_ref = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
    full_name = models.CharField(max_length=254, null=False, blank=False)
    email = models.EmailField(max_length=254, null=True, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=40, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=False, blank=False, default='')
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    original_cart = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')

OrderLineItem:
    order = models.ForeignKey(Order, null=False, blank=False,
        on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2,
        null=False, blank=False, editable=False)

Category
    name = models.CharField(max_length=254)
    display_name = models.CharField(max_length=254, null=True, blank=True)
    with a meta class verbose_name_plural = 'Categories'

Product:
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    ean = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=254, null=True, blank=True)
    tags = models.CharField(max_length=254)

UserProfile:
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_country = models.CharField(max_length=40, null=True, blank=True)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)




## Testing

### Manual Testing

#### Test 1: to check that allauth is working using email verification

In settings.py EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

- Expected   - That email verification would be asked for on 'admin' account
- Testing    - Went to accounts/login and entered 'admin' login details
- Result     - Email verification requested by allauth
- Fix        - No fix required. TEST PASSED

#### Test 2: Check that homepage loads correctly after creation of home app

In home app index.html added. text 'homepage link working' added to base.html. urls added for homepage.

- Expected      - That homepage would load with 'homepage link working' displayed onscreen
- Testing       - Started test server to load homepage 
- Result        - Index.html loaded with expected message
- Fix           - No fix required. TEST PASSED

#### Test 3: Check that all products page loads correctly after creation of products app

In products app products.html added. Text 'all products link working' added to base.html. Urls added for products page.

- Expected      - That all products page would load with 'all products page link working' displayed onscreen
- Testing       - Started test server to load homepage and navigated to products.html page
- Result        - Products page loaded with expected message
- Fix           - No fix required. TEST PASSED

#### Test 4: Check that individual product page loads correctly after creation of products app

In products app product_detail.html added. text 'product link working' added to base.html. urls added for product_detail page.

- Expected      - That  product page would load with 'product page link working' displayed onscreen
- Testing       - Started test server to load homepage, navigated to product_detail.html
- Result        - Product page loaded with expected message
- Fix           - No fix required. TEST PASSED

#### Test 5: to check that products are added successfully to the shopping cart

Added a temporary print cart function to cart views.py.

-  Expected  - That the output of the print function will show a dictionary consisting of product.id, quantity added
- Testing    - Started development server and selected an item. Then added item to cart
- Result     - Print output confirmed that item and quantity were added to the cart successfully
- Fix        - No fix required. TEST PASSED

#### Test 6: Google Lighthouse tests checking Performance, Accessibility, Best practices and SEO

These tests are run through Google's Dev Tools built into Chrome browser.

![](static/img/readme_img/glighthouse0524.png)

- Expected  - That the four areas tested return a green score ie. 90 or above
- Testing   - Tests run by Google Lighthouse in Chrome Dev Tools
- Result    - Accessibilty required addition of some missing alt attributes and SEO required a meta description of the site in the header
- Fix       - Added missing alt attributes and a meta description and then reran the tests resulting in the scores shown in the image. TEST PASSED

#### Test 7: W3C CSS validator

- Expected  - That no errors would be reported when run through the validator
- Testing   - Tested by direct input of CSS code in style.css
- Result    - One error found with font-style used instead of font-family
- Fix       - Corrected the reported error and reran validation. No errors reported. TEST PASSED

![](static/img/readme_img/w3c_css_validator0524.png)

#### Test 8: W3C HTML validator

- Expected  - That no errors would be reported when run through the validator
- Testing   - Tested by direct input of HTML code
- Result    - Two errors reported of button type rather than role. Trailing / errors with img and meta elements
- Fix       - Corrected the reported errors and reran validation. No errors reported. TEST PASSED

![](static/img/readme_img/w3c_html_validator0524.png)

#### Test 9: Google Login

- Expected  - That a user can use their Google account to create a profile on the Blue Box Shop
- Testing   - Used one of my Google accounts to create a profile
- Result    - Account created and checked via Admin panel. No errors during process
- Fix       - No fix required. TEST PASSED

#### Test 10: Custom CSS styling for allauth templates

- Expected  - That the allauth templates will be styled to better match the overall look and feel of the site
- Testing   - Started the development server and visited the login, signup, reset password, reset email and logout screens to check the styling
- Result    - Styling was present on all pages
- Fix       - No fix required. TEST PASSED (see below) 

#### Test 11: CORS testing

- Expected      - That installing the CORS-unblock Google Chrome Extension from the Chrome Webstore would allow CORS requests and fix the inability to load certain stripe elements through their CDN
- Testing       - [webbrowsertools](https://webbrowsertools.com/test-cors/) - This website tests for CORS allowed.
- Result        - With the extension active the Stripe CDN loaded all elements correctly and a successful payment was seen in the Stripe online portal.
- Fix           - The CORS Unblock extension works as expected and is the fix.

#### Test 12: That a non admin user cannot access the admin panel

- Expected      - That a non admin user cannot access the admin panel
- Testing       - Logged in as a non admin user and tried to access the admin page
- Result        - The admin login page loaded with a warning that this user doesn't have access to admin features
- Fix           - Test passed.

[Back to top](#the-blue-box-shop)

## Problems Bugs and Fixes

### Inconsistent Migrations Error:

On initial migrations the sites app was not added to the INSTALLED APPS in settings.py creating an 'inconsistent migration' error when added in later as it must be included in the first migrate.
This prevents any further migrations from happening. The solution is on a  Stackoverflow thread here:

- [Stackoverflow](https://stackoverflow.com/questions/42150499/how-do-i-delete-db-sqlite3-in-django-1-9-to-start-from-scratch) - credit to Mohammed Shareef C. for their solution 
    - delete the 'db.sqlite3' file
    - rm * /migrations/0 *.py (1 space after rm but remove the other 2 spaces)
    - python manage.py makemigrations
    - python manage.py migrate

### Django could not locate the static files folder

When setting up static files for CSS and JS Django could not find the static folder. The solution was to add this to the settings.py file 

- [Stackoverflow](https://stackoverflow.com/questions/12809416/django-static-files-404) - credit to Amar Kamthe for their solution
- STATIC_ROOT = ''
- STATIC_URL = '/static/'
- STATICFILES_DIRS = ('static',)

### Creation of Product Models

When creating the product models Pillow image handling software for Python was not installed.

- python -m pip install Pillow
- version 10.3.0

### Footer moving up the screen when there is little to no content displayed

This is a very common issue when coding a website. What is needed is a footer that stays either at the bottom of the screen or bottom of the
content whichever is the lowest.

- [Stackoverflow](https://stackoverflow.com/questions/643879/css-to-make-html-page-footer-stay-at-bottom-of-the-page-with-a-minimum-height-b)- credit to vsync for a brilliantly simple solution.

### Fontawesome icons flicker on page render

There is a brief flicker from the Fontawesome icons as a page is rendered. The solution involved replacing these icons with Bootstrap SVG icons removing the flicker completely.

### Cannot change color of svg icons added using img tag

SVG icons have their color coded into the icon making it less straightforward to change their color as the CSS color attribute doesn't have any effect. The filter CSS attribute can change the color. For the explanation as to how see the Stackoverflow question linked below.

- [Stackoverflow](https://stackoverflow.com/questions/22252472/how-can-i-change-the-color-of-an-svg-element/53336754#53336754) - credit to Manish Menaria for a simple solution.

### System crashed with an error about expecting a str but received a tuple during admin add product

Error was traced to MEDIA_ROOT = (os.path.join(BASE_DIR, 'media')) having a trailing comma ie. MEDIA_ROOT = (os.path.join(BASE_DIR, 'media'),) which meant a tuple was expected but not received resulting in the error and app crash. Removing the trailing comma resolved the issue.

### No 'Back to all products' button on individual item page

Missing button was traced to the query variable not being passed back through base.html via context in product view.py. Once added the back button displayed correctly.

### CORS error with Stripe CDN script

Having initially worked the script calling the Stripe CDN started giving a CORS (Cross Origin Resource Sharing) error and only partially loading the required resources. This meant that the checkout app would freeze as no payment request could be made. The issue is browser based with the browser refusing to accept a request with mismatched header information. The solution was to install a google extension (see acknowledgements) which correctly adds the required header information and allows the loading of all required resources.

### Payment request failure

The payment failed with an error stating that the client_secret was not in the correct format. This was traced to the incorrect use of 'client_secret' in the context file rather than as the variable client_secret. Once corrected the payment showed as 'succeeded' in the Stripe online portal.

### after initial build completed

On completion of the site build further testing revealed some issues listed here that needed correcting.

- The site rules were added to the homepage and so are easily viewable at any time.

- A link was added to the navbar to enable a logged in admin to access the admin pages for the site with one click. (see acknowledgements)

- On selecting an order from order history in the account page no order line items were displayed. These order items were viewable in the database as objects. This was traced to the order line items object not being passed to the checkout success page via views.py in the profile app. the addition of the line 'order_items = OrderLineItem.objects.filter(order=order.id)' and passing order_items back through context corrected this and the items then displayed correctly. A Toast message confirms that this is a past order that is being viewed.

- The order summary section of the profiles page did not have the correct styling for the items displayed. The addition of some Bootstrap5 classes and custom CSS classes corrected this.

- If logged out when completing the checkout the app crashed with a error about the user profile not being accessible. This was traced to a duplicate line 'profile = UserProfile.objects.get(user=request.user)' appearing before the if user is authenticated statement. removal of this line allowed the checkout to complete successfully and further test orders placed whilst logged out were all successfully completed.

- When creating a new user in the admin panel the admin must add the email not only to the user but also the email addresses section in accounts. Failure to do this results in an email sent notification to the user but no email is sent. no error is generated and the app does not crash but this is not an optimal user experience if missed. With an email addresses added correctly everything works as it should.

- the final site was put through VS Code code formatters, HTML language features for the HTML, Pylint for PEP8 compliant Python

[Back to top](#the-blue-box-shop)

## Future Developments

- There are two new app that I wish to develop at a later date. A message board service enabling users to discuss all things Dr. Who related and a fan art section allowing users to upload their own Dr. Who themed artworks. Both are envisioned to encourage interaction with the site and encourage users to keep coming back. The two apps are created in Django but for now each app's homepage greets users with an 'under construction' message and the option to go to the shop.
- Currently the site only takes orders from people with a UK address. the option is presented to email the site with an international shipping request. This is primarily a cost issue as overseas shipping can be expensive. A site admin can process an international order and create in on the database. Payment can be requested by bank transfer. However I feel that this is not an optimal user experience and with that in mind I plan to completely overhaul the checkout process. In the Stripe documentation it offers the option of having users redirected through Stripe's own checkout which can handle international shipping in a very customisable way even down to styling their checkout to better match the look of the site. So whilst a custom built checkout can give more of a bespoke feel Stripe offers a fully integrated customisable checkout experience 'off the shelf' that I feel would offer all required features for a lot less time and coding effort.
- The profile app would benefit from added features. These could include 
    - An option to store/update a default billing address and have this flagged as the delivery address also
    - An option to have a profile image either uploaded by the user or taken from a social account login
    - When the message boards and fan art sections go live an option to see recent posts to both these sections and quick links to access the posts

## Acknowledgements

- [Stan Triepels](https://djangowaves.com/tips-tricks/gitignore-for-a-django-project/) - for the excellent vscode django gitignore file
- [reMarkable 2](https://remarkable.com/) - e-ink tablet used to generate wireframes as PDF
- [Smashicons on Flaticon](https://www.flaticon.com/free-icons/tardis) - Tardis and under construction icons created by Smashicons. Check them out. Awesome icons for free
- [Bootstrap Icons](https://icons.getbootstrap.com/) - free svg icons from Bootstrap
- [Codepen](https://codepen.io/sosuke/pen/Pjoqqp) - hex to css filter convertor, allowing change of svg icons' color
- [Tech with Tim](https://www.youtube.com/watch?v=yO6PP0vEOMc) - setting up Django with a Google login option
- [Stackoverflow](https://stackoverflow.com/questions/62985371/how-do-i-target-label-for-with-jquery) - targeting specific labels in a form, thanks to kmoser for this helpful answer
- [Access-Control-Allow-Origin-Unblock](https://webextension.org/listing/access-control.html?version=0.3.8&type=install) - resolves CORS errors during development
- [CORS Unblock](https://chromewebstore.google.com/detail/cors-unblock/lfhmikememgdcahcdlaciloancbhjino?utm_source=ext_app_menu) - Google extension for CORS unblocking on Google Chrome Webstore
- [CI Boutique Ado on Github](https://github.com/Code-Institute-Solutions/boutique_ado_v1) - The guided full stack project from CI
- [Stackoverflow](https://stackoverflow.com/questions/1022236/linking-to-the-django-admin-site) - how to link to the admin site from the main site