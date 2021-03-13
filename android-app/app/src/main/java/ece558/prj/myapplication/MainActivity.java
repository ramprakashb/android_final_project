package ece558.prj.myapplication;

import android.media.Image;
import android.provider.ContactsContract;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import com.bumptech.glide.Glide;
import com.google.android.gms.tasks.OnFailureListener;
import com.google.android.gms.tasks.OnSuccessListener;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.database.*;
import com.google.firebase.storage.FirebaseStorage;
import com.google.firebase.storage.StorageReference;

public class MainActivity extends AppCompatActivity {

    //Tag for mainactivity
    private static final String TAG = "MainActivity";

    //Database JSON Tag References
    public static final String DOOR_STATUS = "DOOR_STATUS";


    //Firebase Authentication variable
    private FirebaseAuth mFirebaseAuth;
    private FirebaseDatabase mFireDatabase;

    //UI Elements
    private Button mOpenDoor;
    private Button mGetPhoto;

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


        //Get open door button instance
        mOpenDoor = (Button) findViewById(R.id.openDoor);
        mOpenDoor.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                mFireDatabase.getReference().child(DOOR_STATUS).setValue("fa");
            }
        });

        //Get Download photo button instance and download the photo
        mGetPhoto = (Button) findViewById(R.id.getPhoto);
        final ImageView imageView = findViewById(R.id.photoRef);  //Get reference to image view
        final String url = "https://firebasestorage.googleapis.com/v0/b/final-project-backend.appspot.com/o/models.jpg?alt=media&token=6e40413c-d965-4722-a1e6-ef80f1b337c7";
        mGetPhoto.setOnClickListener(new View.OnClickListener() {
            @Override
                public void onClick(View v) {
                     Glide.with(getApplicationContext())
                                 .load(url)
                                 .into(imageView);
            }

        });
                //StorageReference url = storage.getReferenceFromUrl("gs://final-project-backend.appspot.com/models.jpg");
        //StorageReference gsRef = storage.getReferenceFromUrl("gs://final-project-backend.appspot.com/models.jpg");
        //Download directly from Storage Ref using glide



        /*
        mFireDatabase = FirebaseDatabase.getInstance();
        DatabaseReference myRef = mFireDatabase.getReference();

        myRef.setValue("Hello World!!");

        myRef.addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot snapshot) {
                String value = snapshot.getValue(String.class);
                Log.d(TAG, "Value is: "+ value);
            }

            @Override
            public void onCancelled(@NonNull DatabaseError error) {
                Log.w(TAG, "Failed to read value ",error.toException());
            }
        });
        */


    }
}