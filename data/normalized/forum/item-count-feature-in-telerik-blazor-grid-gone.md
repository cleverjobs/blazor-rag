# Item Count Feature in Telerik Blazor Grid Gone?

## Question

**And** asked on 10 Jul 2023

I just recently upgraded to Telerik 4.3 and after working through the breaking changes, I found that the item count in the bottom right corner of the grid has been removed. How can I reenable this feature for my grid? I have attached a screenshot to reference the feature I am referring to...

## Answer

**Yanislav** answered on 13 Jul 2023

Hello Andy, I created a REPL example to test the Grid appearance. On my side, the pager label is displayed correctly. That being said may I ask you to inspect the DOM and confirm if the Pager label is being rendered? A possible reason for the pager label not being displayed could be a custom style that is affecting the appearance of the Grid/Pager. Please perform the necessary checks. If you are still unable to identify the cause of the issue, could you provide an example or modify the REPL sample so that the problem can be reproduced? By reproducing the problem locally, I will be able to investigate it and attempt to find a possible solution. Thank you for your cooperation in advance! Regards, Yanislav
