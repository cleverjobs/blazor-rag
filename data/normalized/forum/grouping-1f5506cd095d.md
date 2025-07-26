# Grouping

## Question

**Cin** asked on 23 Oct 2020

I have a Blazor Modal with a combobox. It provides a list of users that I want to group by role (see image). <div class="col-10 offset-2 mt-2"> <TelerikDropDownList Data="@UserDropdownList" ValueField="Id" TextField="Name" @bind-Value="@UserSettings.UserId"> </TelerikDropDownList> </div>

## Answer

**Marin Bratanov** answered on 23 Oct 2020

Hi Cindy, This was posted in the ComboBox forum, so I will also link the existing request for grouping in the combo box: [https://feedback.telerik.com/blazor/1477414-grouping-for-the-blazor-combobox.](https://feedback.telerik.com/blazor/1477414-grouping-for-the-blazor-combobox.) I've added your Vote to it to raise its priority, and you can Follow it for status updates. Since the posted snippet uses the DropDownList component, I also made a new feature request on your behalf for that functionality there too: [https://feedback.telerik.com/blazor/1492222-grouping-in-the-dropdownlist-dropdown.](https://feedback.telerik.com/blazor/1492222-grouping-in-the-dropdownlist-dropdown.) Your Vote is already in, and you can click the Follow button for emails with status updates on that too. For the time being, the component that offeres grouping is the grid, and you can preset that from code ( example ). Another alternative would be a treeview in a dropdown (see this feature request for a workaround and if that would be something you need - Vote for it to raise its priority and Follow it too). Regards, Marin Bratanov
