# Selected Item Data Binding

## Question

**And** asked on 13 Nov 2023

Hello, My use case requires me to be able to set the selected panel bar item programmatically. However, I don't see any data bindings or api methods on the control ref to set the selected panel. Is this possible? Setting the private member SelectedItem through reflection appears to work. Are there implications to doing this that I should be aware of? PanelBarRef.GetType().InvokeMember("SelectedItem", BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.SetProperty | BindingFlags.Instance, null, PanelBarRef, new object[] { SelectedPage }); Thank You, -Andy

## Answer

**Dimo** answered on 16 Nov 2023

Hi Andy, This approach is not officially documented and supported, so we haven't tested it and cannot claim that it's reliable. Alternatively, you can use OnItemRender and some custom CSS: Select PanelBar item programmatically Regards, Dimo Progress Telerik
