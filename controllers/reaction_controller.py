from flask import jsonify
from models import models
from controllers import base_controller
import time, datetime

def create(params): 
    #Initialize
    response = {}
    requiredFields = ["user_id", "post_id"]
    reactionFields = {}

    #Check for Required Fields
    for field in requiredFields:
        if params.get(field, None) == None:
            response["message"] = "Missing Required Parameters: {}".format(requiredFields)
            status = 400
            return jsonify(response), status
        reactionFields[field] = params.get(field, None)

    #Check for Invalid Parameters
    if base_controller.verify(params, requiredFields): 
        response["message"] = "Request has invalid parameter {}".format(base_controller.verify(params, requiredFields))
        status = 400
    else:
        #Check for Numerical IDs
        try:
            reactionFields["post_id"] = int(reactionFields["post_id"])
            reactionFields["user_id"] = int(reactionFields["user_id"])
        except:
            response["message"] = "Request has incorrect parameter type"
            status = 400
            return jsonify(response), status

        if reactionFields["user_id"] == 0:
            response["message"] = "Please login to like this post."
            status = 400
            return jsonify(response), status

        #Add Product to Database
        reaction = models.Reaction(
            user_id=reactionFields["user_id"],
            post_id=reactionFields["post_id"],
            )
        models.db.session.add(reaction)
        models.db.session.commit()
        response["message"] = "Reaction created successfully!"
        status = 200
  
    return jsonify(response), status

def show(params):
    #Initialize
    response = {}
    requiredFields = ["reaction_id"]
    reactionFields = {}

    #Check for Required Fields
    for field in requiredFields:
        if params.get(field, None) == None:
            response["message"] = "Missing Required Parameters: {}".format(requiredFields)
            status = 400
            return jsonify(response), status
        reactionFields[field] = params.get(field, None)

    #Check for Invalid Parameters
    if base_controller.verify(params, requiredFields): 
        response["message"] = "Request has invalid parameter {}".format(base_controller.verify(params, requiredFields))
        status = 400
    else:
        #Query for Reaction
        reaction = models.Reaction.query.filter_by(reaction_id=reactionFields["reaction_id"]).first()
        
        if reaction is not None:
            #Query Successful
            response["reaction_id"] = reaction.reaction_id
            response["user_id"] = reaction.user_id
            response["post_id"] = reaction.post_id
            status = 200
        else:
            #Query Unsuccessful
            response["message"] = "Reaction cannot be found"
            status = 200

    return jsonify(response), status

def display_all(params):
    #Initialize
    response = {}
    requiredFields = ["post_id"]
    reactionFields = {}

    #Check for Required Fields
    for field in requiredFields:
        if params.get(field, None) == None:
            response["message"] = "Missing Required Parameters: {}".format(requiredFields)
            status = 400
            return jsonify(response), status
        reactionFields[field] = params.get(field, None)

    #Check for Invalid Parameters
    if base_controller.verify(params, requiredFields): 
        response["message"] = "Request has invalid parameter {}".format(base_controller.verify(params, requiredFields))
        status = 400
    else:
        #Query for Reaction
        reactions = models.Reaction.query.filter_by(post_id=reactionFields["post_id"]).all()
        users = list()

        for reaction in reactions:
            users.append(reaction.user_id)
        
        response["users"] = users
    
        status = 200
    return jsonify(response), status

def delete(params):
    #Initialize
    response = {}
    requiredFields = ["post_id", "user_id"]
    reactionFields = {}

    #Check for Required Fields
    for field in requiredFields:
        if params.get(field, None) == None:
            response["message"] = "Missing Required Parameters: {}".format(requiredFields)
            status = 400
            return jsonify(response), status
        reactionFields[field] = params.get(field, None)

    #Check for Invalid Parameters
    if base_controller.verify(params, requiredFields): 
        response["message"] = "Request has invalid parameter {}".format(base_controller.verify(params, requiredFields))
        status = 400
    else:
        #Query for Product
        reaction = models.Reaction.query.filter_by(post_id=reactionFields["post_id"]).filter_by(user_id=reactionFields["user_id"]).first()
        
        if reaction is not None:
            #Query Successful
            models.db.session.delete(reaction)
            models.db.session.commit()
            response["message"] = "Reaction successfully removed"
            status = 200
        else:
            #Query Unsuccessful
            response["message"] = "Reaction cannot be found"
            status = 200

    return jsonify(response), status

def delete_all(params):
    #Initialize
    response = {}
    requiredFields = []
    optionalFields = ["post_id", "user_id"]
    reactionFields = {}

    #Check for Required Fields
    for field in requiredFields:
        if params.get(field, None) == None:
            response["message"] = "Missing Required Parameters: {}".format(requiredFields)
            status = 400
            return jsonify(response), status
        reactionFields[field] = params.get(field, None)

    #Check for Optional Fields
    for field in optionalFields:
        reactionFields[field] = params.get(field, None)

    #Check for Invalid Parameters
    if base_controller.verify(params, requiredFields): 
        response["message"] = "Request has invalid parameter {}".format(base_controller.verify(params, requiredFields))
        status = 400
    else:
        #Query for Product
        if(reactionFields.get("post_id") != None):
            reaction = models.Reaction.query.filter_by(post_id=reactionFields["post_id"]).first()
            while(reaction is not None):
                models.db.session.delete(reaction)
                reaction = models.Reaction.query.filter_by(post_id=reactionFields["post_id"]).first()
        elif(reactionFields.get("user_id") != None):
            reaction = models.Reaction.query.filter_by(user_id=reactionFields["user_id"]).first()
            while(reaction is not None):
                models.db.session.delete(reaction)
                reaction = models.Reaction.query.filter_by(user_id=reactionFields["user_id"]).first() 
        
        models.db.session.commit()
        response["message"] = "Reaction successfully removed"
        status = 200

    return jsonify(response), status