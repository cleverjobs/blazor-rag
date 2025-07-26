# Customize Events and TimeRange in Gantt Chart

## Question

**duk** asked on 10 Jan 2023

Hi, Is there a possibility to configure the events in Gantt by making the bars of the parent wider and inserting text, similar to the dependent events ? The second question is whether I can set the visualized start time in the Gantt and make it dependent on a variable. For example, by saying that by default the period is displayed from today, which fixes the "left border" with today's date. Thanks.

### Response

**Hristian Stefanov** commented on 13 Jan 2023

Hi Paul, Let me try going through the two questions below...Is there a possibility to configure the events in Gantt by making the bars of the parent wider and inserting text, similar to the dependent events ?.. Customizing the parent (summary) events will be possible as soon as we implement the Summary Task Template feature request. I voted there on your behalf and raised the priority. You can also subscribe to the item to receive email notifications for status updates. Currently, Gantt has a template only for the dependent events. In the meantime, if an alternative approach appears, I will post it as a comment at the above link...The second question is whether I can set the visualized start time in the Gantt and make it dependent on a variable... I assume that the desired result from the second question is to customize and use a variable in the date header. Currently, that is achievable through the Date Header Template. Please confirm if I understand correctly and if the date header is the part you want to change.=====Thank you. Kind Regards, Hristian

### Response

**duktionsplanungIGP** commented on 07 Feb 2023

Hello Hristian, Thank you very much for your comments last month. I was already able to implement part of it. The second question probably did not come across correctly in terms of content. Therefore a short description: Currently the view is apparently dependent on the start and end times of the events. I would like to have the current week always displayed in the weekly view, regardless of the events. Currently, I get the following screen as soon as I open the application (static data and static view as of 03.10.2022): I would like to have a dynamic view where, as soon as I start the application, it directly displays today's week (e.g. view of 06/02/2023). Quasi depending on the actual date, independent of the dates of the events: In addition, a bar showing the actual time per day, as exemplified in the picture, would actually be helpful. Does such a tool exist in a way? Thank you very much. Best Regards Paul

### Response

**Hristian Stefanov** commented on 10 Feb 2023

Hi Paul, Thank you for getting back to me with feedback. Regarding the desired functionality in Gantt, we have two feature requests: Ability to set selected date Current Time Marker The first one will allow you to select the current week on the initial load of the component. That way, the current week will always be displayed in the weekly view regardless of the events. The second feature request will allow you to show a vertical bar that tracks the actual time per day. I voted for both items on your behalf and raised the priority. In the meantime, if an alternative approach appears, I will create a comment with it on the public posts. You can also subscribe to them to receive email notifications for status updates. If we can assist with anything else, I would be glad. Kind Regards, Hristian
