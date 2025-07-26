# Need ability to disable combobox components

## Question

**Dou** asked on 27 Dec 2023

I have a combobox component that can draw on available properties such as "Class" and "MaxHeight." However, when I try to implement comboboxes, I see no way to disable them. Below is a portion of the RenderComboBox method. I can only avoid the error by commenting out "d.AddAttribute(302, "Enabled", "false");" RenderFragment item=d=>
{
d.OpenComponent<ComboBoxPopupSettings>( 20 ); if (RowCount==0 ) { RowCount=20; }
d.AddAttribute( 300, "MaxHeight", $" {(RowCount * 22 ).ToString()} px" );
d.AddAttribute( 301, "Class", "telCombo" );
d.AddAttribute( 302, "Enabled", "false" );
d.CloseComponent();
}; The above code earns me the message " Object of type 'Telerik.Blazor.Components.ComboBoxPopupSettings' does not have a property matching the name 'Enabled'." Indeed, when I look it up, the list of inherited members has nothing for enabling/ disabling the feature. How can i disable it?

## Answer

**Radko** answered on 01 Jan 2024

Hello Doug, You can disable the combobox input itself, rather than the popup. To do this, you need to set the Enabled parameter to false. Here is a REPL example, where you can see the difference between an enabled and a disabled ComboBox: [https://blazorrepl.telerik.com/moYFuPYi24u4dXHP39](https://blazorrepl.telerik.com/moYFuPYi24u4dXHP39) Since your attempt to set the Enabled parameter to the ComboBoxPopupSettings tag rather than the TelerikComboBox, you receive an exception, as the popup does not indeed have such a parameter. To resolve this, simply move the Enabled declaration to its parent. Regards, Radko Progress Telerik
