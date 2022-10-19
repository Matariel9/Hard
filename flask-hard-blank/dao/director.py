from dao.model.director import Director, DirectorSchema

class DirectorDao:
    def __init__(self, session):
        self.session = session
    
    def get_all(self):
        directors = Director.query.all()
        directorsSchema = DirectorSchema(many=True)
        return directorsSchema.dump(directors)

    def get_one(self, id):
        directors = Director.query.get(id)
        directorSchema = DirectorSchema()
        return directorSchema.dump(directors)