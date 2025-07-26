# TelerikDatePicker value less then 1/1/1900 gives error in console.

## Question

**Kis** asked on 10 Nov 2021

Hi there, I have created the blazor app with Telerik. For the <TelerikDatePicker> i am using DateTime with nullable value. and this works fine. if we select the date from the datepicker then it is working as expected. When we try to enter the date manualy by keyboard. then it is giving the error if date is less then 1/1/1900. Not sure what i need to do. Can you help with this

### Response

**Kishan** commented on 12 Nov 2021

Please provide your response, I am eagerly waiting for your reply.

## Answer

**Svetoslav Dimitrov** answered on 15 Nov 2021

Hello Kishan, I have tested the scenario you are describing locally and I did not receive the error. From this REPL link, you can see a runnable code snippet of a form that has a custom editor (by the Template) and the DatePicker is bound to a nullable DateTime object. When I ran it both in VS and in REPL I could not reproduce the issue. Could you confirm the Telerik UI for Blazor version you are using? If the code snippet works for you as expected I would suggest you upgrade to the latest version of the product suite, at the time of writing this, 2.29.0, and test on this version. Regards, Svetoslav Dimitrov
