# Upload and display image on form

## Question

**Jon** asked on 02 May 2020

Hi Are there any samples/ideas of how to - uploading an image and then displaying the image on a form? I'm trying to upload and image to CosmosDB and then show the uploaded image on a form. thx in advance

## Answer

**Marin Bratanov** answered on 04 May 2020

Hi Jonathan, You can use the OnSuccess event to know when a file is uploaded, so you can trigger logic on the view that will display the image. For example, have a data collection that keeps the info about the uploaded files in the view (similar to our overview demo ) and render images for them once they are uploaded (e.g., add another flag to the file descriptor model). You can even send some additional information from the server (e.g., some ID from the database that you can use in the src attribute of the <img /> tag to point it to the correct handler). Regards, Marin Bratanov

### Response

**Jonathan** answered on 09 May 2020

How do you load the file into a FileStream... so I can write to a BLOB thx again

### Response

**Marin Bratanov** answered on 11 May 2020

Hi, You can see an example way of writing a file to a stream in the following controller: [https://docs.telerik.com/blazor-ui/components/upload/overview.](https://docs.telerik.com/blazor-ui/components/upload/overview.) Generally, it is up to the particular endpoint to handle the file and any underlying data storage (be that a file system, database, cloud or something else). For example, a .NET Core API would receive the file as an IFormFile that exposes a couple of methods for working with streams: [https://docs.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.http.iformfile?view=aspnetcore-3.1.](https://docs.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.http.iformfile?view=aspnetcore-3.1.) Regards, Marin Bratanov
