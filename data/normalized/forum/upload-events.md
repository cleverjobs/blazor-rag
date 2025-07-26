# Upload Events

## Question

**aeh** asked on 26 Feb 2021

For uploads, the examples that are given have the controllers returning an empty results set. Is there an example of returning a custom result set back?

## Answer

**Marin Bratanov** answered on 26 Feb 2021

Hello, The second example in the OnSuccess handler shows how you can return information form the action (click the Controller tab there): [https://docs.telerik.com/blazor-ui/components/upload/events#onsuccess](https://docs.telerik.com/blazor-ui/components/upload/events#onsuccess) Here's the gist: event handler: async Task OnSuccessHandler ( UploadSuccessEventArgs e ) {
Console.WriteLine( $"File {e.Files[ 0 ].Name} has Status code: {e.Request.Status}, Custom message: { e.Request.ResponseText } " );
} action: return new OkObjectResult ( "some custom message" ); // new OkResult() sends an OK message without custom texts //return Content("response message"); // another way to return a custom message Regards, Marin Bratanov

### Response

**aehlert** answered on 01 Mar 2021

What I'm trying to do is return a filestream and some other values from the upload controller. In my app, I cannot save the file to disc yet because I do not have the key of the object that I am working with yet.

### Response

**Marin Bratanov** answered on 01 Mar 2021

Hi, I think what you are looking for is a FileSelect for Blazor, you can Follow that here: [https://feedback.telerik.com/blazor/1460649-fileselect-component.](https://feedback.telerik.com/blazor/1460649-fileselect-component.) The thread also offers guidance on how you can build one rather easily with some examples we have in our demos too. There are some more details on this in our previous discussion with you about this last week ( link ). We first made a component that solves the much harder task of an actual asynchronous file upload to an endpoint, and for Blazor there is a significant difference, with the file select giving you the files stream or byte[] immediately in your component, as opposed to sending a file to an endpoint for saving. An alternative path is to consider returning the path to the file (or other identifier) to the Blazor app from the endpoint. Then the event handler can use this to read the file stream from the server or do any other manipulation it needs with the file that the endpoint already saved - e.g., change its file name, or otherwise modify a database record. The benefit of that is that you may be able to avoid transmitting the file content two times over the wire (can be a massive problem for large files), and there won't be overhead of sending files over the SignalR connection. You could also include that key from the Blazor component together with auth information through the OnUpload event - so that the endpoint has all the info it needs immediately. Regards, Marin Bratanov
