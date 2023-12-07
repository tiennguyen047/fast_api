from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required, get_jwt
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import ItemModel
from schemas import ItemSchema, ItemUpdateSchema

blp = Blueprint("Item", __name__, description="Opearation on items")

@blp.route("/item")
class Item(MethodView):
    @blp.response(200, ItemSchema(many=True))
    def get(self):
        return ItemModel.query.all()
    
    @jwt_required(refresh=True) # Require token to run this function
    @blp.arguments(ItemSchema)
    @blp.response(201, ItemSchema())
    def post(self, item_data):
        item = ItemModel(**item_data)
        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, messsage="An error occurred whilte interting the item")
        return item
    
@blp.route("/item/<int:item_id>")
class Item_id(MethodView):
    @jwt_required()
    def delete(self, item_id):
        # Require admin permission to delete item
        jwt = get_jwt()
        if not jwt.get("is_admin"):
            abort(400, message="admin privilege required")

        item = ItemModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "Item deleted"}

    @jwt_required()
    @blp.response(200, ItemSchema())
    def get(sekf, item_id):
        item = ItemModel.query.get_or_404(item_id)
        return item
    
    @jwt_required()
    @blp.arguments(ItemUpdateSchema)
    @blp.response(200, ItemSchema())
    def put(self, item_data, item_id):
        item = ItemModel.query.get(item_id)
        if item:
            item.price = item_data.price
            item.name = item_data.name
        else: ItemModel(id=item_id, **item_data)
        db.session.add(item)
        db.session.commit()
        return item