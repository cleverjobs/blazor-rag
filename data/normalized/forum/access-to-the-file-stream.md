# Access to the File Stream

## Question

**aeh** asked on 23 Feb 2021

Is there a way to access the file stream of the file and not directly upload the file to an endpoint? I just need access to the stream to save the file to the database, not the server.

## Answer

**Svetoslav Dimitrov** answered on 24 Feb 2021

Hello Andy, We have an open Feature request regarding a FileSelect component. The main difference between them is that the Upload sends the file outside the Blazor application - to an endpoint (server) where you process the file as needed and save it to a database. The FileSelect will send the file in the Blazor app (in the application memory). At that point, you can access the file as a byte[] and you can use that as per your application needs. In the comments in the public thread, you can see some ideas on how to implement a custom FileSelect for the time being. If indeed the FileSelect is what you are looking for you can Vote for the feature request to raise the popularity of the item and Follow the thread to receive email notifications on status updates. Let me know if you need any further assistance. Regards, Svetoslav Dimitrov
