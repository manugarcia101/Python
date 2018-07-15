from app import create_app

app = create_app()

''' To run the script directly, I setted this function
    ONLY FOR THE DEVELOPMENT PROCESS'''
if __name__ == '__main__':
    app.run(debug=True)
