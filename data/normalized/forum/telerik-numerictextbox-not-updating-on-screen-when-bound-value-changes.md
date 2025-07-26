# Telerik NumericTextBox not updating on screen when bound value changes

## Question

**Adr** asked on 08 Jul 2021

I have a Blazor application that has some custom component wrappers to the standard Telerik components. For example we have implemented the following wrapper component for a TelerikNumericTextBox @typeparam TModelProperty
@inherits CslaNumericInputBase <TModelProperty> <div> @if (ShowLabel)
{ <CslaLabel Property="Property" /> } <TelerikNumericTextBox T="TModelProperty" Id="@Property.PropertyName" @bind-value="Value" @bind-value:event="@BindEvent" Min="@Min" Max="@Max" Step="@Step" Format="@Format" Decimals="@Decimals" Arrows="@Arrows" Enabled="@Property.CanWrite" Width="@Width" Class="@Class" /> <CslaInputValidationMessages Property="Property" /> </div> The component wrapper code behind file looks like this: using System; using Microsoft.AspNetCore.Components; using ServiceStack; namespace MB5.Client.Shared { public class CslaNumericInputBase <TModelProperty> : CslaInputBase {
[ Parameter ] public string Width { get; set; }="100%";

[ Parameter ] public bool? BoldCondition { get; set; }

[ Parameter ] public TModelProperty Min { get; set; }

[ Parameter ] public TModelProperty Max { get; set; }

[ Parameter ] public TModelProperty Step { get; set; }

[ Parameter ] public int Decimals { get; set; }

[ Parameter ] public bool Arrows { get; set; }=true; protected TModelProperty Value
{ get=> Property.Value !=null? (TModelProperty)Property.Value : default; // ReSharper disable once UnusedMember.Global set { var defaultValueForModelProperty=default (TModelProperty); if (!Equals( value, defaultValueForModelProperty))
{
SetNewValue( value );
} else { if (! typeof (TModelProperty).IsNullableType())
{
SetNewValue( default );
} else {
Property.Value=null;
}
}
}
} protected string Class
{ get { if (BoldCondition.HasValue && BoldCondition.Value)
{ return "bold";
} return null;
}
} private void SetNewValue ( TModelProperty newValue ) {
Property.Value=newValue;
}
}
} using Csla.Blazor; using Microsoft.AspNetCore.Components; namespace MB5.Client.Shared { public class CslaInputBase: ComponentBase { private const string OnInputEventName="oninput"; private const string OnChangeEventName="onchange"; private bool _bindPropertyAndValidationOnInput=true; protected string BindEvent=OnInputEventName;

[ Parameter ] public IPropertyInfo Property { get; set; }

[ Parameter ] public bool BindPropertyAndValidationOnInput
{ get=> _bindPropertyAndValidationOnInput; set {
_bindPropertyAndValidationOnInput=value;
BindEvent=_bindPropertyAndValidationOnInput ? OnInputEventName : OnChangeEventName;
}
}

[ Parameter ] public bool ShowLabel { get; set; }=true;

[ Parameter ] public string ExtraLabelText { get; set; }="";

[ Parameter ] public bool PreFixExtraLabelText { get; set; }

[ Parameter ] public string Format { get; set; }="";
}
} We add the component to the page like so: <CslaNumericInput TModelProperty="decimal?" ShowLabel="false" BindPropertyAndValidationOnInput="false" Property="@(vm.GetPropertyInfo(()=> vm.Model.PremiumTyreValue))" Min="0" Max="9999" Step="1" Decimals="2" Format="N2" /> If we directly update the control value by typing in the textbox then it works. If we update the model value which is bound to the control we expect the new updated value to appear in the textbox. What is happening is that the model value updates successfully but the control doesn't update the value on screen. If you click (set focus) to the textbox then it will update the value in the textbox to the new updated one saved to the model. I have made a video: [https://drive.google.com/file/d/1GVpqJy7EygWZt5rXZCHlQxPRZPNIbhdz/view?usp=sharing](https://drive.google.com/file/d/1GVpqJy7EygWZt5rXZCHlQxPRZPNIbhdz/view?usp=sharing) It shows that on click of the Copy Default to User button the values in the left hand column (Default values) are copied to the right hand column (User values) and you can see that the first two rows at the start are different to the defaults and we expect them both to update and match the default values. Notice that the dropdown correctly updates but the custom NumericTextBox does update even though the model value changes. You will see that when you click into the textbox then the value that we expected to automatically be populated is populated when focus is set to the control. Any idea how we can get the value to update on screen automatically?

### Response

**Dimo** commented on 09 Jul 2021

Hi Adrian, There are a few object types that are not included in the code snippet and this prevents me from creating a test page. So let me ask you this: - Is the same problem exhibited with a plain non-wrapped TelerikNumericTextBox? If not, then the issue lies in the wrapper. If yes, please provide an isolated runnable sample with a TelerikNumericTextBox and I will investigate what's going on.

### Response

**Adrian** commented on 13 Jul 2021

Hi, I have created a repro of the issue and pushed the code to my GitHub: [https://github.com/adrianwright109/NumericTextBox](https://github.com/adrianwright109/NumericTextBox) It seems that the default TelerikNumericTextBox and the Custom one which is wrapping the TelerikNumericTextBox both display the same behaviour when it comes to updating the bound model properties in code. The properties update but the values are not shown in the TelerikNumericTextBox. Also noticed on the custom wrapper version if you use the up and down arrows to change the value the bound value doesn't update until you click on a up and down arrow on a different control (the default TelerikNumericTextBox seem to update the model on the click of its own arrows).

## Answer

**Dimo** answered on 14 Jul 2021

Hello Adrian, Thanks for the runnable project. I fiddled with it for a bit and ultimately saw the problem - @bind- V alue should be with a capital V, as the Blazor attribute binding is case sensitive. The issue is visible on the initially provided snippet, but I admit I didn't notice it then. With regard to the up and down arrows on the custom textbox - even if you directly type a new value in it, the model value is not updated. This should be caused by something in the wrapper implementation, as the standard TelerikNumericTextBox updates the same Model successfully. Regards, Dimo
