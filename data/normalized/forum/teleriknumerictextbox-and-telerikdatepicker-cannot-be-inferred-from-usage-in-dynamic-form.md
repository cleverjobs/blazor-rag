# TelerikNumericTextBox and TelerikDatePicker cannot be inferred from usage in dynamic form

## Question

**JimJim** asked on 14 Dec 2022

Hi, I am working on a dynamic form generator which is capable of generating a form based on a Json formdefinition retrieved from the server. I had some hurdles, but so far things are progressing nicely. Here's a summary of how it works (or should work): FormDefinition with FormFields is retrieved from the server FormModel is created dynamically using PropertyBuilder and AttributeBuilder Form uses an EditContext which takes the generated FormModel as an input TelerikTextBox and TelerikRadioButtonGroup work like a charm (they both use string properties of the dynamically created model). However the TelerikNumericTextBox and TelerikDateTimePicker generate the following error (and show a red line in the razor file: Error (active) CS0411 The type arguments for method 'TypeInference.CreateTelerikNumericTextBox_0 <T> (RenderTreeBuilder, int, int, string, int, T, int, Expression<Func <T>>, int, int, int, T, int, string, int, EventCallback <object>, int, EventCallback <T> )' cannot be inferred from the usage. Try specifying the type arguments explicitly.

Error (active) CS0411 The type arguments for method 'TypeInference.CreateTelerikDatePicker_1 <T> (RenderTreeBuilder, int, int, string, int, T, int, Expression<Func <T>>, int, EventCallback <object>, int, EventCallback <T>, int, string)' cannot be inferred from the usage. Try specifying the type arguments explicitly. I assume it has something to do with the type of the propery, but I am not sure. Here's the full code of the dynamic form so far. @namespace TrueLime.Blazor.TrueForms
@inherits TrueFormBase <TelerikForm EditContext="@FormEditContext" OnSubmit="@HandleSubmit"> <FormValidation> <DataAnnotationsValidator> </DataAnnotationsValidator> </FormValidation> <FormItems> @foreach (var propertyInfo in GetFormFieldProperties())
{ <FormItem Field="@(propertyInfo.Name)"> <Template> <div class="mb-1 row"> <label for="@(propertyInfo.Name)" class="k-label k-form-label col-sm-2"> @propertyInfo.DisplayName() </label> <div class="col-sm-8"> @switch (GetFormControlType(propertyInfo.Name))
{
case "textbox": <TelerikTextBox Id="@(propertyInfo.Name)" Value="@GetStringValue(propertyInfo.Name)" ValueExpression="@(()=> propertyInfo.Name)" OnChange="OnChange" ValueChanged="@(value=> OnValueChanged(value, propertyInfo.Name))" InputMode="text" PlaceHolder="@propertyInfo.PlaceholderDescription()"> </TelerikTextBox> break;
case "decimaltextbox": <TelerikNumericTextBox Id="@(propertyInfo.Name)" Value="@GetDecimalValue(propertyInfo.Name)" ValueExpression="@(()=> propertyInfo.Name)" Decimals="2" Step="0.01m" Format="@CurrencyFormat" OnChange="OnChange" ValueChanged="@(value=> OnValueChanged(value, propertyInfo.Name))"> </TelerikNumericTextBox> break;
case "datepicker": <TelerikDatePicker Id="@(propertyInfo.Name)" Value="@GetDateTimeValue(propertyInfo.Name)" ValueExpression="@(()=> propertyInfo.Name)" OnChange="OnChange" ValueChanged="@((DateTime value)=> OnValueChanged(value, propertyInfo.Name))" Placeholder="@propertyInfo.PlaceholderDescription()"> </TelerikDatePicker> break;
case "radiogroup": <TelerikRadioGroup Id="@(propertyInfo.Name)" Value="@GetStringValue(propertyInfo.Name)" ValueExpression="@(()=> propertyInfo.Name)" OnChange="OnChange" ValueChanged="@((string value)=> OnValueChanged(value, propertyInfo.Name))" Layout="@GetRadioGroupLayout(propertyInfo.Name)" Data="@GetFormOptions(propertyInfo.Name)" ValueField="@nameof(FormOption.Value)" TextField="@nameof(FormOption.Text)"> </TelerikRadioGroup> break;
} </div> <div class="col-sm-2"> <TrueFormValidationMessage For="@(new FieldIdentifier(FormModel, propertyInfo.Name))" /> </div> </div> </Template> </FormItem> } </FormItems> <FormButtons> <TelerikButton ButtonType="ButtonType.Submit"> @SubmitButtonLabel </TelerikButton> </FormButtons> </TelerikForm> <br /> @ScreenLog Here's the OnValueChanged (which needs work, but the get the gist of it): protected void OnValueChanged(object e, string propertyName)
{
var propertyInfo=FormInputModel.GetType().GetProperty(propertyName);
if (propertyInfo==null) return;

if (propertyInfo.PropertyType==typeof(int))
SetFormValue(propertyInfo.Name, Convert.ToInt32(e));

if (propertyInfo.PropertyType==typeof(long))
SetFormValue(propertyInfo.Name, Convert.ToInt64(e));

if (propertyInfo.PropertyType==typeof(decimal))
{
// Needs work
SetFormValue(propertyInfo.Name, Convert.ToDecimal(e, new CultureInfo("nl-NL", false)));
}

if (propertyInfo.PropertyType==typeof(string))
SetFormValue(propertyInfo.Name, e.ToString());

//if (propertyInfo.PropertyType==typeof(DateTime) || propertyInfo.PropertyType==typeof(DateTime?))
// throw new NotImplementedException("DateTime nog niet geimplementeerd.");

//if (propertyInfo.PropertyType==typeof(bool) || propertyInfo.PropertyType==typeof(bool))
// throw new NotImplementedException("Boolean nog niet geimplementeerd.");
} And some of the helper methods: private FormField GetFormField(string propertyName)=>
FormDefinition.FormFields.SingleOrDefault(x=> x.PropertyName==propertyName);

