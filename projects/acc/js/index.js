if ('Accelerometer' in window && 'Gyroscope' in window) {
  //document.getElementById('moApi').innerHTML = 'Generic Sensor API';
  
  let accelerometer = new Accelerometer();
  accelerometer.addEventListener('reading', e => MaccelerationHandler(accelerometer, 'moAccel'));
  accelerometer.start();
  
  let accelerometerWithGravity = new Accelerometer({includeGravity: true});
  accelerometerWithGravity.addEventListener('reading', e => MaccelerationHandler(accelerometerWithGravity, 'moAccelGrav'));
  accelerometerWithGravity.start();
  var global_caliber = 0;
  var counter = 1;
  
  let gyroscope = new Gyroscope();
  gyroscope.addEventListener('reading', e => rotationHandler({
    alpha: gyroscope.x,
    beta: gyroscope.y,
    gamma: gyroscope.z
  }));
  gyroscope.start();
  
  intervalHandler('Not available in Generic Sensor API');
  
} else if ('DeviceMotionEvent' in window) {
  //document.getElementById('alert').style.display = 'none';
  //document.getElementById('moApi').innerHTML = 'Device Motion API';
  
  window.addEventListener('devicemotion', function (eventData) {
    accelerationHandler(eventData.acceleration, 'moAccel');
    MaccelerationHandler(eventData.accelerationIncludingGravity, 'moAccelGrav');
    rotationHandler(eventData.rotationRate);
    intervalHandler(eventData.interval);
  }, false);
} else {
  //document.getElementById('alert').style.display = 'none';
  //document.getElementById('moApi').innerHTML = 'No Accelerometer & Gyroscope API available';
}

function accelerationHandler(acceleration, targetId) {
  var info, xyz = "[X, Y, Z]";

  info = xyz.replace("X", acceleration.x && acceleration.x.toFixed(3));
  info = info.replace("Y", acceleration.y && acceleration.y.toFixed(3));
  info = info.replace("Z", acceleration.z && acceleration.z.toFixed(3));
  //document.getElementById(targetId).innerHTML = info;
}

function MaccelerationHandler(acceleration, targetId) {
  var info, xyz = "[X, Y, Z]";

  var zz = (acceleration.z && acceleration.z.toFixed(3));
  global_caliber += zz;
  counter +=1;
  if (zz>10) {
    var avg = (global_caliber/counter);
    var newPara = document.createElement('p');
    newPara.textContent = avg;
    document.getElementById("updateDiv").appendChild(newPara);
    document.body.style.backgroundColor = "red";
  }
}


function rotationHandler(rotation) {
  var info, xyz = "[X, Y, Z]";

  //info = xyz.replace("X", rotation.alpha && rotation.alpha.toFixed(3));
  //info = info.replace("Y", rotation.beta && rotation.beta.toFixed(3));
  //info = info.replace("Z", rotation.gamma && rotation.gamma.toFixed(3));

  var xx = (rotation.alpha && rotation.alpha.toFixed(3));
  var yy = (rotation.beta && rotation.beta.toFixed(3));
  var zz = (rotation.gamma && rotation.gamma.toFixed(3));

  var mean = (((xx)^2) + ((yy)^2) + ((zz)^2))*(1/2);
  //document.getElementById("mean").innerHTML = mean;
  //document.getElementById("moRotation").innerHTML = info;

}

function intervalHandler(interval) {
  //document.getElementById("moInterval").innerHTML = interval;
}



if (location.href.indexOf('debug') !== -1) {
  //document.getElementById('alert').style.display = 'none';
}