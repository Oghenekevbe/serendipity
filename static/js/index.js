function targetMobile() {

    if (window.innerWidth<=800) {
        document.getElementById('index-content').style.display = 'none'
        
        document.getElementById('welcome-button').style.display = 'block'
        document.getElementById('welcome-button').style.width = '160px'
        document.getElementById('welcome-button').style.marginTop = '200px'
        document.getElementById('welcome-button').style.marginLeft = '40px'
        document.getElementById('welcome-button').addEventListener('click', function (event) {
            event.preventDefault();
            document.getElementById('welcome-button').style.display = 'none'
            document.getElementById('index-content').style.display = 'block'

           
        })
    }else{
        document.getElementById('welcome-button').style.display = 'none'
        
        
    }
    
}

targetMobile()


window.addEventListener('resize', targetMobile)