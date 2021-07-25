from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
    def get(self,name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message': '找不到商店'}, 404

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': '商店{}，已經存在'.format(name)}, 400

        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {'message': '出錯了'}
        return store.json(), 201

    def delete(self,name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
        return {'message': '商店已刪除'}


class StoreList(Resource):
    def get(self):
        return {'stores': list(map(lambda x: x.json(), StoreModel.query.all()))}
