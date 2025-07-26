# grid not working

## Question

**n/an/a** asked on 31 Jan 2022

Hi there, I'm new at telerik and I'm trying to use the grid component. unfortunately i keep getting this error: Unhandled exception rendering component: Could not find 'TelerikBlazor.initGrid' ('TelerikBlazor' was undefined). Error: Could not find 'TelerikBlazor.initGrid' ('TelerikBlazor' was undefined). I have installed telerik.ui.for.blazor in both Client and Server projects. I have installed telerik.ui.for.blazor as i couldn't find anywhere in the documentation the specific packaged that needs to be installed in order to start using the components and I thought the aforementioned should be the right one. Please find below code inside the component: <Telerik.Blazor.Components.TelerikGrid Data="@Books"> <GridColumns> <Telerik.Blazor.Components.GridColumn Field="@nameof(Book.Name)"></Telerik.Blazor.Components.GridColumn> </GridColumns> </Telerik.Blazor.Components.TelerikGrid> Please note that using only <TelerikGrid></TelerikGrid> is not permitted by the project. Any help would be appreciated. Or if you could please specify which package needs to be installed (in case I have installed the wrong package) Thank you very much. Kind regards

### Response

**n/a** commented on 31 Jan 2022

I've also added this in the startup.cs (Server): public void ConfigureServices(IServiceCollection services) { ... services.AddTelerikBlazor(); ... }

## Answer

**n/a** answered on 31 Jan 2022

Never mind, I have just found in the documentation at GETTING STARTED all the necessary documentation and now it works! Thanks
