class Logging(object):

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization on start-up

    def __call__(self, request):
        # Logic executed on a request before the view (and other middleware) is called.

        """ After you modify (or not) the original request, you must turn over control to the view method in order for it to run. 
        This phase is triggered when you pass request to the self.get_response reference you set in the _init_ method. 
        This phase effectively says, "I'm done modifying the request, go ahead and turn it over to the view method so it can run." """
        response = self.get_response(request)
        
        # Logic executed on response after the view is called.

        # Return response to finish middleware sequence
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        # Logic executed before a call to view
        # Gives access to the view itself & arguments
        pass

    def process_exception(self, request, exception):
        # Logic executed if an exception/error occurs in the view
        pass

    def process_template_response(self, request, response):
        # Logic executed after the view is called,
        # ONLY IF view response is TemplateResponse
        return response
