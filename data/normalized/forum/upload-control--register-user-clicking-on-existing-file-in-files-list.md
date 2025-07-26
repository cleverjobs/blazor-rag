# Upload Control- register user clicking on existing file in Files list?

## Question

**Bil** asked on 22 Aug 2023

Hello, Is there a way to fire an event (or listen to an existing one) for the Upload control when the user clicks on a file that has been added to the Files list of the Upload control? I'm populating the list of pre-existing files for records and I'd like to be able to let the user download them. Thanks

## Answer

**Dimo** answered on 25 Aug 2023

Hello Bill, Click events will be supported out-of-the-box when we implement a file list item template. In your case, you will need one of the following: Use your own JavaScript click handlers for our file list. Hide the built-in file list with CSS and implement a custom one, that is populated with the help of the Upload events (see related links in the feature request above). Use a custom UI for the initial files (e.g. ListView) and the built-in file list for the newly uploaded files. Regards, Dimo Progress Telerik
