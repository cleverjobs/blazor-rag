# I want to override on AllowCreate, How to override this method in TelerikSchedule?

## Question

**sud** asked on 12 Jul 2022

When AllowCreate="true", its automatically opened own appointment addDialog?. I want Stop that and want move custom page(My own page). Please help me! Thank You!.

## Answer

**Dimo** answered on 14 Jul 2022

Hi Sudath, Here is how to use a custom Scheduler edit form. Regards, Dimo Progress Telerik

### Response

**Emmanuel** commented on 21 Oct 2024

This is not sufficient because for the modification part, using the combination of... void EditHandler ( SchedulerEditEventArgs args ) {
args.IsCancelled=true; //prevent built-in edit form from showing up AppointmentDto item=args.Item as AppointmentDto;
CustomEditFormShown=true; if (!args.IsNew) // an edit operation, otherwise - an insert operation {
FormAction=EnumActions.Update;
CurrentAppointment=item.ShallowCopy();
} else {
FormAction=EnumActions.Create;
CurrentAppointment=new AppointmentDto() { Start=args.Start, End=args.End, IsAllDay=args.IsAllDay };
}
} and the js hack function clickSchedulerPromptButton ( btnIndex ) { setTimeout ( function ( ) { var buttons=document. querySelectorAll ( ".k-window-content .text-right button" ); if (buttons && buttons. length>=btnIndex) { var chosenButton=buttons[btnIndex];
chosenButton. click ();
}
}, 50 );
} <ItemTemplate> @{var appointment=context as AppointmentDto;} <div style="padding: 10px;" title="" @ondblclick="@( ()=> ChooseEditMode(appointment) )"> </div> </ItemTemplate> async void ChooseEditMode ( AppointmentDto appt ) { // check if we have a recurring appointment or a member of one if (appt.RecurrenceId !=null || ! string.IsNullOrEmpty(appt.RecurrenceRule))
{ int btnIndexToClick=1; //the first button - edit instance // make it 1 for the second button - the series await _jsInterop.InvokeVoidAsync( "clickSchedulerPromptButton", btnIndexToClick);
}

} This works when the user double-clicks on an event (having made sure to manage the choice between editing a series or an occurrence in the custom edit form). However, if the scheduler is configured with AllowUpdate, another path for event modification opens up, which is resizing events with the mouse. The problem is that the OnEdit event is not triggered in this case; instead, the OnUpdate event is triggered, but only after the modification choice popup appears. The SchedulerUpdateEventArgs arguments do not carry the user's choice or the targeted occurrence date. As a result, it's not possible to modify an occurrence within a series this way, even though the popup gives the user the choice. Is this a bug or an oversight?

### Response

**Dimo** commented on 21 Oct 2024

@Emmanuel - review the recurrence-related properties of args.Item in the OnUpdate handler. Their values will show whether the user resized (modified) a particular recurrence instance, or the whole recurrence series. For example, if there are no (new) recurrence exceptions, it's the latter.
