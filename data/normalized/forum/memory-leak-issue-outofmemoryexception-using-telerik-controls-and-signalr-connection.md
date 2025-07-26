# Memory leak issue (OutOfMemoryException) using Telerik controls and SignalR connection

## Question

**Cla** asked on 04 Jun 2021

Hi, in our application we receive notification from server signalR connection and update some controls UI (typical progress bar and TextBox). I found an issue who generate an OutOfMemory exception when we loop to update ui with telerik controls. I have replied the issue with a demo project (see attachment). Note who i can reply the issue with this conditions: - Initialize a SignalR connection (initialized but unused..) - Use Telerik controls inside a EditForm (in the sample TelerikTextBox and TelerikNumericTextBox) To reply the issue i generate an infinite loop who raise an event, inside the event handler i simply update ui controls and call StateHasChanged(). Starting the loop it reach about 2GB of memory in about 90 seconds and then raise an outofmemory exception. If i replace TelerikTextBox/TelerikNumericTextBox with simple input control the memory grow up and remain stable to about 500MB without raising the OutOfMemory exception, so i think who garbage collector do his job. If i not initialize the SignalR connection, the memory leak does not occurs. Waiting for your reply. Thanks

## Answer

**Svetoslav Dimitrov** answered on 09 Jun 2021

Hello Claudio, Thank you for raising that issue to our attention. We were successfully able to see the OutOfMemory exception. I have awarded your account with Telerik Points as a small token of appreciation. That being said, I have opened a bug report on our public feedback portal on your behalf - OutOfMemory exception when an infinite loop updates the Telerik UI for Blazor components in an EditForm. I have given your Vote for it and you are automatically subscribed to receive email notifications on status updates. Having done that, our dev team will launch an investigation on why the components are not disposed of. The reason why our components use more memory than the standard HTML input is due to the added functionality. Regards, Svetoslav Dimitrov Progress Telerik

### Response

**Claudio** answered on 22 Jun 2021

Hi, after 2 weeks i noted the issue status is still not planned. This is a blocking bug for our project ui, we are unable to put a simple progress bar updated by SignalR response in a simple input form, cause the out of memory. Can we have a resolution date of the issue? Thanks

### Response

**Svetoslav Dimitrov** commented on 25 Jun 2021

Hello Claudio, I am sorry to read that this issue is blocking your entire application. Indeed, currently, the status of the issue is unplanned which would mean that this is a valid bug report and we are committed to working on its fix. The issue at hand, however, is not that easy to investigate properly so we might need some additional time. The best way to be notified of the status updates is to follow your email notifications. Currently, the workaround I can offer is to change the numeric textbox and the textbox with the standard Blazor or HTML input tags until this issue is fixed. Let me know if you need any further assistance.

### Response

**Giampaolo** commented on 21 Sep 2021

Hi Any news about this issue ?

### Response

**Radko** commented on 24 Sep 2021

Gi Giampaolo, This is an issue that is high on our list and is something that we will be working on in our next releases. It appears resources are allocated internally when validation occurs, which are then not released correctly. You can follow this thread for updates in regards to this specific issue - OutOfMemory exception when an infinite loop updates the Telerik UI for Blazor components in an EditForm Regards, Radko Stanev

### Response

**Claudio** answered on 04 Apr 2022

There is any update? after 10 months this issue is still unplanned: [https://feedback.telerik.com/blazor/1523129-outofmemory-exception-when-an-infinite-loop-updates-the-telerik-ui-for-blazor-components-in-an-editform?_ga=2.30533117.316947574.1649072879-885474183.1613480056](https://feedback.telerik.com/blazor/1523129-outofmemory-exception-when-an-infinite-loop-updates-the-telerik-ui-for-blazor-components-in-an-editform?_ga=2.30533117.316947574.1649072879-885474183.1613480056)

### Response

**Nadezhda Tacheva** answered on 07 Apr 2022

Hi Claudio, I've reached out to our development team to discuss the status of this issue. We agreed to add it to our parking lot as we see the demand is growing. An approximate ETA for its evaluation is 6 months. Regards, Nadezhda Tacheva Progress Telerik

### Response

**Coding Machine** answered on 09 Aug 2023

The issue still there in version 4.4.0 - memory is still leaking if you use TelerikTextBox If you replace it with HTML input - issue is gone. It seems TelerikTextBox control doesn't properly dispose hnadlers for DOM events - I see in dev tools of browser in Memory tab that TelerikTextBox actively raises some events while you are typing the text. HTML input (with Blazor @bind) raises sugnificantly less events. As this is the basic control - the issue is critical and should be found and fixed. I can imagine how huge memory leak could be when you use more complex UI controls from Teleking library...

### Response

**Svetoslav Dimitrov** commented on 14 Aug 2023

Hello Dmitry, Can you share with us your findings? Currently, when I have tested with the application provided by Claudio in the opening message, the issue is no longer reproducible. As memory leaks are very important to us, I will highly appreciate your help in reproducing the issue.
