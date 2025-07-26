# Have a class for the menu drop down

## Question

**JJJJ** asked on 30 Jun 2023

I have a ItemTemplate for the menu item which defines background color. But the parent node define the Padding, so it has different background color. I want to remove that padding. But I don't want to change the style for global Telerik class, the other places may not want the behavior. For Telerik DropDownList, we can have DropDownListSettings to define a separated class for the dropdownlist, like this: <TelerikDropDownList Class="@componentClass"> <DropDownListSettings> <DropDownListPopupSettings Class="@dropdownClass" /> </DropDownListSettings> <TelerikDropDownList> Please provide the same for TelerikMenu as well, so we can style the item without affect the Telerik global class.
