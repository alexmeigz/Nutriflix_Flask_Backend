from flask import jsonify
from models import models
from controllers import base_controller
import time, datetime

# def add_test_data():
#     products = ["Avocado Toast", "Vanilla French Toast", "Lobster and Filet", "Cha Siu Chicken Wings", 
#                 "Smoked Salmon Salad"]
#     for i in range(1000, 1100):
#         product = models.Product(
#             vendor_id=i,
#             name=products[i%5],
#             subscription=i%2,
#             price=i%19,
#             list_date=datetime.date.today()
#             )
#         models.db.session.add(product)
#     models.db.session.commit()
#     return {}, 200

def create(params): 
    #Initialize
    response = {}
    requiredFields = ["user_id", "restName", "vendorType", "reason"]
    optionalFields = ["busLocation"]
    allFields = requiredFields + optionalFields
    applFields = {}

    #Check for Required Fields
    for field in requiredFields:
        if params.get(field, None) == None:
            response["message"] = "Missing Required Parameters: {}".format(requiredFields)
            status = 400
            return jsonify(response), status
        applFields[field] = params.get(field, None)
        
    #Check for Optional Fields
    for field in optionalFields:
        if field == "frequency":
            applFields[field] = params.get(field, 0)
        else:
            applFields[field] = params.get(field, None)

    #Check for Invalid Parameters
    if base_controller.verify(params, allFields): 
        response["message"] = "Request has invalid parameter {}".format(base_controller.verify(params, allFields))
        status = 400
    else:
        #Check for Numerical Price and Frequency
        try:
            applFields["user_id"] = int(applFields["user_id"])
        except:
            response["message"] = "Request has incorrect parameter type"
            status = 400
            return jsonify(response), status

        #Add Product to Database
        application = models.Application(
            user_id=applFields["user_id"],
            restName=applFields["restName"],
            busLocation=applFields["busLocation"],
            vendorType=applFields["vendorType"],
            reason=applFields["reason"],
            applsDate=datetime.date.today()
            )
        models.db.session.add(application)
        models.db.session.commit()
        response["message"] = "Application sent successfully!"
        status = 200
  
    return jsonify(response), status

def show(params):
    #Initialize
    response = {}
    requiredFields = ["id"]
    optionalFields = []
    allFields = requiredFields + optionalFields
    applFields = {}

    #Check for Required Fields
    for field in requiredFields:
        if params.get(field, None) == None:
            response["message"] = "Missing Required Parameters: {}".format(requiredFields)
            status = 400
            return jsonify(response), status
        applFields[field] = params.get(field, None)
        
    #Check for Optional Fields
    for field in optionalFields:
        applFields[field] = params.get(field, None)

    #Check for Invalid Parameters
    if base_controller.verify(params, allFields): 
        response["message"] = "Request has invalid parameter {}".format(base_controller.verify(params, allFields))
        status = 400
    else:
        #Query for Application
        application = models.Application.query.filter_by(id=applFields["id"]).first()
        
        if application is not None:
            #Query Successful
            response["id"] = application.id
            response["restName"] = application.restName
            response["user_id"] = application.user_id
            response["vendorType"] = application.vendorType
            response["applsDate"] = str(application.applsDate)
            response["busLocation"] = application.busLocation
            response["reason"] = application.reason
            status = 200
        else:
            #Query Unsuccessful
            response["message"] = "Application cannot be found"
            status = 200

    return jsonify(response), status

def display_all():
    applications = models.Application.query.all()
    response = {}
    for application in applications:
        response[application.id] = {
            "applsDate": str(application.applsDate),
            "busLocation": application.busLocation,
            "application_id": application.id,
            "user_id": application.user_id,
            "restName": application.restName
            "reason": application.reason
            "vendorType": application.vendorType
        }
    status = 200
    return jsonify(response), status

def update(params):
    #Initialize
    response = {}
    requiredFields = ["user_id", "restName", "vendorType", "reason"]
    optionalFields = ["busLocation"]
    allFields = requiredFields + optionalFields
    applFields = {}

    #Check for Required Fields
    for field in requiredFields:
        if params.get(field, None) == None:
            response["message"] = "Missing Required Parameters: {}".format(requiredFields)
            status = 400
            return jsonify(response), status
        applFields[field] = params.get(field, None)

    #Check for Optional Fields
        for field in optionalFields:
            applFields[field] = params.get(field, None)

    #Check for Invalid Parameters
    if base_controller.verify(params, allFields): 
        response["message"] = "Request has invalid parameter {}".format(base_controller.verify(params, allFields))
        status = 400
    else:
        #Query for Product
        application = models.Application.query.filter_by(id=applFields["id"]).first()     

        if application is not None:
            #Check for Numerical Price and Frequency
            try:
                applFields["user_id"] = int(applFields["user_id"])
            except:
                response["message"] = "Request has incorrect parameter type"
                status = 400
                return jsonify(response), status

            #Update application
            application.restName = applFields["restName"]
            application.user_id = applFields["user_id"]
            application.vendorType = applFields["vendorType"]
            application.busLocation = applFields["busLocation"]
            models.db.session.commit()
            
            #Query Successful
            response["message"] = "Application successfully updated"
            status = 200
        else:
            #Query Unsuccessful
            response["message"] = "Application cannot be found"
            status = 200

    return jsonify(response), status

def delete(params):
    #Initialize
    response = {}
    requiredFields = ["id"]
    optionalFields = []
    allFields = requiredFields + optionalFields
    applFields = {}

    #Check for Required Fields
    for field in requiredFields:
        if params.get(field, None) == None:
            response["message"] = "Missing Required Parameters: {}".format(requiredFields)
            status = 400
            return jsonify(response), status
        applFields[field] = params.get(field, None)
        
    #Check for Optional Fields
    for field in optionalFields:
        applFields[field] = params.get(field, None)

    #Check for Invalid Parameters
    if base_controller.verify(params, allFields): 
        response["message"] = "Request has invalid parameter {}".format(base_controller.verify(params, allFields))
        status = 400
    else:
        #Query for Product
        application = models.Application.query.filter_by(id=applFields["id"]).first()
        
        if product is not None:
            #Query Successful
            models.db.session.delete(application)
            models.db.session.commit()
            response["message"] = "Application successfully removed"
            status = 200
        else:
            #Query Unsuccessful
            response["message"] = "Application cannot be found"
            status = 200

    return jsonify(response), status