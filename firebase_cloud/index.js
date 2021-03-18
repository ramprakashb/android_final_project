const functions = require('firebase-functions');
const admin = require('firebase-admin');
const { ref } = require('firebase-functions/lib/providers/database');
admin.initializeApp(functions.config().firebase);

//The function defined here is used to take the instance from 
// the firebase database and firebase cloud messaging service and 
// trigger a notification whenever there is a change in the firebase 
// database function named "IMAGE"

exports.changeValue12 = functions.database.ref('IMAGE')
          .onWrite((change, context) => {
               //get the value for image status
               var image_status = change.after.val();
               console.log("image_status = " + image_status);
               //define the values for the notification
               
               //write the value to console
               console.log("type of var " + typeof(image_status));
               //define ref to access the database
               var db = admin.database();
               //The token reference defined here is used to get the token value
               //which get set by the onNewToken method in the FirebaseMessageReceiver
               //class in the Android app java code.
               var token_ref = db.ref('TOKEN');
               //use the token ref to query the token value
               token_ref.once("value", function(snapshot) {
                    console.log("token val = " + snapshot.val());
                    var regToken = snapshot.val();
                    
                    var message = { 
                              notification: {

                                   //Set the Notification Title and 
                                   //Notification body
                                   title: 'Intruder Detected',
                                   body: 'Open App to view Face'
                              },
                              token:regToken
                         };
                    //check if the image status is true
                    if (image_status) {
                    admin.messaging().send(message)
                         .then((response) => {
                              console.log('Successfully sent message: ', response);
                         })
                         .catch((error) => {
                              console.log('Error sending message: ', error);
                         });
                    }
               
              }, function (errorObject) {
                   console.log("The read failed: " + errorObject.code);
              });	
          		
          return null;

          });