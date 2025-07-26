# How to upload a document to sharepoint library (using CSharp and not javascript) with Telerik/Blazor UI widgets etc.

## Question

**sco** asked on 27 Jul 2023

How to upload a document to sharepoint library (using CSharp and not javascript) in a Telerik/Blazor UI.. For various reasons we can no longer use the older Telerik / Javascript interface to Sharepoint to do this After research think the only way to do this is to interface to MicrosoftGraph using CSharp, Telerik/Blazor widgets but I cannot find a good working example. Does anyone have a link to a good working example. Thanks in advance for your help! Scott

### Response

**Dimo** commented on 31 Jul 2023

Does Sharepoint accept file uploads via HTTP? If yes, then you can use the built-in Upload component inside the FileManager. It supports all events of the standalone Upload component, and you can also send custom authentication or meta data with the file. If not, then you can't use our Upload component, or at least not directly. You can consider our FileSelect or Upload components to send the user file to the Blazor app, and then transfer the file to Sharepoint via any valid technique, which Sharepoint supports.
