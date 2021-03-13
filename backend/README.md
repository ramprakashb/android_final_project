# Setting uo the backend

1) Install Redis

What is Redis?

- Redis is an open source (BSD licensed),
  in-memory data structure store, used as a database, cache,
  and message broker.
  Redis provides data structures such as strings,
  hashes, lists, sets, sorted sets with range queries,
  bitmaps, hyperloglogs, geospatial indexes, and streams.

  Link to Redis: https://redis.io/

  To download Redis : `wget -c https://download.redis.io/releases/redis-6.2.1.tar.gz`

  After downloading it:
  1) `tar -xf redis-6.2.1.tar.gz`
  2) `cd redis-6.2.1`
  3) If you want to install the application somewhere specific `cd src` and modify the Makefile
  at line 46 `PREFIX` - add your directory there
  4) Go to the root directory and `make` && `make test`
  5) If all tests have passed `make install`
  If you are missing the latest `tcl` `sudo apt-get install tcl`

  2) Setting up the server
  For this project we are going to use Firebase
  Firebase is a Google product , and offers free services for students
  However, any other Api most probably will follow the same instructions

  In order to use the Python interface to the Google's Firebase REST APIs:

  - `pip install firebase`

  From : https://firebase.google.com/docs/admin/setup#python

  Add the Firebase Admin SDK to your server

  The Admin SDK is a set of server libraries that lets you interact with Firebase from privileged environments to perform actions like:

  `sudo pip install firebase-admin`

  - Read and write Realtime Database data with full admin privileges.
  - Programmatically send Firebase Cloud Messaging messages using a simple, alternative approach to the Firebase Cloud Messaging server protocols.

  - Generate and verify Firebase auth tokens.
  - Access Google Cloud resources like Cloud Storage buckets and Cloud Firestore databases associated with your Firebase projects.
  - Create your own simplified admin console to do things like look up user data or change a user's email address for authentication.


  When authorizing via a service account, you have two choices for providing the credentials to your application. You can either set the GOOGLE_APPLICATION_CREDENTIALS environment variable, or you can explicitly pass the path to the service account key in code. The first option is more secure and is strongly recommended.

  To set the environment variable:

  Set the environment variable GOOGLE_APPLICATION_CREDENTIALS to the file path of the JSON file that contains your service account key. This variable only applies to your current shell session, so if you open a new session, set the variable again.

  `export GOOGLE_APPLICATION_CREDENTIALS="/home/user/Downloads/service-account-file.json"`

  After you've completed the above steps, Application Default Credentials (ADC) is able to implicitly determine your credentials, allowing you to use service account credentials when testing or running in non-Google environments.

  Initialize the SDK as shown:
  `default_app = firebase_admin.initialize_app()`
