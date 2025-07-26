# Copy and Paste a Date

## Question

**Rog** asked on 31 Jul 2020

Can the DatePicker allow copy and pasting of a date such as "7/31/2020"?

## Answer

**Svetoslav Dimitrov** answered on 03 Aug 2020

Hello Roger, Allowing the paste into the DatePicker would have a lot of cases to control and that is why we have not yet enabled it. If the format is M/d/yyyy, for example, validation for numbers lower or equal to 12 would not be possible when the month is regarded. If the user pastes 8/2/2020 could mean two things - 8th of February 2020 or 2nd of August 2020. This might cause issues as the data that goes to the database might be incorrect and causing the application to misbehave. That being said, how would you suggest handling the pasting of dates in the component. How would you like from us to handle the format difference of the dates? I am waiting for your feedback on the topic. Regards, Svetoslav Dimitrov

### Response

**Shailendrasinh** answered on 25 Mar 2021

Hi Steve, Can we do that? I am also facing the same issue right now.. Can we consider that as "MM/dd/yyyy" and convert into the date format which the datepicker supposed to match? Thanks,

### Response

**Svetoslav Dimitrov** answered on 30 Mar 2021

Hello Shailendrasinh, We have an open feature request for pasting a date with the same format. I have given your Vote for it and you can Follow it to receive email notifications on status updates. In the public thread, you can find more information on the current situation and why we did not provide it already. Regards, Svetoslav Dimitrov Progress Telerik
