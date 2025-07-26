# Cascading DropDownList With Virtualization

## Question

**Ind** asked on 14 Mar 2022

Hi, do you have a working sample of Cascading DropDownList with Virtualization? My use case: There are 2 dropdowns (A and B), dropdown B cascaded from A, dropdown B has virtualization turn on (large data) . I want to use the onChange-virtualization so I can still use my standard bind-value. I tried to follow your example [https://docs.telerik.com/blazor-ui/knowledge-base/samples/dropdownlist-cascading-samples.zip](https://docs.telerik.com/blazor-ui/knowledge-base/samples/dropdownlist-cascading-samples.zip) from your article [https://docs.telerik.com/blazor-ui/knowledge-base/dropdown-cascading](https://docs.telerik.com/blazor-ui/knowledge-base/dropdown-cascading) The problem with that "onchange-virtualization" sample is the second dropdown is still loading all the data I already tried not calling GetAllproducts() but just calling Rebind() (on the productDropDown) now the problem is the selectedValue on the second dropdown won't change after the first dropdown value has been changed. This does not happened when I use non virtualization. The other problem with Rebind(): the skip value is not reset to 0. So do you have the latest sample for this common virtualization use case? Thank you

### Response

**Indra** commented on 15 Mar 2022

I modified the Telerik REPL sample from this page [https://demos.telerik.com/blazor-ui/dropdownlist/virtualization](https://demos.telerik.com/blazor-ui/dropdownlist/virtualization) and this is my modification to show cascading dropdown with virtualization [https://blazorrepl.telerik.com/cmOxPJml02JeUCE212,](https://blazorrepl.telerik.com/cmOxPJml02JeUCE212,) I attached my REPL code too if that REPL page is modified. The issue is the skip value is not reset to 0 when the datasource has changed. So if you have a large datasource and you scroll down to the last dropdown item, when you change the datasource to smaller one when you open the dropdownList, the skip value is still the previous one. How do you reset the DropDownList skip value or other states(filter, etc.) to initial value when the datasource has been changed? Thanks

## Answer

**Dimo** answered on 17 Mar 2022

Hello Indra, Indeed, the described behavior is incorrect. I logged a public bug report on your behalf. Sorry if this is a show-stopper for you. I hope the data is not so much and you can turn off virtualization until we fix this. I am also awarding you some Telerik points. Regards, Dimo Progress Telerik

### Response

**Indra** commented on 17 Mar 2022

And shouldn't the Bind-Value be reset too? For non virtualMode, I do not
have to reset the bind-value for the second dropdown when I change the
datasource. In non virtual mode, when I change the first dropdown, the
second dropdown value is also reset to default.

### Response

**Dimo** commented on 22 Mar 2022

This behavior is by design. The idea is that the component data changes all the time during virtual scrolling and we don't want to reset the value in this case. You can clear the value manually.

### Response

**Indra** commented on 13 Oct 2022

The bug fix is still unplanned, do you have temporary solution for this large data cascading scenario? Our project will soon goes to production with large data.

### Response

**Dimo** commented on 17 Oct 2022

Hi Indra, A possible workaround is to recreate the cascading DropDownList when its Data changes. This is usually done by toggling the visibility (rendering): <TelerikButton OnClick="@RecreateComponent">Recreate Component</TelerikButton> @if (IsVisible) { <p> Some component here... @DateString </p> } @code { bool IsVisible { get; set; }=true; string DateString=> DateTime.Now.ToLongTimeString(); async Task RecreateComponent ( ) { IsVisible=false; await Task.Delay( 1 );
IsVisible=true; }
}
