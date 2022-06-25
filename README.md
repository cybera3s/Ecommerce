<div id="top"></div>

[![LinkedIn][linkedin-shield]][linkedin-url]



<div>
  <h1 align="center">Ecommerce</h1>

  <p>
This is an example of an <b> e-commerce </b> website that offers online shopping.
It uses the Django server as a back-end and also as the front-end for dynamic performance, and the Django REST Framework to serve REST API service and manipulate data. Uses Bootstrap for responsiveness and better display on different devices
I faced various challenges in this project, including:

- storing user information and orders in cookies when user is not logged in and using that information after the user logged in
- Implementing cart page single-page using asynchronous JavaScript requests to the server and making changes without refreshing the page

  
  </p>
</div>
<h1 align="center">Home Page</h1>
<img src="https://user-images.githubusercontent.com/74768669/169667903-ac1291af-53de-49da-bb68-87e95de2b2f6.png" alt="index page" >

<h1 align="center">Detail Page</h1>
<img src="https://user-images.githubusercontent.com/74768669/175774302-5a083999-dbe5-46d3-8b67-b02d20e2d802.png"
     alt="detial page" />
<h1 align="center">Contact Us Page</h1>
<img src="https://user-images.githubusercontent.com/74768669/175774378-f09082f0-b069-4a38-a718-77b318f80bf2.png"
     alt="contact us page" />
<h1 align="center">Customer Panel Page</h1>
<img src="https://user-images.githubusercontent.com/74768669/175774467-75612e26-4a94-49b3-bbeb-2d199261c867.png" 
     alt="customer panel page" />
<h1 align="left">Checkout Page</h1>
<img src="https://user-images.githubusercontent.com/74768669/175774512-5dd270be-754c-4a7d-a032-97cf1d6ad666.png"
    alt="Checkout page" />
<h1 align="right">Mobile size Overview</h1>


https://user-images.githubusercontent.com/74768669/175774849-ec6bc154-e0b5-4655-890e-2459ace22cc0.mp4





### Built With
 * [Django](https://www.djangoproject.com/)
 * [Django REST Framework](https://www.django-rest-framework.org/)
* [Bootstrap](https://getbootstrap.com)
* [JQuery](https://jquery.com)

# Deployed
```
https://aivashop.pythonanywhere.com/en/
  ```


### Prerequisites


* python (Debian)
  
```sh
sudo apt install python
  ```

for other platforms go to  [this link](https://www.python.org/downloads/)

### Installation

Clone the repo

   ```sh
  git clone https://github.com/cybera3s/Ecommerce.git
   ```
change to root folder  

    cd Ecommerce/

create virtual environment 

    python -m virtualenv venv

  activate venv
  

    source venv/bin/activate

install required packages

    pip install -r requirements.txt

change to Project folder  

    cd ecommerce/

extract static and media folder and remove archive file

    tar -xf media-static.tar.xz && rm media-static.tar.xz

create migrations

    python manage.py makemigrations 


create database tables

    python manage.py migrate

create a super user

    python manage.py createsuperuser

load prepared data

    python manage.py loaddata data.json

compile translated messages

    python manage.py compilemessages

start Django development server

    python manage.py runserver

if everything goes well go to:  http://localhost:8000
 


[comment]: <> (<!-- USAGE EXAMPLES -->)

[comment]: <> (## Usage)

[comment]: <> (if both development servers or up go to home page by)

[comment]: <> ( http://localhost:8000)

[comment]: <> (You can log in with the username and password you created for your superuser)

[comment]: <> (after log in you redirect to [students]&#40;http://localhost:8080/students&#41; table page you can add or delete any row of table)

[comment]: <> (Any other usage and information served API will find in http://127.0.0.1:8000/swagger/)

<!-- LICENSE -->

## License

Distributed under the GPL License




<!-- CONTACT -->

## Contact

Sajad Safa - cybera.3s@gmail.com

Project Link: [https://github.com/cybera3s/Ecommerce](https://github.com/cybera3s/Ecommerce)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/cybera3s/Ecommerce.svg?style=for-the-badge
[contributors-url]: https://github.com/cybera3s/Ecommerce/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/cybera3s/Ecommerce.svg?style=for-the-badge
[forks-url]: https://github.com/cybera3s/Ecommerce/network/members
[stars-shield]: https://img.shields.io/github/stars/cybera3s/Ecommerce.svg?style=for-the-badge
[stars-url]: https://github.com/cybera3s/Ecommerce/stargazers
[issues-shield]: https://img.shields.io/github/issues/cybera3s/Ecommerce.svg?style=for-the-badge
[issues-url]: https://github.com/cybera3s/Ecommerce/issues
[license-shield]: https://img.shields.io/github/license/cybera3s/Ecommerce.svg?style=for-the-badge
[license-url]: https://github.com/cybera3s/Ecommerce/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/cybera3s
