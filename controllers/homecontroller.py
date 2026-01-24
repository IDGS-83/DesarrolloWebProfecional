from flask import Blueprint

BlueprintHome = Blueprint('home',__name__)
@BlueprintHome.route('/home')
def home():
    return {'msg': 'Hola desde home'}