# Telerik Scheduler - Hide "Repeat" options

## Question

**Mat** asked on 15 Dec 2023

Is there any way to dynamically hide the Repeat options on the Add Event dialog? We have a scenario where some users should be able to create recurring appointments, but other users should be restricted to creating "one-off" appointments only.

## Answer

**Georgi** answered on 18 Dec 2023

Hello, Mathew There is a feature request open for a Popup Form Template, which will allow you to customize the Popup Form. I have added your vote to it as this helps us prioritize based on community feedback. Additionally, you can follow the item in our feedback portal to get notified of status updates. In the meantime, there are two possible workarounds: Create a custom edit form - this sample project that demonstrates how to do this. Conditionally hide the Repeat options with a ternary operator and a:nth-child CSS pseudo-class like in this REPL example. The:nth-child pseudo-class is used because the number of fields inside the form does not change. Kind regards, Georgi Progress Telerik
