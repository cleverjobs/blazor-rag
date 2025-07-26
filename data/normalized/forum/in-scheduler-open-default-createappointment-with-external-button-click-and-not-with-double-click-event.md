# In Scheduler, open default "CreateAppointment" with external button click and not with double click event

## Question

**n/an/a** asked on 20 Oct 2021

I would simulate the "DblClick" event that Telerik use to open the window with the "Create Appointment" default fields. I have a button in the page, outside the TelerikScheduler component, and I would like to create a new Appointment by there, using the default "CreateAppointment" Telerik window, obviously with tha "StartDate" and "EndDate" fields empty. A generic Appointment, in few words. Is there any way to do this? Where I can find the method that open that window? (I found this in the "kendo.all.min.js", but I am not sure if it is the right point where Telerik launch the method: t.trigger("add", {
eventInfo: f({
start: i.startDate(),
end: i.endDate()
}, o); if it is, how can I use it?) Thanks, Angelo Marzullo

## Answer

**Hristian Stefanov** answered on 25 Oct 2021

Hi Salvatore, Regarding the described scenario, we have opened on your behalf a feature request for Scheduler State on our Public Feedback Portal: Add State feature in the Scheduler With the State, you will be able to open a window "Create Appointment" with predefined or default fields and achieve the desired functionality. You will be able to control the add/insert/update operations in the Scheduler. We prioritize feature requests depending on interest. With your vote already added to the public item, the item's popularity is increased. Since you are the creator of this feature request, you are automatically subscribed to receive email notifications on status updates. In the meantime, I can confirm that we are not aware of any workarounds that can achieve the described functionality. Perhaps, if you want to trigger only the default "Create Appointment" window from a separated button, you can try using a custom Javascript function to catch the "DblClick" event from a cell. Thank you for raising a question that led to making the component better by adding a new feature request. Please let me know if you need any further information. Regards, Hristian Stefanov
