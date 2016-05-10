var start = new Date().getTime();

// Modified for the purpose of demonstrating that m, n are respected
var asynchronousOperation = function(callback) {
  var t = Math.floor(Math.random() * 500 + 2000);
  var now = new Date().getTime()
  setTimeout(function() {
    console.log("t=" + t + ", d=" + (now - start));
    callback();
  }, t); 
}; 
 
var run = function(n, m) {
  var operationDone = function() {
    console.log('OK');
  };
 
  var initial, queue = Math.max(0, n - m);
  
  var next = function() {
    if(queue > 0) {
      // There are more in the queue
      queue--;
      asynchronousOperation(next);
    } else {
      // No unstarted jobs left; am I last?
      initial--;
      if(initial == 0) {
        // I was last
        operationDone();
      }
    }
  }
  
  for(initial = 0; initial < Math.min(m, n); initial++) {
    asynchronousOperation(next);
  }
  console.log("Started " + n + " asynchronous operations");
}
run(12, 3);
