# Timezones in TelerikGantt

## Question

**duk** asked on 30 Mar 2023

Good day, can time zones be inserted in TelerikGantt? If I want to insert events only in certain working hours (for example, Monday to Friday from 6am to 10pm). If an event starts Friday at 9pm, it should be automatically extended to Monday (if the event lasts more than 1 hour). The function should be part of any Gantt by default, but I can't find a description for the definition of the ranges. Can you give me the path to the description or a short description on how to perform the described functionality? Thanks! Regards Paul

### Response

**Hristian Stefanov** commented on 03 Apr 2023

Hi Paul, As far as I can understand the desired functionality in this scenario is the following (please advise if I am missing something): Prevent the task drop on weekends - allow the user to drag tasks only on workdays but still display the weekends in the timeline. If that is the case, we have an open feature request for which you can vote: Ability to customize the drag/drop and resize step of the Gantt Timeline tasks. Once you are able to control the drag step, so the user can snap the tasks to the beginning of the day, you can easily restrict them from dropping the tasks on weekends. You can handle the OnUpdate event of the Gantt and only update the data if the user drops the task on a valid day (workday in your desired scenario). Let me know if this is what you are looking for or if the idea is different. I look forward to your reply. Kind Regards, Hristian

## Answer

**duktionsplanungIGP** answered on 04 Apr 2023

Hi, thanks for your respond. Unfortunately I need this feature asap in this month. When can I expect a final result for this feature? Please contact me by mail regarding the time and cost needed to implement the features quickly. Thank you very much. Best Regards Paul

### Response

**Hristian Stefanov** commented on 06 Apr 2023

Hi Paul, Thank you for getting back to me with feedback and notifying us of your urgency. As soon as I saw your latest response, I contacted our management to discuss a time and a cost to accelerate the feature implementation. As a result of the discussion, we found an even more suitable feature for your scenario - the ability to set a working week that will exclude the weekends. Here is what it looks like in jQuery: Working Week. I'm sharing one more sample via their dojo so you can explore the functionality: Dojo link. From a user experience point of view, it seems to look better than cutting the events. Please check out the above feature and consider if it will cover your needs or if you still prefer the other feature. Afterward, we can move on to propose an offer. I look forward to hearing your opinion. Kind Regards, Hristian
