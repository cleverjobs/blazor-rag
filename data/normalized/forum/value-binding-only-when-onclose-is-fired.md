# Value binding only when OnClose is fired

## Question

**Lis** asked on 02 Dec 2022

Hi, Is there a way to bind the selected Value in a TelerikDropdownList only when the popup is closed? I don't want the Value to be binded, when I use the arrows (up/down) - only when I hit enter or click on an element in the popup. In the following code the Value is binded, when the popup is closed, but the arrows is not working in the popup. <ul> <li> DropDownList Value: @DropDownValue </li> <li> Event Log: @EventLog </li> <li> Selected Log: @SelectedLog </li> </ul> <TelerikDropDownList Data="@DropDownData" Value="@DropDownValue" ValueChanged="@( (string newValue)=> OnDropDownValueChanged(newValue) )" OnClose="@( (DropDownListCloseEventArgs arg)=> OnPopupClosed(arg) )"> </TelerikDropDownList> @code{ private List <string> DropDownData { get; set; }=new List <string> { "Manager", "Developer", "QA", "Technical Writer", "Support Engineer" }; private string DropDownValue { get; set; }="Developer"; private string SelectedValue { get; set; } private string EventLog { get; set; } private string SelectedLog { get; set; } private void OnDropDownValueChanged(string newValue) { SelectedValue=newValue; EventLog=string.Format("The user selected: {0}", SelectedValue); } private void OnPopupClosed(DropDownListCloseEventArgs arg) { DropDownValue=SelectedValue; SelectedLog=string.Format("OnPopupClosed: {0}", DropDownValue); } }

## Answer

**Dimo** answered on 07 Dec 2022

Hello Lisa, Such a behavior will be possible to achieve when we implement this feature request. In the meantime, you can use a similar approach as the one in the linked page - use an ItemTemplate, which will capture item clicks, and ignore value changes via the arrow keys, which happens with the provided implementation, because the ValueChanged handler does not update DropDownValue. Regards, Dimo Progress Telerik
