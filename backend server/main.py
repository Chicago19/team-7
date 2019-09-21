from flask import Flask, jsonify
import json

app = Flask(__name__)

REFERRALS  = "referral-links.json"
REFERRAL_URL = "url"
GAMES_PATH = "games.json"
PASSW_PATH = "password.json"
GAMES_URL_KEYWORD = 'url'
GAMES_USAGE_KEYWORD = 'usage'


#### Retrieve Password

@app.route('/parentpassword')
def get_pass():
    # Retrieves the current parent password
    password = parse_json_file(PASSW_PATH)
    return jsonify(password)

@app.route('/parentpassword/change/<new_pass>')
def change_pass(new_pass):
    password = parse_json_file(PASSW_PATH)



####


@app.route('/games')
def get_games():
    # Retrieves a dictionary of games in the database
    games = parse_json_file(GAMES_PATH)
    return jsonify(games)

@app.route('/games/get/<game_name>')
def get_game_link(game_name):
    # Retrieves the link for a given game_name
    games = parse_json_file(GAMES_PATH)
    return games[game_name][GAMES_URL_KEYWORD]

@app.route('/games/remove/<game_name>')
def remove_game(game_name):
    # Removes a game from the database
    games = parse_json_file(GAMES_PATH)

    if game_name in games:
        del games[game_name]

    write_json_file(games, GAMES_PATH)

    return "VErryYYy GooOd"

@app.route('/games/add/<game_name>/<game_url>')
def add_game(game_name, game_url):
    # Adds or updates a game to the json file
    games = parse_json_file(GAMES_PATH)

    if games.get(game_name) is None:
        games[game_name] = {}
    games[game_name][GAMES_URL_KEYWORD] = game_url

    write_json_file(games, GAMES_PATH)

    return "VEry GOOD"

#### Retrieving referral URL data
def parse_json_file(path):
    return json.load(open(path))

@app.route('/referrals')
def parse():
    # Sends a JSON response to the browser
    referrals = parse_json_file(REFERRALS)
    return jsonify(referrals)

@app.route('/referrals/get/<referral_name>')
def get_referral_link(referral_name):
    # Retrieves the link for a given referral_name
    referrals = parse_json_file(REFERRALS)
    return referrals[referral_name][REFERRAL_URL]

# Returns a dictionary formatted by the json file
def parse_json_file(path):
    return json.load(open(path))

    # Overwrites a json file with the given dictionary
    def write_json_file(data, path):
        with open(path, "w") as write_file:
            json.dump(data, write_file)


if __name__ == '__main__':
    app.run()
