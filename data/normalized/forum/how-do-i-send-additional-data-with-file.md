# How do I send additional data with File

## Question

**Joh** asked on 18 Jun 2021

I have a Blazor server app which I am using to upload photos. I am attempting to use the Window and Upload components to have a modal dialog. It is unclear to me from the examples WHEN does the Upload component attempt to call the API Controller. Also, I need to specify exactly where to place the uploaded picture. I have a special folder off the root for photos and folders within that to "group" the photos. How do I pass the "group" to the controller from the Upload component? Eventually, this app will be used on tablets and phones and I will want to upload from the device storage OR from the camera. I don't see anything related to that.

## Answer

**Marin Bratanov** answered on 19 Jun 2021

Hello John, To each distinct question I see: When the API controller is called - by default, as soon as the user selects the file. You can make that happen on a click of a button by setting the AutoUpload parameter to false. Where to store the files - this is entirely up to the controller code. It defines what to do with the files and where to save them. How to pass the group to the controller - you can add metadata to the files through the OnUpload event (see the second sample). Touch devices with a camera - once the user taps the Select button their browser will show the native OS file selection options, and camera-enabled systems should have a camera option there. This is OS dependent and also depends on the permissions their browser has been granted, and is not something the web app can control. Regards, Marin Bratanov

### Response

**John** commented on 20 Jun 2021

I may have been slightly unclear in my description of "grouping". I have a base folder wwwroot\ClientImages to which I want to upload a file. However, I want to upload the file to a subfolder of ClientImages to be determined at the time the file is selected. i.e. I pick a folder ("Fathers Day 2021") from a dropdown and the file(s) I select should go to that folder. I want to send the folder selection along with the file(s).

### Response

**Svetoslav Dimitrov** commented on 23 Jun 2021

Hello John, The Telerik UI for Blazor Upload component provides a "connection" between the UI of the application and the backend. It sends the file to the controller/API and the latter control where the file will be actually saved. If I misunderstood the question, could you provide some more details on what behavior you are expecting from the component.

### Response

**John** commented on 26 Jun 2021

All good. After checking out the link for OnUpload event, it gave me ideas and they worked.
