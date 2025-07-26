# preventdefault on checkbox

## Question

**Mor** asked on 30 Apr 2020

Hi, I want to set preventDefault to true on my checkbox, something like this: <TelerikCheckBox Id="checkboxReader" @onclick:preventDefault="true" Class="checkbox-rbac" @bind-Value="isReader"></TelerikCheckBox> But I get error: Unhandled exception rendering component: Object of type 'Telerik.Blazor.Components.TelerikCheckBox`1[[System.Boolean, mscorlib, Version=2.0.5.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]' does not have a property matching the name 'onclick'. It works fine for normal input: <input id="checkbox-rbac-azure-01" class="checkbox-rbac-azure" type="checkbox" @onclick:preventDefault="true" />

## Answer

**Marin Bratanov** answered on 30 Apr 2020

Hi Morten, This approach is only possible with plain DOM elements, but it is not possible for components. You need to use an HTML element around the checkbox in a fashion similar to this: [https://docs.telerik.com/blazor-ui/knowledge-base/inputs-handle-keyboard-events](https://docs.telerik.com/blazor-ui/knowledge-base/inputs-handle-keyboard-events) <div @onclick="@DivClick">
<span @onclick:preventDefault="true"><TelerikCheckBox @bind-Value="@cbValue" /></span>
<input id="checkbox-rbac-azure-01" class="checkbox-rbac-azure" type="checkbox" @onclick:preventDefault="true" />
</div>

@code{ bool cbValue { get; set; } void DivClick ( ) {
Console.WriteLine( "DIV click" );
}
} Regards, Marin Bratanov

### Response

**Morten** answered on 30 Apr 2020

Ok thanks Marin. I think I'm in a little catch22 here. I simply want the checkbox to not check (on the UI), but still want to capture the click and the value. I can get it to work with input like this: <td><input id="checkbox-rbac-azure-01" class="k-checkbox checkbox-rbac-azure" type="checkbox" @onclick="@(e=> RoleChecked(e,AzureRoles.Reader))" @onclick:preventDefault="true" /></td> But this does not give me the object value only the mousevent. I tried this: <td> <span @onclick:preventDefault="true"> <TelerikCheckBox Class="checkbox-rbac-azure" OnChange="@(e=> RoleChecked2((bool)e, AzureRoles.Contributor))" @bind-Value="isContributor"></TelerikCheckBox> </span> </td> but this prevents the onchange from firing.

### Response

**Morten** answered on 30 Apr 2020

Anyways I can work it out with checking the value it is binded too, but that gives me some more workarounds though. Had been easier if I could capture the object from the OnChange event.

### Response

**Marin Bratanov** answered on 30 Apr 2020

Hello Morten, If you need the user action (attempt to check/uncheck), use the ValueChanged event, determine whether you want to change the value and change it in the model if you need to. If not - don't change it and the UI won't change. Regards, Marin Bratanov

### Response

**Jim** answered on 05 Aug 2020

Do you plan on fixing this issue with onclick on a telerik component? So that you don't have to wrap it?

### Response

**Marin Bratanov** answered on 05 Aug 2020

Hello Jim, This is not an issue with the component. Such attributes (and, by the way, attribute splatting as well) can work for simple DOM elements, like a <span>, for example. That does not work well for components (like what we do), and even worse when they have a complex HTML structure behind the simple tag you write. You can read more details and the discussion in this thread: [https://feedback.telerik.com/blazor/1416978-support-arbitrary-attributes](https://feedback.telerik.com/blazor/1416978-support-arbitrary-attributes) So, for the Telerik CheckBox Component - you can use the events it provides, and you can "cancel" the ValueChanged event if you don't want to update the value. Regards, Marin Bratanov

### Response

**Andrew** commented on 04 Mar 2022

Marin, I'm in a position where I need to "cancel" the checkbox event. And I'm using the ValueChanged technique, however it appears that the UI element is checking and unchecking irrespective of whether or not I update the underlying model. I tested this in the ValueChanged documentation site: [https://docs.telerik.com/blazor-ui/components/checkbox/events#valuechanged](https://docs.telerik.com/blazor-ui/components/checkbox/events#valuechanged) By commenting out the following line and you'll see that the check box still checks even though the model is not updated. Any advice? -Andy item. IsDelivered=value;

### Response

**Marin Bratanov** commented on 06 Mar 2022

My best guess is that something happens around the parameters coming from a parent component and how data travels to it, and when child components re-render. With just one line of code it is a bit of a shot in the dark. If reviewing when re-renders happen and ensuring the parent component has the correct value don't help - I recommend opening a support ticket with a small reproducible sample.

### Response

**Jim** answered on 05 Aug 2020

I understand. Thanks.
