# Menu for BLAZOR - How to change the color of the menu items?

## Question

**Sat** asked on 17 Nov 2021

I have the following code. Currently it renders menus in Orange color by default. How to customize the item color to WHITE and make it BOLD? <div style="width: 100%; margin: 0 auto; background-color:gray;"> <TelerikMenu Data="@MenuItems" Class="centered-menu" UrlField="@nameof(MenuItem.Page)" ItemsField="@nameof(MenuItem.SubSectionList)" TextField="@nameof(MenuItem.Section)"> </TelerikMenu> </div> My CSS: .k-menu.centered-menu,
::deep .k-menu.centered-menu {
justify-content: center;
} It renders:

## Answer

**Dimo** answered on 18 Nov 2021

Hello Satish, The Menu root item color is set in our theme with a specificity of 0,3,0 (three CSS classes). To override it, you need to use the same or higher specificity, for example: (in the .razor file - same specificity) .centered-menu.k-menu.k-item { color: white; font-weight: bold;
} (OR in the .razor.css file - higher specificity, due to the ::deep dynamic selector) ::deep.centered-menu.k-menu.k-item { color: white; font-weight: bold;
} Regards, Dimo
