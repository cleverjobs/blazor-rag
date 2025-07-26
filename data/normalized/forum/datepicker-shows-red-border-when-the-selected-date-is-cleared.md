# DatePicker shows red border when the selected date is cleared

## Question

**Dom** asked on 22 May 2023

I have a DatePicker and a DateInput bound to the same nullable DateTime property (for behavior testing purposes). <TelerikDateInput @bind-Value="@TestDate" /> <TelerikDatePicker @bind-Value="@TestDate" /> public DateTime? TestDate { get; set; }=null; As it isn't a required field, the user can fill in the field and delete it afterwards (by selecting the full date and pressing the "Del" key). When this happens, the DateInput, in terms of layout behaves as if it has never been filled. On the other hand, the DatePicker shows a red border as if it was a required field that has yet to be filled in. Is there any way to not show the red border when the DatePicker is cleared?

## Answer

**Svetoslav Dimitrov** answered on 25 May 2023

Hello Domingos Portela, We have an open bug report that describes the issue you are facing - DatePicker should accept null value as valid when bound to nullable DateTime. I have added your Vote for it and you can click the Follow button to receive email notifications on status updates. In the public post, you can find a few workarounds until the bug is fixed. Regards, Svetoslav Dimitrov Progress Telerik
