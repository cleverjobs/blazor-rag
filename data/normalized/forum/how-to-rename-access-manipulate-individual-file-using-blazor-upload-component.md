# How to rename / access / manipulate individual file using Blazor Upload Component

## Question

**Ste** asked on 24 Nov 2024

Hi, Hi I am writing an app where user can upload files (multiple at once) and each file will have custom data attached to it. How do I access individual files and attach custom data to each file once I load them into the select file grid? Almost like a SelectedItem event in a grid where I can access the individual files which I click on it. I can use the OnUpload and OnSelect to send custom data and look through all the files but They aren't bind to the individual file. Example, I have data like a description for each individual files that I want to send with it when I upload and write to the database. How do I bind that data to the file?

## Answer

**Nadezhda Tacheva** answered on 25 Nov 2024

Hi Steven, You can indeed use the OnSelect and OnUpload events to send custom data or rename a file. It is not, however, possible to send custom data bound to the individual file - the attached request data is one whole piece. The Upload always makes a separate call to the controller for each file. So, your options are: Send custom meta data for all files with every request, for example, as a serialized Dictionary<> or any other object type. Then, deserialize the object in the controller and find the correct meta data for the currently received files in the controller method. Set Multiple="false", so that users can upload files one by one. Regards, Nadezhda Tacheva Progress Telerik
