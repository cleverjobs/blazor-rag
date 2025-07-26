# Customize Edit Recurring Appointment Dialog

## Question

**Hol** asked on 01 Aug 2022

Hi, I have build a custom dialog for editting appointments. But if I double click a recurring appointment, the default edit recurring appointment dialog appears. In my OnEdit method, I have: args.IsCancelled=true But at the moment, the edit recurring appointment dialog appears, my custom OnEdit method is not yet invoked. How can I use a custom dialog for the selection of "edit series" and "edit current occurence"?

## Answer

**Kristian** answered on 03 Aug 2022

Hello Holger, As you already observed the OnEdit event is triggered once the user chooses from one of the options in the recurring dialog. At this point we don't support customizing the existing dialog. An existing workaround could be to disable the Edit functionality and trigger your custom Edit dialog on double click. That way you could have more than one custom edit dialogs and choose between them, depending on the clicked item. You can move even further and implement a similar recurrence editing dialog, but trigger your own forms from it. Alternatively, you can trigger the editing on a context menu click. Check the existing example for using a context menu for the scheduler appointment in this project: [https://github.com/telerik/blazor-ui/tree/master/scheduler/appointment-context-menu](https://github.com/telerik/blazor-ui/tree/master/scheduler/appointment-context-menu) There are two Feature Requests you can look at here, which will do this process a lot easier: - Differentiate "edit current occurrence" and "edit the series" in the RecurrenceDialog: [https://feedback.telerik.com/blazor/1522653-differentiate-edit-current-occurrence-and-edit-the-series-in-the-recurrencedialog](https://feedback.telerik.com/blazor/1522653-differentiate-edit-current-occurrence-and-edit-the-series-in-the-recurrencedialog) - Exposing the RecurranceEditor component. If you want to build a custom editing of the whole recurrence series, you may also follow this item: [https://feedback.telerik.com/blazor/1485984-expose-recurrenceeditor-component](https://feedback.telerik.com/blazor/1485984-expose-recurrenceeditor-component) I added your vote to both Feature requests. Regards, Kristian

### Response

**Holger** commented on 04 Aug 2022

Thank you for you reply. I get it working with the link to the first feature request. But how do I identify on which recurrent event the user clicked? I only have the event object. The only difference in the generated html is the data-render-id (and the content of course). With the OnDoubleClick Event, there is no click-source or similar. Finally I got the event from the double click event.

### Response

**Holger** answered on 09 Aug 2022

I got it to work with the solution in the link you provided. Thanks for that. This solution clicks the "edit current occurence" button with javascript and I can use my own methods. But this solution works only on the OnDblClick event. Now I have to do the same for editing the event by drag'n drop. If the user drags a recurring event, the build-in dialog for choosing to edit the series or the current event occurs. In this case I want the same behavior as on double click. I triey it with ondragend, ondragleave, ondrop on the same element (div) as the working ondblclick event, but It seems none of them is fired. How can I set the args.IsCancelled=true if the user drags the event?

### Response

**Svetoslav Dimitrov** commented on 09 Aug 2022

Holger, We have an open feature request for the Drag and Drop events in the Scheduler. They are coming with our next release (3.6.0). The 3.6.0 is due by the 14th of September 2022. Once this feature is exposed you will be able to achieve the desired functionality.
