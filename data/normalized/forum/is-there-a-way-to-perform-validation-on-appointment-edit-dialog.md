# Is there a way to perform validation on appointment edit dialog?

## Question

**Kev** asked on 27 Apr 2023

On the appointment edit dialog I would like to validate the Title field(see screenshot below) without having to do it in the OnCreateHandler or OnUpdateHandler. I have tried validation in these events, but it closes the dialog and I have to re-enter the data once again. I would like to not have to enter the data over again in case a title gets duplicated inadvertently. So my question is: is there a way to assign validation to the input fields?

## Answer

**Nadezhda Tacheva** answered on 02 May 2023

Hi Kevin, By design, the Scheduler supports built-in validation for the title, start and end times of the appointments. To add custom validation rules, you may use a custom edit form where you can assign the validation to the input fields. An example of such a configuration you may find here: [https://github.com/telerik/blazor-ui/tree/master/scheduler/custom-edit-form.](https://github.com/telerik/blazor-ui/tree/master/scheduler/custom-edit-form.) The sample app uses ValidationSummary to list the error messages in the custom edit form. If needed, you may add a different validation tool - for example, validation message. Note: we have a feature request for allowing DataAnnotations for scheduler appointments. This will let you specify the desired DataAnnotation rules in your model. If interested, you may vote for the request and follow it to get status updates. I hope you will find the above information useful to move forward with your application. Please let us know if any other questions appear. Regards, Nadezhda Tacheva Progress Telerik
