<div id="top"></div>

[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<div align="center">
  <h1 align="center">Ecommerce</h3>

  <p align="center">
This is an example of an <b> e-commerce </b> website that offers online shopping.
It uses the Django server as a back-end, a Django for the front-end for dynamic performance, and the Django REST Framework to serve REST API service and manipulate data. Uses Bootstrap for responsiveness and better display on different devices
I faced various challenges in this project, including:

- storing user information and orders in cookies when user is not logged in and using that information after the user logged in
- Implementing cart page single-page using asynchronous JavaScript requests to the server and making changes without refreshing the page

  </p>
  </p>
</div>


### Built With
 * [Django](https://www.djangoproject.com/)
 * [Django REST Framework](https://www.django-rest-framework.org/)
* [Bootstrap](https://getbootstrap.com)
* [JQuery](https://jquery.com)


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

extract static folder

    tar -xf static.tar.xz

install required packages

    pip install -r requirements.txt

create databse tables

    python manage.py makemigrations 

    python manage.py migrate

create a super user

    python manage.py createsuperuser

start Django deveopment server

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
[stars-url]: https://github.com/cybera3s/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/cybera3s/Ecommerce.svg?style=for-the-badge
[issues-url]: https://github.com/cybera3s/Ecommerce/issues
[license-shield]: https://img.shields.io/github/license/cybera3s/Ecommerce.svg?style=for-the-badge
[license-url]: https://github.com/cybera3s/Ecommerce/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/cybera3s
