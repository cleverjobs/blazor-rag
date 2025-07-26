# TelerikForm: FormItem for bool value does not 'trigger' on change - aka checkbox

## Question

**Chr** asked on 21 Jul 2021

Hi all, We want an easy to set up (and easy to code) form in Blazor, with default CSS styling, and with real two-way data binding. And this is where we are already struggling. In our case, we cannot get one checkbox to trigger the visibility of another. To better understand the issue, we provide a simple and small sample (attached). It has a very simple TelerikForm and a very simple EditForm. <TelerikForm Model="@_data"> <FormItems> <FormItem LabelText="Condition 1:" Field="@nameof(_data.Value1)"> </FormItem> @if (_data.Value1)
{ <FormItem LabelText="Result 1:" Field="@nameof(_data.Value2)"> </FormItem> } </FormItems> </TelerikForm> <br /> <br /> <EditForm Model="@_data"> <label> Condition 2: </label> <InputCheckbox @bind-Value="@_data.Value1" /> <br /> @if (_data.Value1)
{ <label> Result 2 </label> <InputCheckbox DisplayName="Result 2:" @bind-Value="@_data.Value2"> </InputCheckbox> } </EditForm> @code {
private ExampleDto _data { get; set; }=new ExampleDto();
} To repro the behavior: If you click 'Condition 2' (inside the EditForm), then it triggers any bound item, also in the TelerikForm. However, if you click 'Condition 1' in the TelerikForm, nothing will change and nothing gets triggered. Is there an easy and obvious solution? Thanks!

## Answer

**Christian** answered on 21 Jul 2021

This seems to work: <TelerikForm Model="@_data"> <FormItems> <FormItem> <Template> <label for="x"> Condition 1: </label> <TelerikCheckBox Id="x" @bind-Value="_data.Value1" /> </Template> </FormItem> @if(_data.Value1)
{ <FormItem LabelText="Result 1:" Field="@nameof(_data.Value2)"> </FormItem> } </FormItems> </TelerikForm> Why would this not be the default behavior...?

### Response

**Dimo** commented on 23 Jul 2021

Hi Christian, Thanks for the provided code. I was able to reproduce the described behavior and I agree it doesn't look right. It's good that you have found a workaround In the meantime, I have forwarded a test page to our developers to take a look. I will update this thread if there is new information, and will log a bug, if confirmed.

### Response

**Christian** commented on 23 Jul 2021

Great, thanks Dimo!

### Response

**Dimo** commented on 23 Jul 2021

Hi again, Christian, The bug is now confirmed and logged on your behalf: [https://feedback.telerik.com/blazor/1529038-boolean-formitem-does-not-trigger-model-and-dynamic-form-updates](https://feedback.telerik.com/blazor/1529038-boolean-formitem-does-not-trigger-model-and-dynamic-form-updates) You will receive email notifications for status updates. Thank you for bringing the issue to our attention! I also updated your Telerik points.
