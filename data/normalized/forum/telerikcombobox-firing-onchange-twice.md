# TelerikComboBox firing OnChange twice

## Question

**Mar** asked on 27 Aug 2021

Hi when I select an item I get a change event as expected, but I also got one on lostfocus, when I tab away. <td class="pe-3"> <TelerikComboBox Data="@ComboItems" TextField="Name" ValueField="Id" @bind-Value="SelectedValue" OnChange="ValueChangedHandler" /> </td> private void ValueChangedHandler(object value)
{
int id=(int) value;
Console.WriteLine("" + id);
} ValueChangedHandler called twice

## Answer

**Matthias** answered on 27 Aug 2021

I'm pretty sure that the binding only occurs when you leave the ComoBox. Without binding, "ValueChanged" would be called only once. Try this without binding and use only "Value". This will be the case for all input fields.

### Response

**Marin Bratanov** answered on 28 Aug 2021

Hi Martin, Take a look at this article which describes this behavior and two ways to avoid it: [https://docs.telerik.com/blazor-ui/knowledge-base/common-onchange-fires-twice](https://docs.telerik.com/blazor-ui/knowledge-base/common-onchange-fires-twice) Regards, Marin Bratanov
