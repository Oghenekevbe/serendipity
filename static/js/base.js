  // Define an array of image URLs
let imageUrls = [
    '../media/images/1.jpg',       
    '../media/images/2.jpg',       
    '../media/images/3.jpg',       
    '../media/images/4.jpg',       
    '../media/images/5.jpg',       
    '../media/images/6.jpg',  
  ];
  
  let currentIndex = 0;
  
  // Function to change the background image
  function changeBackground() {
    let imageUrl = imageUrls[currentIndex];
    document.body.style.backgroundImage = 'url(' + imageUrl + ')';
    currentIndex = (currentIndex + 1) % imageUrls.length;
  }
  
  // Call the function initially
  changeBackground();

  // Set interval to call the function every 3 seconds
setInterval(changeBackground, 3000);