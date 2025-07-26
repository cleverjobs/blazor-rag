# Change SubmitButton Enabled State on TelerikForm by when form is modified

## Question

**Pet** asked on 04 May 2023

I am stuck with a problem that I just can't seem to solve: I have built a TelerikForm with a Submit button. The requirement is to change the enabled status of this button depending on whether the form has been modified or not. So the basic code is : <TelerikForm @ref="@FormRef" Model="@EntityModel" OnSubmit="@OnSubmitHandler"> <FormValidation> <DataAnnotationsValidator /> </FormValidation> <FormItems> <CascadingValue Name="TheForm" Value="@FormRef"> @foreach (var form_item in FormItemCollection)
{ <DynamicComponent Type="@form_item.ComponentType" Parameters="@form_item.Parameters" /> } </CascadingValue> </FormItems> <FormButtons> <TelerikButton ButtonType="@ButtonType.Submit" Enabled="@SaveEnabled" ThemeColor="primary"> Speichern </TelerikButton> </FormButtons> </TelerikForm> The ButtonShould be changed on the EditContext.IsModified() state. So I tried: protected override void OnAfterRender(bool firstRender)
{
if (firstRender)
{
FormRef.EditContext.OnFieldChanged +=EditContext_OnFieldChanged;
}
base.OnAfterRender(firstRender);
}

private void EditContext_OnFieldChanged(object sender, FieldChangedEventArgs e)
{
SaveEnabled=true;
StateHasChanged();
} But every time the StateHasChanged() is called, I lost the new values in the form cause it is rendered again with the previos values. I can't find any solution to change the State of the Button without StateHasChanged. The enabled attribute is not a bound value, so the state does not change. So how to solve this troubles?

## Answer

**Dimo** answered on 06 May 2023

Hello Peter, In general, StateHasChanged is required in this case, because the OnFieldChanged handler is not an EventCallback. By definition, Blazor does not update the UI automatically, unless an event handler is an EventCallback (such as a button click, value change, etc.) However, my test page works with StateHasChanged: [https://blazorrepl.telerik.com/mHEfuAOJ02G6v9qz24](https://blazorrepl.telerik.com/mHEfuAOJ02G6v9qz24) Here is another one with a child component and version 4.2.0: [https://blazorrepl.telerik.com/QxaJOKOz248AUedr08](https://blazorrepl.telerik.com/QxaJOKOz248AUedr08) So I have a few notes: You can (or should) detach the handler after first execution if it's no longer needed. I don't see if and how the EntityModel values are passed or consumed in the <DynamicComponent>s. If it's not done correctly, this is the likely cause for the value reset. After you upgrade to 4.2.0, you need to refactor the Form declaration and move your custom markup outside <FormItems> to <FormItemsTemplate>. Regards, Dimo Progress Telerik

### Response

**Peter** answered on 09 May 2023

Hi Dimo, thanks for the answer. I think you pointed into the right direction. Here's a sample of one of the Items, they are all made similar <FormItem> <Template> <label for="@RexFormItemConfig.Id"> @RexFormItemConfig.Label </label> <TelerikTextBox @bind-Value="@Value" Id="@RexFormItemConfig.Id" Name="@RexFormItemConfig.Id" ValidateOn="@ValidationEvent.Change" /> </Template> </FormItem> public string Value { get; set; } protected override void OnParametersSet () { base.OnParametersSet(); var model=(IPzeDomainEntity)FormRef.Model; var pi=model.GetType().GetProperty( this.RexFormItemConfig.Property);
Value=( string )pi.GetValue(model);
} Due to the dynamic nature of this, We load the Value in OnParametersSet(). This is done the same way in all the Items. this.RexFormItemConfig.Property ist just a string, with the property name loaded from a configuration object. Your statements give me pause and make me think that, as you suspect, this is where the problem lies. However, to be honest, I am not sure how I could do this differently without the filling of the "Value" properties. I thought binding it will be the best way.

### Response

**Dimo** commented on 09 May 2023

OK, I see. The app is setting (binding) the model values manually. This requires you to propagate the value changes up in the component hierarchy to where the Form is. Otherwise, the values in the original EntityModel object will never change, which is also a problem for the validation. [https://learn.microsoft.com/en-us/aspnet/core/blazor/components/data-binding?view=aspnetcore-7.0#binding-with-component-parameters](https://learn.microsoft.com/en-us/aspnet/core/blazor/components/data-binding?view=aspnetcore-7.0#binding-with-component-parameters)

### Response

**Peter** commented on 09 May 2023

Oh man, yes, I've read this so many times, and...forgot it. Again, thanks for the help. I think I can fix this, but first we'll go to 4.2. Then we can do this in one fell swoop. Please close the ticket.
