from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'search for the name by /api/name'
@app.route('/<name>')
def hello_worlds(name):
    return f'{name} youtuber'

@app.route('/api/<name>')
def hello_name(name):
    return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@200;600&display=swap" rel="stylesheet">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300&display=swap" rel="stylesheet">
    <style>
    body{
    margin: 0px;
}
.navbar{
    margin: 0px;
    display: flex;
    justify-content: space-between;
}
.nav-elements{
    display: flex;
    padding-left: 30px;
}
.list-elements{
    list-style: none;
    padding: 10px 10px;
    color: black;
   font-family:  Arial, "Helvetica Neue", Helvetica, sans-serif;
   font-size: 20px;
   font-weight: 550;
}
.intro{
    margin-top: 9rem;
    display: flex;
    width: 100%;
    justify-content: space-evenly;
}
.content{
    width: 35%;
    padding-left: 16rem;
}
.heading{
    font-family: 'Roboto', sans-serif;
    margin:0px;
}
#h2{
    margin-top: 1rem;
    margin-bottom: 3rem;
}
.join-link{
    display: flex;
    justify-content: space-between;
    margin-bottom: 1.5rem;
}
.new-meeting{
    background: #0d6efd;
    color: white;
    display: flex;
    justify-content: center;
    align-items: center ;
    border: 1px solid #0d6efd;
    width: 35%;
    border-radius: 5px;
    font-weight: 550;
    font-size: 15px;
}
.user-link{
    padding: 13px;
    display: flex;
    justify-content: center; 
    align-items: center;
    outline: #0d6efd;
    width: 45%;
    font-weight: 600;
}
.user-link:hover{
    border: 2px solid #0d6efd;
    border-radius: 5px;
}
.info{
    display: flex;

    font-family: Arial, "Helvetica Neue", Helvetica, sans-serif;
    font-size: 16px;
    font-weight: 550;
    color: rgb(33, 23, 23);
    font-family: Montserrat, sans-serif;
}
.infot{
    font-family: Montserrat, sans-serif;
    display: flex;
    font-family: 'Poppins', sans-serif;
    font-size: 16px;
    font-weight: 550;
    color: rgb(120, 116, 116);
    padding-top: 8px;
    padding-bottom: 2rem;
}
body{
    width: 100%;
}

    </style>
    
    <title>Document</title>
</head>
<body>
    <nav class="navbar">
            <ul class="nav-elements">
                <li class="list-elements">Meet Up</li>
            </ul>
            <ul class="nav-elements">
                <li class="list-elements">icon1</li>
                <li class="list-elements">icon1</li>
                <li class="list-elements">icon1</li>
            </ul>
    </nav>
    <div class="intro">
        <div class="duo-logo">
            <img src="image.png" alt="" width="350" class="zoom-img">
            <div class="text">Lorem ipsum dolor sit amet.</div>
        </div>
        <div class="content">
            <h1 class="heading">Premium Video Meetings.</h1>
            <h1 class="heading" id="h2">Now free for everyone.</h1>
            <div class="info">
                We re-engineered the service we build for secure business 
            </div>
            <div class="infot">
                meeting. Google Meet, to make it free and available for all.
            </div>
            <div class="join-link">
                <button class="new-meeting">
                    New Meeting
                </button>
                <input class="user-link" type="text" placeholder="Enter a code or link">
            </div>
            <hr>
            <p>Learn more about Google Meet</p>
        </div>
    </div>
</body>
</html>'''

if __name__ == '__main__':
    app.run()
