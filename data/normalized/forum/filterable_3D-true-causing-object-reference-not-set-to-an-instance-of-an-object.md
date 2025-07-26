# Filterable="true" causing Object reference not set to an instance of an object

## Question

**Ale** asked on 10 Jul 2019

Everything is working fine in my Grid, except the Filterable="true". When I set the property to true, the grid throws an exception: Object reference not set to an instance of an object. at Telerik.Blazor.Components.TelerikRootComponentFragmentBase.OnInitAsync() at Microsoft.AspNetCore.Components.ComponentBase.RunInitAndSetParametersAsync() Any help?

## Answer

**Alexandre** answered on 10 Jul 2019

<TelerikGrid Data="@Usuarios?.Resultado" Height="90%" Filterable="true"> <TelerikGridEvents> <EventsManager OnRead=@PopulaUsuarios></EventsManager> </TelerikGridEvents> <TelerikGridColumns> <TelerikGridColumn Field="@(nameof(UsuarioReadModel.Nome))" Title="Nome do usuário" Filterable="true" /> </TelerikGridColumns> </TelerikGrid>

### Response

**Marin Bratanov** answered on 11 Jul 2019

Hi Alexandre, This exception means that the TelerikRootComponent is not added to the root of the layout as described in the second snippet here: [https://docs.telerik.com/blazor-ui/getting-started/what-you-need#project-configuration.](https://docs.telerik.com/blazor-ui/getting-started/what-you-need#project-configuration.) For our next version the exception will be more meaningful. Regards, Marin Bratanov

### Response

**Medhanie** answered on 18 Dec 2019

Hi Marin I also have similar problem, when I add FilterMode="Telerik.Blazor.GridFilterMode.FilterMenu" parameter to my Grid System.NullReferenceException: Object reference not set to an instance of an object. at Telerik.Blazor.Components.RootComponent.TelerikRootComponentFragmentBase.Dispose() I couldn't understand what the error mean. Any help would be appreciated.

### Response

**Marin Bratanov** answered on 19 Dec 2019

Hi Medhanie, This is the first time we get such a report. Can you confirm that you are using the latest version (2.5.1 at the time of writing, and .NET Core 3.1)? If yes, could you open a support ticket and send a runnable sample that showcases this issue so I can investigate? Regards, Marin Bratanov

### Response

**Medhanie** answered on 19 Dec 2019

Hi Marin; Yes I am using latest version but trail one. I'm using Telerik.UI.for.Blezor.Trial (2.5.1) with Core 3.1.0 As you said, I have already created a new ticket, hopping to get some suggestions there. Thank you

### Response

**Marin Bratanov** answered on 19 Dec 2019

Here is a link to the new thread, because it is a public forum [https://www.telerik.com/forums/filtermode=-telerik-blazor-gridfiltermode-filtermenu-getting-me-object-reference-not-set-to-an-instance-of-an-object](https://www.telerik.com/forums/filtermode=-telerik-blazor-gridfiltermode-filtermenu-getting-me-object-reference-not-set-to-an-instance-of-an-object) Regards, Marin Bratanov

### Response

**Mythri** answered on 06 Aug 2020

NullReferenceException: Object reference not set to an instance of an object. Telerik.Blazor.Components.Common.Filters.FilterList.TelerikFilterList.GetFilterOperators() I am gtting this on clicking the filter icon in grid. What might be the issue?

### Response

**Marin Bratanov** answered on 07 Aug 2020

Hello Mythri, My best guess is that the type of the field for this column is not supported (see more here ) - e.g., it is a collection of sorts (List, Dictionary), or a complex object (another model). I'd suggest you open a ticket and send us a simple repro we can run and debug - the grid markup and a basic model that shows the problem would usually suffice. Regards, Marin Bratanov
