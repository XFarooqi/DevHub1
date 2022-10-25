# from flask import Blueprint, render_template
# from flask_login import login_required, current_user
# import smtplib, os, uuid
# from flask import render_template, request, session

# display = Blueprint('display', __name__)


# # return render_template('display.html')
# @display.route('/display')
# def display():
#     return render_template('display.html')  # This will show the display page



# @display.route("/form/<string:display>", methods=["GET", "POST"])
# def form(display):

#     """
# # This is the function that will be called when the user Select a template.
# Here we are starting a session for the user.

# While Methods are GET and POST.
# In GET method we can not send large amount of data and request parameter is appended into the URL
# In POST method we can send large amount of data and request parameter is appended into the body of the request.
# """

#     session["display_ses"] = display
#     return render_template("form.html")



# @display.route("/upload", methods=["GET", "POST"])
# def upload():

#     """
# This is the function that will be called when the user submits the form.
# Here we are setting the condition for the if statement.
# Like what will happen if user click on Design1 or Design2 or Design3.

# "display_name" varribale will store the information of that tmeplate and when user submit the information, all the information will be pass in the variables of this particaulr tempalte.
# """

#     display_upload = session.get("display_ses")
#     if display_upload == "design1":
#         display_name = "Design1.html"
#     elif display_upload == "design2":
#         display_name = "Design2.html"
#     elif display_upload == "design3":
#         display_name = "Design3.html"
#     elif display_upload == "design4":
#         display_name = "Design4.html"

#     if request.method == "POST":

#         # Here all the Values that user enter in form are assigned to the variables.

#         firstname = request.form.get("firstname")
#         lastname = request.form.get("lastname")
#         name = firstname + lastname
#         school = request.form.get("school")
#         college = request.form.get("college")
#         phone = request.form.get("phone")
#         email = request.form.get("email")
#         skill1 = request.form.get("skill1")
#         skill2 = request.form.get("skill2")
#         skill3 = request.form.get("skill3")
#         skill4 = request.form.get("skill4")
#         about = request.form.get("about")
#         img = request.form.get("img")


# # Assigning Ids to Images
#         key = uuid.uuid1()  # Creating A Unique Id
#         img = request.files["dp"]  # Getting the Image
#         img.save(f"website/static/images/{img.filename}")  # Saving the Image
#         img_new_name = f"{key}{img.filename}" # Renaming the Image with the Unique Id
#         os.rename(f"website/static/images/{img.filename}",  # Taking Orignal Image and Chaning its Name with the Unique Id
#                   f"website/static/images/{img_new_name}")

#     # # Email Generation
#     #     subject = "Congratulations!" + " " + firstname + \
#     #         "" + lastname  # Subject of the Email
#     #     body = "You will get the Working Link of You Website Shortly!"  # Messae of the Email
#     #     msg = f'Subject: {subject}\n\n{body}'
#     #     server = smtplib.SMTP("smtp.gmail.com", 587)
#     #     server.starttls()
#     #     # Setting the Login Access
#     #     server.login("arfarooqix@gmail.com", "qjxlzmkgjgglqkgp")
#     #     #server.login("Email", "Applcaiton Token from Gmail")
        

#     #     server.sendmail("arfarooqix@gmail.com", email, msg)  # Sending the Email


#     return render_template(display_name, t_fname=firstname, t_lname=lastname, school=school, college=college, phone=phone, email=email, skill1=skill1, skill2=skill2, skill3=skill3, skill4=skill4, about=about, img=img_new_name)




