# DateOnly/TimeOnly support

## Question

**Ben** asked on 09 Dec 2021

Hi, I try tu use the new Date/TimeOnly types of .Net6 and they are not supported by the Telerik components (you cannot bind them to these types). I tested it on the 2.30.0 version you just released. It works fine with the Blazor Components (InputDate, input type="time"...) but it is not a practical solution for component like TelerikGrid (it would mean templating everything, breaking the inline validation etc.) or TelerikScheduler/Gantt (I would like to use a DateOnly for its Date property for example, and ideally its model could be a DateOnly and 2 TimeOnly instead of 2 DateTime but that's less important). Do you have an ETA for their support or a workaround? Also, is there documentation about the limitations of your .Net6 support so I don't have other bad surprises?

## Answer

**Svetoslav Dimitrov** answered on 14 Dec 2021

Hello Benoit, I have opened a new feature request on your behalf - Provide support for DateOnly and TimeOnly structs for the respective pickers. I have added your Vote for it and you will receive email notifications on status updates. Following the email notifications is the best way to know when the support for those structs will be available. The Grid, Gantt, Scheduler (and other more complex components) internally use the standard Telerik Pickers so supporting those structs for the pickers should automatically mean that the complex components would support them. On the topic of the other .NET6 limitations, I am not aware of other limiting factors at the time of writing this. Regards, Svetoslav Dimitrov
