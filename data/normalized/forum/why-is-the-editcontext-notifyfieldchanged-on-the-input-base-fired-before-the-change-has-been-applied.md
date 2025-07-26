# Why is the EditContext.NotifyFieldChanged on the input base fired before the change has been applied?

## Question

**Mat** asked on 27 Jun 2024

Hello, I am trying to check some custom validation when a value is adjusted on a TelerikForm. And I am using EditContext.OnFieldChanged +=HandleFieldChanged; But the value is still the old value, it looks like the TelerikInputBase is firing the notification before the change is actually applied. private protected void TriggerChange(T value)
{
if (this.ValidateOn==ValidationEvent.Change)
this.CascadedEditContext?.NotifyFieldChanged(this.FieldIdentifier);
this.OnChange.InvokeAsync((object) value);
} Is there a better way to be doing this? I do not want to have to add the validation check on every input OnChange. I have also tried OnFormUpdate with the same issue, this is the function I am using where EditContext still has the old values protected async Task OnFormUpdate(FormUpdateEventArgs args)
{
if (!IsUpdating)
{
IsUpdating=true;
DataHasChanged=true;
var type=args.Model.GetType();
var property=type.GetProperty(args.FieldName);
if (property !=null)
{
if (property.GetCustomAttributes(typeof(SkipMessageCheckAttribute), true).FirstOrDefault() is not SkipMessageCheckAttribute)
{
await CheckMessagesAsync();
}
}
IsUpdating=false;
}
DataIsValid=!EditContext.GetValidationMessages().Any() && Messages.All(m=> m.Priority !=PageMessagePriority.Error);
} Thanks, Matt

## Answer

**Radko** answered on 02 Jul 2024

Hi Matt, When using the OnUpdate event, the developer should rely on the values provided from the FormUpdateEventArgs. I tested the example just below the documentation and was not able to reproduce the error you are referring to with the event yielding stale data. If you are still encountering issues, perhaps sending a repro example through REPL would be best, as we will be able to then examine the exact use-case. Regards, Radko Progress Telerik
