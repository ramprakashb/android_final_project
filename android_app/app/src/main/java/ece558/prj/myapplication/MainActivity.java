package ece558.prj.myapplication;

import android.graphics.Color;
import android.graphics.drawable.ColorDrawable;
import android.graphics.drawable.Drawable;
import android.media.Image;
import android.net.Uri;
import android.provider.ContactsContract;
import android.renderscript.Sampler;
import android.util.Log;
import android.view.View;
import android.widget.*;
import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.appcompat.app.ActionBar;
import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import com.bumptech.glide.Glide;
import com.bumptech.glide.GlideBuilder;
import com.bumptech.glide.load.DataSource;
import com.bumptech.glide.load.engine.GlideException;
import com.bumptech.glide.request.RequestListener;
import com.bumptech.glide.request.target.Target;
import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.OnFailureListener;
import com.google.android.gms.tasks.OnSuccessListener;
import com.google.android.gms.tasks.Task;
import com.google.android.material.floatingactionbutton.FloatingActionButton;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.database.*;
import com.google.firebase.messaging.FirebaseMessagingService;
import com.google.firebase.messaging.RemoteMessage;
import com.google.firebase.storage.FirebaseStorage;
import com.google.firebase.storage.StorageReference;

public class MainActivity extends AppCompatActivity {

    //Tag for mainactivity
    private static final String TAG = "MainActivity";

    //Database JSON Tag References
    public static final String DOOR_STATUS = "DOOR_STATUS";
    public static final String DOORBELL = "DOORBELL";
    public static final String IMAGE = "IMAGE";

    //Firebase Authentication variable
    private FirebaseAuth mFirebaseAuth;
    private FirebaseDatabase mFireDatabase;
    private ValueEventListener mpostListener;

    //UI Elements
    private ToggleButton mOpenDoor;
    private FloatingActionButton mGetPhoto;
    private TextView mDateNotify;
    private TextView mPayloadNotify;
    private ToggleButton mRingBell;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        //Initializing the Firebase Database
        mFireDatabase = FirebaseDatabase.getInstance();

        //Firebase Storage instance
        FirebaseStorage storage = FirebaseStorage.getInstance();

        //Get Storage ref
        StorageReference gsReference = FirebaseStorage.getInstance().getReference();

        //Database ref
        DatabaseReference ref = mFireDatabase.getReference();

        //Storage Ref
        StorageReference storageReference = storage.getReference();

        //Action Bar - to change color
        ActionBar actionBar;
        actionBar = getSupportActionBar();

        //Define colordrawable object and parse color
        ColorDrawable colorDrawable = new ColorDrawable(Color.parseColor("#00bfff"));

        actionBar.setBackgroundDrawable(colorDrawable);

        //Open door toggle button is obtained and then the DOOR_STATUS key in the
        //Firebase Realtime database is updated
        mOpenDoor = (ToggleButton) findViewById(R.id.openDoor);
        mOpenDoor.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
                if (isChecked) {
                    mFireDatabase.getReference().child(DOOR_STATUS).setValue("Open");
                } else {
                    mFireDatabase.getReference().child(DOOR_STATUS).setValue("Closed");
                }
            }
        });



        //The date value is queried from the firebase database and then displayed
        //as a text view.
        mDateNotify = (TextView) findViewById(R.id.notification_date);
        final DatabaseReference databaseReference = mFireDatabase.getReference().child("DATE_TIME");
        databaseReference.addValueEventListener(new ValueEventListener() {
            //The date value gets updated whenever there is a change in the date
            //value in DB
            @Override
            public void onDataChange(@NonNull DataSnapshot snapshot) {
                Log.d("Date_Retrieved",snapshot.getValue().toString());
                mDateNotify.setText(snapshot.getValue().toString());
            }

            @Override
            public void onCancelled(@NonNull DatabaseError error) {

            }
        });

        //Door bell is updated whenever the user presses the toggle buttton
        //and similar to the Door status the value in the DB is updated.
        mRingBell = (ToggleButton) findViewById(R.id.ringBell);
        mRingBell.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
                if (isChecked) {
                    mFireDatabase.getReference().child(DOORBELL).setValue("true");
                } else {
                    mFireDatabase.getReference().child(DOORBELL).setValue("false");
                }
            }
        });


        //Get Download photo button instance and download the photo
        mGetPhoto = (FloatingActionButton) findViewById(R.id.getPhoto);
        final ImageView imageView = findViewById(R.id.photoRef);  //Get reference to image view
        final StorageReference photoRef = FirebaseStorage.getInstance().getReference().child("camera-image.png");//cam-image/facesNew.png");
        final ProgressBar progressBar = (ProgressBar) findViewById(R.id.progress);
        //A progress bar will be shown whenever the user presses the get photo button. This progress bar
        //will be shown intermittently till the photo gets downloaded.
        progressBar.setVisibility(View.GONE);
        mGetPhoto.setOnClickListener(new View.OnClickListener() {
            @Override
                public void onClick(View v) {
                    progressBar.setVisibility(View.VISIBLE);
                    photoRef.getDownloadUrl().addOnCompleteListener(new OnCompleteListener<Uri>(){
                        @Override
                        public void onComplete(@NonNull Task<Uri> task) {
                            if(task.isSuccessful()) {
                                //Glide package is used to display the photo on the phone.
                                Glide.with(MainActivity.this)
                                        .load(task.getResult())

                                        //The glide listener is used to set the photo to the image view and if there is a failure
                                        // the exception gets thrown.
                                        //The progress bar is visible till the image gets downloaded.
                                        .listener(new RequestListener<Drawable>() {
                                            @Override
                                            public boolean onLoadFailed(@Nullable GlideException e, Object model, Target<Drawable> target, boolean isFirstResource) {
                                                progressBar.setVisibility(View.GONE);
                                                return false;
                                            }

                                            @Override
                                            public boolean onResourceReady(Drawable resource, Object model, Target<Drawable> target, DataSource dataSource, boolean isFirstResource) {
                                                progressBar.setVisibility(View.GONE);
                                                return false;
                                            }
                                        })

                                        //Once the photo gets downloaded it gets placed into the image view.
                                        .into(imageView);
                                mFireDatabase.getReference().child(IMAGE).setValue(false);
                            } else {
                                Toast.makeText(MainActivity.this, task.getException().getMessage(), Toast.LENGTH_SHORT).show();
                            }
                        }
                    });
            }

        });
    }
}