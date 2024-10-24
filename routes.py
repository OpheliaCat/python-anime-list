from flask import jsonify, request

data = {
    'anime': ['Steins Gate', 'Attack on Titan', 'One Piece', 'Naruto', 'Bleach', 'Death Note', 'Tokyo Ghoul', 'My Hero Academia', 'Demon Slayer', 'Black Clover'],
    'manga': []
}

def reg_routes(app, db):
    @app.route('/')
    def home():
        return jsonify({'message': 'Hello, World!'}), 200

    @app.route('/anime/<int:id>')
    def getAnimeByID(id):
        return jsonify({'result': f'Found anime: {data["anime"][int(id)]}'}), 200

    @app.route('/anime/list', methods=['GET', 'POST'])
    def getAnimeList():
        if request.method == 'GET':
            keyword = request.args.get('keyword')
            if keyword is None:
                return jsonify({'result': data['anime']}), 200
            else:       
                return jsonify({'result': [anime for anime in data['anime'] if keyword.lower() in anime.lower()]}), 200
        else:
            data['anime'].append(request.json['anime'])
            return jsonify({'result': data['anime']}), 201
    return app