from cardgame import create_app
from cardgame import recreate_databases

app = create_app()

if __name__ == "__main__":
    if input("Reset/Create Databases?\n\n1) No\n2) Yes\n\nInput:\t") == "2":
        recreate_databases(app)
    app.run(host="0.0.0.0", port="8080", debug=True)
