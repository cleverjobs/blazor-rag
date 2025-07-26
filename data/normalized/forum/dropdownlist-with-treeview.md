# Dropdownlist with Treeview

## Question

**Ser** asked on 21 Feb 2025

Hello, i want use the treeview, i have many elements. so it stretch if i expand it over the screen, and this is not fine :) so i want the treeview in the dropdown list. but it doestn work. it looks horrible. Have someone a idea or a soution. thank you. this is my code. and i need a treeview. because i have expand items. <TelerikDropDownList Data="@FlatData" @bind-Value="SelectedItemText"> <ItemTemplate> <TelerikTreeView Data="FlatData" SelectedItems="@SelectedItems" @bind-ExpandedItems="@ExpandedItems" /> </ItemTemplate> </TelerikDropDownList>

## Answer

**Hristian Stefanov** answered on 24 Feb 2025

Hi Serkan, The provided requirement outlines a component known as the DropDownTree. We have an open feature request for it: DropDownTree. I voted there on your behalf and raised the priority. Once implemented, the DropDownTree component seems a solution that aligns with your specific needs. It combines the functionality of a DropDownList with the visually appealing features of a TreeView. I admit that the public item is quite old. The reason is that items with higher priority have been addressed during that time. To keep you updated on its progress, I encourage you to subscribe to the item, ensuring that you receive email notifications whenever there are any updates regarding its status. Regards, Hristian Stefanov
