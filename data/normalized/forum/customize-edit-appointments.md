# Customize Edit Appointments

## Question

**Jon** asked on 12 Apr 2020

Hi Is their anyway to make the Edit Appointments - ReadOnly - and remove the Save button. What about removing or changing the labels? thx in advance

## Answer

**Marin Bratanov** answered on 13 Apr 2020

Hello Jonathan, Unless you enable editing explicitly, appointments are read-only. You can enable only insertion, deletion or editing separately through properties: [https://docs.telerik.com/blazor-ui/components/scheduler/edit-appointments.](https://docs.telerik.com/blazor-ui/components/scheduler/edit-appointments.) You can also cancel the OnEdit event to prevent an appointment from being edited on a condition, effectively making it read-only. You can even show your own custom popup with information from that event (e.g., use a Window component ). We also have an example of this to make a custom edit form in our samples repo: [https://github.com/telerik/blazor-ui/tree/master/scheduler/custom-edit-form](https://github.com/telerik/blazor-ui/tree/master/scheduler/custom-edit-form) - this will let you have full flexibility on what you render. Finally, you can also change the labels through localization in your app while still using the built-in edit form: [https://demos.telerik.com/blazor-ui/scheduler/globalization.](https://demos.telerik.com/blazor-ui/scheduler/globalization.) If you don't save the user changes in OnUpdate, you will also effectively make an appointment read-only, although I feel it would be unpleasant user experience to edit their info and not have it saved. Of course, you could hide the Update button with CSS but the user would still have spent time updating fields only to lose the data. Regards, Marin Bratanov
