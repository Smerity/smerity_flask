(function() {
  var N, context, cvs, plot, render, serp;

  cvs = document.getElementById("display");

  context = cvs.getContext('2d');

  N = cvs.width;

  serp = function(x, y, dist, depth, maxDepth) {
    var d2;
    if (depth > maxDepth) return;
    d2 = dist / 2;
    context.beginPath();
    context.moveTo(x, y);
    context.lineTo(x + dist, y + dist);
    context.lineTo(x - dist, y + dist);
    context.closePath();
    context.stroke();
    serp(x, y, d2, depth + 1, maxDepth);
    serp(x + d2, y + d2, d2, depth + 1, maxDepth);
    return serp(x - d2, y + d2, d2, depth + 1, maxDepth);
  };

  plot = function(maxDepth) {
    return serp(N / 2, 0, N / 2, 0, maxDepth);
  };

  render = function(depth) {
    var f, newDepth, trigger;
    context.clearRect(0, 0, N, N);
    plot(depth);
    trigger = 7;
    newDepth = depth < trigger ? depth + 1 : 0;
    f = function() {
      return render(newDepth);
    };
    if (depth === trigger) {
      return setTimeout(f, 1600);
    } else {
      return setTimeout(f, 400);
    }
  };

  render(0);

}).call(this);
