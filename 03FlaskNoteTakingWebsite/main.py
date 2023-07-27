from website import create_app   #Pulling create_app from the website folder

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)  #debug means any changes made in code, will auto run on web sever