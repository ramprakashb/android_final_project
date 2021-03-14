# Setting up the back-end

1) Run the setup bash scripts
Before you start run the setup scripts to ensure you have
all the libraries ready
- `sudo setup-mqtt.sh`
- `setup-google-sdk.sh`

The scripts will implement the below :

- Setting up the Firebase
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
