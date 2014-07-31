#
#
# copow routings
# 
# Standard is RESTful:
#
# meaning a call to domain:port/controller/([someting]+)
#   Where something is usually an ID
#   HTTP get        => will call controller.show(something)
#   HTTP POST       => will call controller.create(something)
#   HTTP PUT        => will call controller.edit(something)
#   HTTP DELETE     => will call controller.delete(something)
#   and a call to domain:port/controller/
#   Where something is usually an ID
#   HTTP get        => will call controller.list()
#   HTTP POST       => will call Nothing, yet.
#   HTTP PUT        => will call controller.replace_all() [empty by degfault]
#   HTTP DELETE     => will call controller.delete_all()
#
# 

import #APPNAME.controllers.welcome_controller
import #APPNAME.controllers.login_controller
import #APPNAME.controllers.logout_controller
import #APPNAME.controllers.error_controller


# default RESTful routes 
#  #controller will be replaced by the controllername for any controller in ./controllers
#  #controller_cls will be replaced by the actual class like:
#    .#APPNAME.controllers.controllername_python.ClassName

rest_routes = [
        (r"/#controller/echo"                           ,     ("#controller_cls", dict(  method_get="echo", 
                                                                                        method_post=None, 
                                                                                        method_put=None, 
                                                                                        method_delete=None, 
                                                                                        params=[]))
        ),
        (r"/#controller(?:/([0-9]*))?"                  ,     ("#controller_cls", dict(  method_get="list", 
                                                                                        method_post=None, 
                                                                                        method_put=None, 
                                                                                        method_delete=None, 
                                                                                        params=["page"]))
        ),
        (r"/#controller/create"                         ,     ("#controller_cls", dict(  method_get="create_form", 
                                                                                        method_post=None, 
                                                                                        method_put="create", 
                                                                                        method_delete=None, 
                                                                                        params=[]))
        ),
        (r"/#controller/([0-9a-zA-Z]+)"                 ,     ("#controller_cls", dict(  method_get="show", 
                                                                                        method_post="update", 
                                                                                        method_put="create", 
                                                                                        method_delete="delete", 
                                                                                        params=["id"]))
        ),
        (r"/#controller/([0-9a-zA-Z]+)/update"          ,     ("#controller_cls", dict(  method_get="update_form", 
                                                                                        method_post="update", 
                                                                                        method_put=None, 
                                                                                        method_delete=None, 
                                                                                        params=["id"]))
        )
]

# Add your routes below.
# Details about formatting routes can be found in the documentation

# www.pythononwheels.org/copow/documentation/routes
handlers = [
        (r'/welcome',           #APPNAME.controllers.welcome_controller.WelcomeController),
        (r'/features',          #APPNAME.controllers.welcome_controller.WelcomeController),
        (r'/next-steps',        #APPNAME.controllers.welcome_controller.WelcomeController),
        (r'/twitter',           #APPNAME.controllers.welcome_controller.WelcomeController),
        (r'/login',             #APPNAME.controllers.login_controller.LoginController,
                                dict(   method_get="show", 
                                        method_post="check_login", 
                                        method_put=None, 
                                        method_delete=None, 
                                        params=["email", "password"])

                ),
        (r'/logout',            #APPNAME.controllers.logout_controller.LogoutController,
                                dict(   method_get=None, 
                                        method_post="logout", 
                                        method_put=None, 
                                        method_delete=None, 
                                        params=[])
                ),
        (r'/',                  #APPNAME.controllers.welcome_controller.WelcomeController),
        #
        # REST Handling via Dispatcher
        #
        #(r'/(w+)/', #APPNAME.controllers.dispatch_controller.DispatchController),
        #(r'/(w+)/([0-9]+)', #APPNAME.controllers.dispatch_controller.DispatchController),
        #
        # Anything else => ERROR
        #
        (r'.*', #APPNAME.controllers.welcome_controller.WelcomeController)
        ]