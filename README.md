# Pitch-Perfect

## Description
This is a blogging application that enables users to log in and create posts. A user can also view posts from other users, comment on them and even delete posts that they created.
### By Sauda Habib

## Setup/Installation Requirements

### Prerequisites
* python3.6
* pip
* Virtual environment(virtualenv)
* Flask-Mail
* PostgreSQL

## Cloning and running
Clone the application using git clone(this copies the app onto your device). In your terminal:

  ```  $ git clone https://github.com/saudahabib/writerly/

  ```  $ cd writerly```

## Creating the virtual environment

  ```  $ python3.6 -m venv --without-pip virtual```

  ```  $ source virtual/bin/env```

  ```  $ curl https://bootstrap.pypa.io/get-pip.py | python```

## Installing Flask and other Modules

  ```  $ python3.6 -m pip install Flask```

  ```  $ python3.6 -m pip install Flask-Bootstrap```

  ```  $ python3.6 -m pip install Flask-Script```

  ```  $ python3.6 -m pip install Flask-Mail```


## Testing the Application
To run the tests for the class files:

  ```  $ python3.6 manage.py test```

## Technologies Used
* Python 3.6
* Flask

## Behaviour driven development/ Specifications
| Behaviour    | Input     | Output|
| :------------- | :------------- |:---------|
|   Post blog     |     Blog is saved in a database | Blog from database|
|Comment on blog|Leave a comment| Comment saved for display|
|Login and authenticate|Email address and password|Saved and used for authentication|


## Support and contact details
Feel free to reach out to the developer at:

* Mobile: 0714828944
* Email: saudababs00@gmail.com
## License
MIT License Copyright (c) {2019} Sauda Habib Salim
