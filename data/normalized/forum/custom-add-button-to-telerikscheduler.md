# Custom Add button to TelerikScheduler

## Question

**RobRob** asked on 02 Oct 2024

I don't like the "Default" behavior of adding items to TelerikScheduler ... there is NO visible UI cue for users on how to add an item to the schedule ... they have to be told to double click on a day, this is bad UI design. I realize I can just create my own Add button and manage adding of schedule items. BUT, I was wondering if Telerik offered a custom Add option either with the OnCreate or something else? Something along the lines of how Add is supported in TelerikGrid with GridToolBarTemplate and GridCommandButton?? Rob.

## Answer

**Nansi** answered on 04 Oct 2024

Hi Rob, A Scheduler toolbar template feature is scheduled for our next release in November. This feature will allow you to add custom tools to the toolbar, as in your case, an Add button. However, managing the adding of an appointment from the custom button will remain a matter of custom implementation. On the other hand, when it comes to the built-in way to create an appointment: Currently, the only built-in way to add an appointment is to double-click on an empty slot. We do not provide another custom option to add an appointment. However, to have an Add button in the toolbar as a built-in tool seems to me a valid use case. Can you share if this will meet your requirements? Additionally, would you like to prevent the current built-in way to add an appointment if you have a built-in Add button in the toolbar? Are there any other customization or requirements we need to consider? As you may know, we evaluate the feature requests and we take into consideration factors such as feasibility, development effort and the users' demand. If you share more information I will discuss this with the team. If we decide that this is a valid feature request, we can create a request in our feedback portal. Regards, Nansi Progress Telerik
