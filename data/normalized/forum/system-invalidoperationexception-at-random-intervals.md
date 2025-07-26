# System.InvalidOperationException at random intervals

## Question

**Mau** asked on 21 Sep 2021

Hi, I have a grid and sometimes at random intervals I get an error "System.InvalidOperationException: TelerikValidationComponent requires a cascading parameter of type EditContext. You can use Telerik.Blazor.Components.TelerikValidationTooltip`1[System.Object] inside a EditForm or TelerikForm". This is during an edit/update of values. I use blazor server side net5.0 telerik ui for blazor 2.27

### Response

**Hristian Stefanov** commented on 24 Sep 2021

Hi Maurice, Indeed, this seems like strange behavior. We have fixed such a bug with the Grid in our 2.24.0 release. I tested with the Grid live demo which uses the latest version (2.27.0), and it seems the editing actions are working as expected. Can you please isolate the issue in a runnable sample project and send it to us? This will allow us to test the behavior and investigate the issue on our end. Thank you in advance! I look forward to receiving your reply.

### Response

**Maurice** commented on 24 Sep 2021

I have found the issue. What I have are a main grid which is updated and a loaded grid from another page <StillToWrite Date=" @DateDatePickerValue " @ref="_stillToWriteChild" /> At the end of the upgrade process of the main grid I send a refresh to the StillToWrite page with his own grid using if ( _stillToWriteChild!=null ) await _stillToWriteChild. RefreshMainGridOnClickHandler (); And this refresh fails due to, what I think, a mismatch in the timing. closed connection and then the update of this subgrid, Sometimes the closing of the connection is slower and the update of this subgrid is fast enough.

## Answer

**Hristian Stefanov** answered on 28 Sep 2021

Hi Maurice, Thank you for sharing how things turned out. It seems that you have found the issue. I'm glad to hear that. If you are still facing a problem and further investigation is needed, you can isolate the issue in a runnable project and send it for review. Regards, Hristian Stefanov Progress Telerik
