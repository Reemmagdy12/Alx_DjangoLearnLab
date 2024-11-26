I made some views for the Book model like:
BookCreateView to create an instance of that model 
BookListView to retrieve all the instances of that model 
BookUpdateView to update instances of the model 
BookDetailView to view the details of an instance of the model 
BookDeleteView to delete instances of the model 

I have also extended the Bookcreateview with a customized function called create to make sure that the instance created does not already exists 

I added some permissions using the rest framework like is authemticated and allow any.

I have implemented in my BookListView a filter called BookFilter so the user could filter the instances by title, author and publication_year 
I have also implemented both of the search and ordering filters so the user could search and order the instances based on some predefined fields 