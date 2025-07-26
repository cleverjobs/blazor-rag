# Value gets set to null if ValueField is an empty string

## Question

**NiV** asked on 09 Jan 2025

Hi there. I have a list of a class which contains 2 string properties, "MyValueField" and "MyTextField". If one of the items in the list has the MyValueField property set to an empty string (in the example below it's the first item), selecting that item in the TelerikDropDownList will assign null to the binded value. Instead, an empty string should be assigned to the binded value variable. It is worth noting that "externally" assigning the binded value variable to an empty string (either on initialization or through a button) will successfully work and the TelerikDropDownList component will display the selected item. The following gif showcases the binded value variable becoming null when the item with MyValueField set to an empty string is selected through the TelerikDropDownList: [https://i.gyazo.com/3d75359334d900a74334ae6de2493576.mp4](https://i.gyazo.com/3d75359334d900a74334ae6de2493576.mp4) The following gif showcases the binded value variable becoming an empty string when pressing a button that sets it to one, and gets set to null when the first item in the TelerikDropDownList is selected: [https://i.gyazo.com/12ee88a8e161f8c3b5a023d8fbc44a28.mp4](https://i.gyazo.com/12ee88a8e161f8c3b5a023d8fbc44a28.mp4) Here is the REPL link: [https://blazorrepl.telerik.com/GfYbuCFt318IzZzv41](https://blazorrepl.telerik.com/GfYbuCFt318IzZzv41) This also affects the ComboBox component: [https://blazorrepl.telerik.com/czOPYjFf04sX7cIW36](https://blazorrepl.telerik.com/czOPYjFf04sX7cIW36)

## Answer

**Dimo** answered on 14 Jan 2025

Hi NiV-L-A, The ComboBox and DropDownList are generic components that don't know their value type at compile time. This is reflected in some aspects of the implementation. At some point in the internal logic, the components make checks with the newly set value and may assign the default value of the generic type which is null for strings. A possible easy workaround is to use the DropDownList ValueChanged event. If it fires with a null value, set it to string.Empty. In the meantime, I will try to find out if it's possible to avoid this need in the future. <TelerikDropDownList Data="@Data" ValueField="MyValueField" TextField="MyTextField" Value="SelectedValue" ValueChanged="@( (string newValue)=> SelectedValueChanged(newValue) )">
</TelerikDropDownList>

@code {
private void SelectedValueChanged ( string newValue ) { if (newValue==null )
{
newValue=string.Empty;
}

SelectedValue=newValue;
}
} You may also need a ValueExpression if the component is inside a Form: Requires ValueExpression exception Validate a Telerik component as a child component Regards, Dimo Progress Telerik
