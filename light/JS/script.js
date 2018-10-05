// Initialize Firebase
//fill in your own config info
var config = {
  apiKey: "AIzaSyDmDtJOeyfAlIfSYb3f-ftWFHpa-p6OdbY",
  authDomain: "smart-solar-led.firebaseapp.com",
  databaseURL: "https://smart-solar-led.firebaseio.com",
  projectId: "smart-solar-led",
  storageBucket: "smart-solar-led.appspot.com",
  messagingSenderId: "429827155544"
};
firebase.initializeApp(config);

$(document).ready(function(){
  var database = firebase.database();
  var S1;
  var S3;

  // For Power Button
  database.ref().on("value", function(snap){
    S1 = snap.val().S1;
    if(S1 == 1){
      $(".lightStatus").text("The light is on");
      $(".powerButton").text("Turn Off");
    } else {
      $(".lightStatus").text("The light is off");
      $(".powerButton").text("Turn On");
    }
  });

  $(".powerButton").click(function(){
    var firebaseRef = firebase.database().ref().child("S1");
    if(S1 == 1){
      firebaseRef.set(0);
      S1 = 0;
    } else {
      firebaseRef.set(1);
      S1 = 1;
    }
  });

    // For Automatic Power 
    database.ref().on("value", function(snap){
      S2 = snap.val().S2;
      if(S2 == 1){
        $(".automaticHeading").text("Automatic Power On");
        $(".automaticPower").text("Turn Off");
      } else {
        $(".automaticHeading").text("Automatic Power Off");
        $(".automaticPower").text("Turn On");
      }
    });

    $(".automaticPower").click(function(){
      var firebaseRef = firebase.database().ref().child("S2");
      if(S2 == 1){
        firebaseRef.set(0);
        S2 = 0;
      } else {
        firebaseRef.set(1);
        S2 = 1;
      }
    });
});




  



