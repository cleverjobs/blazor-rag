# Component Library

## Question

**Jes** asked on 02 Dec 2020

Hello everyone, Recently I have been working on a project where we wanted build all of our Components in a separate library. When we do this, we get the purple squiggly line stating "Found markup element with unexpected name 'TelerikMenu'. If this is intended to be a component, add a @using directive for its namespace." This is what we include in our _Imports.razor for the Library itself: @* Telerik. *@@using Telerik.Blazor @using Telerik.Blazor.Components This is one of our Components - MainMenu.razor: @namespace Component.Menu @inherits MainMenuBase @using ViewModel.MainMenu <TelerikMenu Data="@MenuItems" ItemsField="@nameof(MainMenuViewModel.SubMenuList)" TextField="@nameof(MainMenuViewModel.Name)" UrlField="@nameof(MainMenuViewModel.Page)" ImageUrlField="@nameof(MainMenuViewModel.IconUrl)" IconField="@nameof(MainMenuViewModel.Icon)" IconClassField="@nameof(MainMenuViewModel.IconClass)" Orientation="@MenuOrientation.Horizontal" /> When we compile the project, it runs just fine, but we were really looking for a way to make sure these Messages do not show up. It also makes it so Intellisense does not find all of the Parameters available to a Telerik Component. All C# code is in full Code-Behind and why it is not posted here. The C# has no problems at all with Errors, Warnings, or Messages. Thank you for your time, Jesse

## Answer

**Marin Bratanov** answered on 03 Dec 2020

Hi Jesse, Since the builds run OK, this indicates that the components are referenced and work as expected and the issue is in the VS intellisense itself. Closing all tabs, closign VS, deleting the bin and obj folders and the .vs folder of the solution could help it rebuild its caches and start working. It is not something we can influence, however, the razor editor and intellisense are entirely in the IDE domain. Perhaps you can also try to switch back and forth between the standard and experimental razor editors to see if this makes a difference too. Regards, Marin Bratanov

### Response

**Jesse** answered on 03 Dec 2020

Marin, As always, you have the solution. It was the experimental razor editor that was throwing it off. Jesse

### Response

**Marin Bratanov** answered on 03 Dec 2020

Great to see you have a solution! I have not had much success in using the experimental one either, so I reverted back to the standard one. Regards, Marin Bratanov
