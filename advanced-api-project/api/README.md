The ListView accepts user request, enables both authenticated and unauthenticated users get data of all books from database which is the GET method, using the BookSerializer class defined to serialize the django models objects to json file for user as response.

The DetailView accepts user request, enables both authenticated and unauthenticated users retrieve each book data with the respective id from the database which is the GET method, using the BookSerializer class defined to serialize the django models objects to json file for user as response.

The CreateView accepts user request, enables only authenticated users to create a book which is the POST method, using the BookSerializer class defined to serialize the django models objects to json file then validate the update, and save to database.

The UpdateView accepts user request, enables only authenticated users to update a book data with the respective id, which is the PUT/PATCH method, using the BookSerializer class defined to serialize the django models objects to json file then validate the update, and save to database.

The DeleteView accepts user request, enables only authenticated users to delete a book data with the respective id, which is the DELETE method, using the BookSerializer class defined to serialize the django models objects to json file then delete the data.
