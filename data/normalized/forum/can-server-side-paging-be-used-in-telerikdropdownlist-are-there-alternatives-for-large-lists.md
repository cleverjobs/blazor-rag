# Can server-side paging be used in TelerikDropDownList? Are there alternatives for large lists.

## Question

**Par** asked on 09 Aug 2022

I am using TelerikDropDownList component in my app, it can have 1000+ records, for performance reasons server-side paging is implemented. Does telerikDropdownlist support server-side paging? Please suggest alternatives for using server-side paging with the dropdown in a blazor app.

## Answer

**Nadezhda Tacheva** answered on 10 Aug 2022

Hi Parul, The DropDownList does not support paging, however, it provides a virtualization feature which allows you to use huge data source without UI performance issues. With virtualization enabled the component will reuse a set number of items in the dropdown as you scroll, instead of rendering out the entire data source. You may find more details in the DropDownList Virtualization article. It also provides examples for working with local and remote data. I hope you will find this information and article useful to move forward with your application. Please let us know if any further questions are raised. Regards, Nadezhda Tacheva Progress Telerik
