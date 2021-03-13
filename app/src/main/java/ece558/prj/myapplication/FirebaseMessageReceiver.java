package ece558.prj.myapplication;

import android.app.NotificationChannel;
import android.app.NotificationManager;
import android.app.PendingIntent;
import android.content.Context;
import android.content.Intent;
import android.os.Build;
import android.widget.RemoteViews;
import androidx.core.app.NotificationCompat;
import com.google.firebase.messaging.FirebaseMessagingService;
import com.google.firebase.messaging.RemoteMessage;

public class FirebaseMessageReceiver extends FirebaseMessagingService {
    // Override the onMessageReceived() method to extract the title
    //  and body from the message passed in FCM
    @Override
    public void onMessageReceived(RemoteMessage remoteMessage) {
        //If notification payload is received
        if (remoteMessage.getNotification() != null) {
            //notification received directly
            showNotification(remoteMessage.getNotification().getTitle(),
                    remoteMessage.getNotification().getBody());
        }
    }

    //Method to get custom design for display of notification
    private RemoteViews getCustomDesign(String title, String message) {
        RemoteViews remoteViews = new RemoteViews(getApplicationContext().getPackageName(),
                                                    R.layout.notification);
        remoteViews.setTextViewText(R.id.title, title);
        remoteViews.setTextViewText(R.id.message, message);
        remoteViews.setImageViewResource(R.id.icon, R.drawable.magnify_glass_icon);
        return remoteViews;
    }


    //Method to display Notification
    public void showNotification(String title, String message) {
        //Pass the Intent to switch to the MainActivity
        Intent intent = new Intent(this, MainActivity.class);
        //Assign channel ID
        String channel_id = "notification_channel";
        //Set FLAG_ACTIVITY_CLEAR_TOP flag is set to clear the activities
        // present in the activity stack,
        intent.addFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP);
        //pass the intent to the pending intent to start the next activity
        PendingIntent pendingIntent = PendingIntent.getActivity(this, 0, intent,
                PendingIntent.FLAG_ONE_SHOT);
        //Creating a Builder object using NotificationCompat class.
        NotificationCompat.Builder builder = new NotificationCompat.Builder(
                getApplicationContext(),
                channel_id)
                .setSmallIcon(R.drawable.magnify_glass_icon)
                .setAutoCancel(true)
                .setVibrate(new long[]{1000, 1000, 1000,
                        1000, 1000})
                .setOnlyAlertOnce(true)
                .setContentIntent(pendingIntent);
        //A customized design for notification can be set only for android 4.1 so adding
        // the following condiion to check
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.JELLY_BEAN) {
            builder = builder.setContent(getCustomDesign(title, message));
        } else {
            builder = builder.setContentTitle(title)
                            .setContentText(message)
                            .setSmallIcon(R.drawable.magnify_glass_icon);
        }
        //Create a object of notification manager class to notifiy the user of any events that
        // happen in the background
        NotificationManager notificationManager = (NotificationManager) getSystemService(
                                                            Context.NOTIFICATION_SERVICE);
        if(Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            NotificationChannel notificationChannel = new NotificationChannel(
                                                    channel_id, "web_app",
                                                    NotificationManager.IMPORTANCE_HIGH);
            notificationManager.createNotificationChannel(notificationChannel);
        }
        notificationManager.notify(0, builder.build());
    }
}