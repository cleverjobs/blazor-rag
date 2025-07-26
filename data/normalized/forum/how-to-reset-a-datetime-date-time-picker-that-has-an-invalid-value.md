# how to reset a datetime/date/time picker that has an invalid value?

## Question

**Cha** asked on 29 Oct 2024

Let's say we have a DateTimePicker two-way bound to a DateTime? value: <TelerikDatePicker @bind-Value="searchCriteria.specificDate" ShowClearButton="true"></TelerikDatePicker> public DateTime? specificDate {get; set; } The user enters an invalid value, such as 1/d/yyyy. How do you reset it programmatically? Assigning the bound value to null doesn't do anything, as it's already null. I don't see a reset method anywhere? It'd be nice if there was a way to programmatically call whatever is called when the user clicks on the ClearButton. Thanks. p.s. This probably applies to all the date/time picker variations.

## Answer

**Dimo** answered on 30 Oct 2024

Hi Charles, Currently you can reset the DateTimePicker value by changing it twice with a small delay in-between, which triggers a UI refresh. On a side note, can you describe what is the scenario, which requires resetting the picker programmatically? Normally, the user should notice the invalid state and either enter a valid value, or ignore the invalid state, or press the Clear button. <TelerikDatePicker @bind-Value="@DValue" Width="200px" ShowClearButton="true" /> <TelerikButton OnClick="@ResetDatePicker"> Reset DatePicker </TelerikButton> @code {
private DateTime? DValue { get; set; }

private async Task ResetDatePicker ( ) {
DValue=new DateTime( 1, 1, 1 ); await Task.Delay( 1 );
DValue=null;
}
} Regards, Dimo Progress Telerik

### Response

**Charles** commented on 30 Oct 2024

It's common practice on forms to have a "reset" button that puts all controls back to their default value. I'll implement this. Still, it would be useful to have a .Reset method instead of a kludge. Thanks, Charles

### Response

**Dimo** commented on 31 Oct 2024

Aha. In that case, resetting the Form by resetting the model instance will produce the desired result as well. On a side note, I will raise a discussion about this scenario with the team. @using System.ComponentModel.DataAnnotations

<TelerikForm Model="@Employee" Width="300px"> <FormValidation> <DataAnnotationsValidator> </DataAnnotationsValidator> <TelerikValidationSummary /> </FormValidation> <FormButtons> <TelerikButton> Submit </TelerikButton> <TelerikButton ButtonType="@ButtonType.Reset" OnClick="@OnFormReset"> Reset </TelerikButton> </FormButtons> </TelerikForm>

@code {
private Person Employee { get; set; }=new ( ) { FirstName="initial first name" };

private void OnFormReset ( ) {
Employee=new ( ) { FirstName="initial first name" };
}

public class Person {
[Required]
public string FirstName { get; set; }=string.Empty;

[Required]
public string LastName { get; set; }=string.Empty;

public DateTime? BirthDate { get; set; }
}
}

### Response

**Charles** commented on 31 Oct 2024

Thanks. I'll try that as well. It's clear that function/method already exists in the control, as it's triggered when the user clicks the clear X button. You should be able to just make it publicly accessible?
