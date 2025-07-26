# DatePicker Overflow Issue

## Question

**Ter** asked on 16 May 2025

We have a Blazor DatePicker in our web app to store the Date of Birth. The calendar popup seems to be working correctly. However, for the input portion, when typing in the year of the date, the content typed into the year overflows the input area for as long as the user types, instead of horizontally scrolling within the 4-digit year space. The interesting thing is that this is only happening to one of our client users. We have been unable to duplicate this either locally or in our Dev/Test environments. I'm assuming that, since the horizontal scrolling of the year entry is within the DatePicker widget, could this possibly be due to an environment issue with the Blazor library or maybe some setting within Microsoft Edge? I don't have as many details as I would like to have to share with you. At this time, I'm just trying to find out if you have ever heard of this issue before?

## Answer

**Hristian Stefanov** answered on 20 May 2025

Hi Terry, A bug report has already been submitted on our public feedback portal related to the described issue: [Blazor Server] When having higher latency, the value of the date inputs is incorrect. I voted for it on your behalf and raised the item's priority. You can also subscribe to it to receive email notifications for future status updates. Regards, Hristian Stefanov Progress Telerik