protected string GetStringValue(string propertyName)=>
GetFormValue(propertyName)?.ToString();

protected decimal GetDecimalValue(string propertyName)=>
Convert.ToDecimal(GetFormValue(propertyName));

protected DateTime GetDateTimeValue(string propertyName)=>
Convert.ToDateTime(GetFormValue(propertyName));

protected object GetFormValue(string propertyName)=>
FormModel?.GetType().GetProperty(propertyName)?.GetValue(FormModel);

protected void SetFormValue(string propertyName, object value)=>
FormModel.GetType().GetProperty(propertyName)?.SetValue(FormModel, value, null); Any help is highly appreciated.

### Response

**Jim** commented on 15 Dec 2022

To make myself a bit more clear. This DOES work. <TelerikTextBox Id="@(propertyInfo.Name)" Value="@GetStringValue(propertyInfo.Name)" ValueExpression="@(()=> propertyInfo.Name)" OnChange="OnChange" ValueChanged="@(value=> OnValueChanged(value, propertyInfo.Name))" InputMode="text" PlaceHolder="@propertyInfo.PlaceholderDescription()"> </TelerikTextBox> This DOES work too (both use string as property type, not sure if that's relevant) <TelerikRadioGroup Id="@(propertyInfo.Name)" Value="@GetStringValue(propertyInfo.Name)" ValueExpression="@(()=> propertyInfo.Name)" OnChange="OnChange" ValueChanged="@((string value)=> OnValueChanged(value, propertyInfo.Name))" Layout="@GetRadioGroupLayout(propertyInfo.Name)" Data="@GetFormOptions(propertyInfo.Name)" ValueField="@nameof(FormOption.Value)" TextField="@nameof(FormOption.Text)"> </TelerikRadioGroup> However, this DOES NOT work (for decimal) <TelerikNumericTextBox Id="@(propertyInfo.Name)" Value="@GetDecimalValue(propertyInfo.Name)" ValueExpression="@(()=> propertyInfo.Name)" Decimals="2" Step="0.01m" Format="@CurrencyFormat" OnChange="OnChange" ValueChanged="@(value=> OnValueChanged(value, propertyInfo.Name))"> </TelerikNumericTextBox> And this DOES NOT work either (for DateTime) <TelerikDatePicker Id="@(propertyInfo.Name)" Value="@GetDateTimeValue(propertyInfo.Name)" ValueExpression="@(()=> propertyInfo.Name)" OnChange="OnChange" ValueChanged="@((DateTime value)=> OnValueChanged(value, propertyInfo.Name))" Placeholder="@propertyInfo.PlaceholderDescription()"> </TelerikDatePicker>

### Response

**Jim** commented on 15 Dec 2022

After some more testing I have found a solution. I have added the T property and set it to decimal and I have replaced the ValueExpression with a DummyDecimalValue property. protected decimal DummyDecimalValue { get; set; } <TelerikNumericTextBox Id="@(propertyInfo.Name)" T="decimal" ValueExpression="@(()=> DummyDecimalValue)" Decimals="2" Step="0.01m" Format="@CurrencyFormat" OnChange="OnChange" Value="@GetDecimalValue(propertyInfo.Name)" ValueChanged="@(value=> OnValueChanged(value, propertyInfo.Name))"> </TelerikNumericTextBox> The valueexpression for the working controls didn't result in an error because the propertyInfo.Name is a string. I have replaced the valueexpression with this for clarification. protected string DummyStringValue { get; set; }
