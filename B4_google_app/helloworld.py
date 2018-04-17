import webapp2
import os
from google.appengine.ext.webapp import template
from google.appengine.ext import db
# Declare your database models here
class Employee(db.Model):
    first_name = db.StringProperty()
    last_name = db.StringProperty()
    employee_dept = db.StringProperty()
    employee_salary = db.IntegerProperty()
    date = db.DateTimeProperty(auto_now_add=True)
    
#     content = db.StringProperty(multiline=True)
#     date = db.DateTimeProperty(auto_now_add=True)

# def comment_key():
#     return db.Key.from_path('comments_dir','default_comments_dir')

# 
class MainPage(webapp2.RequestHandler):
    def get(self):
        employee_query = Employee.all()
        employees = employee_query.fetch(10)
        template_values = {'employees':employees}
        path = os.path.join(os.path.dirname(__file__),'index.html')
        self.response.out.write(template.render(path, template_values))


class AddEmployee(webapp2.RequestHandler):
    def post(self):
        employee = Employee()
        employee.first_name = self.request.get('first_name')
        employee.last_name = self.request.get('last_name')
        employee.employee_dept = self.request.get('employee_dept')
        employee.employee_salary = int(self.request.get('employee_salary'))
        employee.put()
        self.redirect('/')
#         
app = webapp2.WSGIApplication([
('/',MainPage),
('/add',AddEmployee)
], debug=True)
     
if __name__=='__main__':
    app.run()