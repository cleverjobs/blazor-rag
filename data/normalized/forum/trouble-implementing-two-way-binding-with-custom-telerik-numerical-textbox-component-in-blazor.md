# Trouble Implementing Two-way Binding with Custom Telerik Numerical Textbox Component in Blazor

## Question

**Ahm** asked on 11 Jul 2023

I am having difficulty implementing a custom Telerik Numerical Textbox component in a Blazor application, specifically with setting up two-way data binding. In my Razor page, I'm trying to use the custom component like so: <CustomNumericalTextBox Id="ID" Format="P" Min="0" Max="1" Step="0.01m" @Bind-Value="@Model.Value1" /> In the code-behind of this page, I have a model class: public class Model { public decimal Value1 { get; set; }="Something" } The custom component is defined in a separate Razor page: @inherits CustomNumericalTextBoxBase <FormItem> <Template> <TelerikNumericalTextBox Id="@Id" Format="@Format" Min="@Min" Max="@Max" @bind-Value="@BindValue"> </TelerikNumericalTextBox> </Template> </FormItem> And its code-behind is: public class CustomNumericalTextBox {
[ Parameter ] public decimal BindValue { get; set; }

[ Parameter ] public EventCallback<decimal> BindValueChanged { get; set; }

[ Parameter ] public string Format { get; set; }=string.Empty;

[ Parameter ] public string Min { get; set; }="0";

[ Parameter ] public string Max { get; set; }="1";

[ Parameter ] public string Id { get; set; }
} Any guidance on how I can achieve two-way data binding with this custom component would be greatly appreciated. The errors I receive are: 'CustomNumericalTextBox.BuildRederTree(RederTreeBuilder)': No suitable method found to override 'CustomNumericalTextBox.BuildRederTree(RederTreeBuilder)': No suitable method found to override The attribute names could not be inferred from bind attribute 'bind-BindValue'. Bind attributes should be of the form 'bind' or 'bind-value' along with their corresponding optional parameters like 'bind-value:event', 'bind:format' etc.

## Answer

**Dimo** answered on 13 Jul 2023

Hello Ahmad, There are two possible issues here: When you override one of our components, you can follow two techniques. It is possible that the problem is caused by using a different approach, rather than the ones below: Inherit the base component, but in this case, you can't override the markup in a .razor file. Don't inherit the base component, override the markup, but don't override the C# logic. <FormItem> tags should belong to the .razor component, which holds the <TelerikForm> component. If you need separation in custom child components, use a FormItemsTemplate with renderers. I suspect the error is either related to problem 1, or to something else, which is not related to our components. Regards, Dimo

### Response

**Ahmad Josef** commented on 17 Jul 2023

We found an approach, where we inherit from inputbase<T>, and that works for TelerikTextBox, TelerikTextArea and TelerikCheckBox, but for a reason we don't understand, it doesn't work for TelerikNumericalTextBox. Razor File of Component: @inherits CustomNumericalTextBoxBase <FormItem ColSpan="@ColSpan" Field="@Field"> <Template> <label for="@Id" class="k-label k-form-label" data-bookmark="@DataBookmark"> @Label </label> <TelerikNumericTextBox Id="@Id" Format="@Format" Max="@Max" Min="@Min" Step="@Step" Decimals="@Decimals" @bind-Value="@CurrentValue" Enabled="@Enabled"> </TelerikNumericTextBox> <div class="k-form-hint"> @Hint </div> </Template> </FormItem> Code Behind of the razor file above: using Microsoft.AspNetCore.Components; using Microsoft.AspNetCore.Components.Forms; using DocumentFormat.OpenXml.Spreadsheet; namespace ServerApp.Shared { public class Custom NumericalTextBoxBase: InputBase <decimal>
{
[ Parameter ] public string DataBookmark { get; set; }="";
[ Parameter ] public string Hint { get; set; }="";
[ Parameter ] public int ColSpan { get; set; }=12;
[ Parameter ] public string Format { get; set; }=String.Empty;
[ Parameter ] public string Max { get; set; }="1";
[ Parameter ] public string Min { get; set; }="0";
[ Parameter ] public string Step { get; set; }="0.01m";
[ Parameter ] public int Decimals { get; set; }=2;
[ Parameter ] public string Label { get; set; }="";
[ Parameter ] public string PlaceHolder { get; set; }="";
[ Parameter ] public String Class { get; set; }="";
[ Parameter ] public bool Enabled { get; set; }=true;
[ Parameter ] public string Field { get; set; }=String.Empty; private string? _id=null;
[ Parameter ] public string Id
{ get { return _id ?? Field;
} set {
_id=value;
}
} protected override bool TryParseValueFromString ( string? value, out decimal result, out string validationErrorMessage ) { if ( decimal.TryParse( value, out result))
{
validationErrorMessage=null; return true;
} else {
validationErrorMessage=$"The value must be a valid decimal."; return false;
}
}
}
} As mentioned, the approach shown above works for almost all other Telerik components, but not for TelerikNumericalTextBox. We can't figure out what we are doing wrong for this specific component. Any help on fixing this is highly appreciated!

### Response

**Dimo** commented on 17 Jul 2023

The Max, Min and Step parameters of our NumericTextBox component are pointing to string properties. The type of these three parameters must match the type of the Value parameter, which is decimal in this case. On a side note, please avoid phrases such as "something is not working". Instead, be more specific what is the expected behavior, what is the actual behavior, what are the exact error messages (if any), etc.

### Response

**Ahmad Josef** commented on 17 Jul 2023

Changing the properties Max, Min and Step to decimal type fixed our issue, and we can now use the component. Thank you for your time and help. I will remember to be more specific, when posting next time.
