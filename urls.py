from server import app, index


app.add_api_route("/", index)
