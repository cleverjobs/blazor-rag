# Accessing property(s) from MainLayout.razor(.cs) within other pages

## Question

**Doo** asked on 30 Jul 2021

I am trying to use Telerik Blazor's MediaQuery at the base page. That page, for me is, MainLayout.razor. First, I separated the code-behind for the MainLayout and had to introduce a base class for my properties as MainLayout already inherits LayoutComponentBase: MainLayout.razor @using DA.BrrMs.Portal.Blazor.Helpers

@inherits MainLayoutModel

@layout TelerikLayout <TelerikMediaQuery Media="@WindowBreakPoints.ExtraSmall" OnChange="@(matches=> IsExtraSmall=matches )" /> <TelerikMediaQuery Media="@WindowBreakPoints.Small" OnChange="@(matches=> IsSmall=matches )" /> <TelerikMediaQuery Media="@WindowBreakPoints.Medium" OnChange="@(matches=> IsMedium=matches )" /> <TelerikMediaQuery Media="@WindowBreakPoints.Large" OnChange="@(matches=> IsLarge=matches )" /> <TelerikMediaQuery Media="@WindowBreakPoints.ExtraLarge" OnChange="@(matches=> IsExtraLarge=matches )" /> <Header @bind-StateCssClass="@NavMenuCssClass"> </Header> <div class="main"> <div class="sidebar @NavMenuCssClass"> <NavMenu /> </div> <div class="container-fluid px-2"> @Body </div> </div> MainLayout.razor.cs using DA.BrrMs.Portal.Blazor.Base; namespace DA.BrrMs.Portal.Blazor.Shared { public class MainLayoutModel: BaseLayout { protected string NavMenuCssClass { get; set; }
}
} BaseLayout.cs using Microsoft.AspNetCore.Components; namespace DA.BrrMs.Portal.Blazor.Base { public class BaseLayout: LayoutComponentBase { protected bool IsExtraSmall { get; set; } protected bool IsSmall { get; set; } protected bool IsMedium { get; set; } protected bool IsLarge { get; set; } protected bool IsExtraLarge { get; set; }
}
} With this done, at very late hours, I realized there is no code level link between a MainLayout and any other page and I cannot access the IsSmall property in my dashboard page. I need to change the layout itself is screen is small or less for my mobile clients and that's another reason for me doing this at MainLayout level Any proper way to accomplish this?

## Answer

**DoomerDGR8** answered on 01 Aug 2021

With all the useful inputs ad a bit of late night blazor tutorials, I finally figured out the case. I learned that cascading parameter are bound by type of parameter. I was getting a strange behavior where on the actual pages, the wrong Booleans were getting set. I learned that we can also Name the parameter explicitly. So, here is the final working code: Helper class: namespace DA.BrrMs.Portal.Blazor.Helpers { public static class WindowBreakPoints { public static string ExtraSmall=> "(max-width: 480px)"; public static string Small=> "(max-width: 767px)"; public static string Medium=> "(max-width: 1023px)"; public static string Large=> "(max-width: 1199px)"; public static string ExtraLarge=> "(min-width: 1200px)";
}
} MainLayout.razor: @using DA.BrrMs.Portal.Blazor.Helpers

@layout TelerikLayout

@inherits MainLayoutModel <TelerikMediaQuery Media="@WindowBreakPoints.ExtraSmall" OnChange="@(matches=> IsExtraSmall=matches )" /> <TelerikMediaQuery Media="@WindowBreakPoints.Small" OnChange="@(matches=> IsSmall=matches )" /> <TelerikMediaQuery Media="@WindowBreakPoints.Medium" OnChange="@(matches=> IsMedium=matches )" /> <TelerikMediaQuery Media="@WindowBreakPoints.Large" OnChange="@(matches=> IsLarge=matches )" /> <TelerikMediaQuery Media="@WindowBreakPoints.ExtraLarge" OnChange="@(matches=> IsExtraLarge=matches )" /> <Header @bind-StateCssClass="@NavMenuCssClass"> </Header> <div class="main"> <div class="sidebar @NavMenuCssClass"> <NavMenu /> </div> <div class="container-fluid px-2"> <CascadingValue Value="@IsExtraSmall" Name="UiIsExtraSmall"> <CascadingValue Value="@IsSmall" Name="UiIsSmall"> <CascadingValue Value="@IsMedium" Name="UiIsMedium"> <CascadingValue Value="@IsLarge" Name="UiIsLarge"> <CascadingValue Value="@IsExtraLarge" Name="UiIsExtraLarge"> @Body </CascadingValue> </CascadingValue> </CascadingValue> </CascadingValue> </CascadingValue> </div> </div> MainLayout.razor.cs: using DA.BrrMs.Portal.Blazor.Base; namespace DA.BrrMs.Portal.Blazor.Shared { public class MainLayoutModel: BaseLayout { protected string NavMenuCssClass { get; set; }
}
} BaseLayout.cs: using Microsoft.AspNetCore.Components; namespace DA.BrrMs.Portal.Blazor.Base { public class BaseLayout: LayoutComponentBase {
[ CascadingParameter(Name="UiIsExtraSmall" ) ] protected bool IsExtraSmall { get; set; }

[ CascadingParameter(Name="UiIsSmall" ) ] protected bool IsSmall { get; set; }

[ CascadingParameter(Name="UiIsMedium" ) ] protected bool IsMedium { get; set; }

[ CascadingParameter(Name="UiIsLarge" ) ] protected bool IsLarge { get; set; }

[ CascadingParameter(Name="UiIsExtraLarge" ) ] protected bool IsExtraLarge { get; set; }
}
} Notice that each Cascading Parameter now had a name attribute as well. With the above code, we have the five Booleans ready to be used application wide. Dashboard.razor: @page "/"
@page "/dashboard"

@inherits DashboardModel

@attribute [Authorize] <PageHeader PageTitle="Dashboard" AreaName="Request"> </PageHeader> @if (IsExtraSmall || IsSmall || IsMedium)
{ <TelerikTileLayout Columns="2" ColumnWidth="50%" RowHeight="250px" Reorderable="true" Resizable="true" Class="myTileLayout" ColumnSpacing="2px" RowSpacing="2px" OnResize="@ItemResize"> <TileLayoutItems> </TileLayoutItems> </TelerikTileLayout> }
else
{ <TelerikTileLayout Columns="6" ColumnWidth="20%" RowHeight="235px" Reorderable="true" Resizable="true" Class="myTileLayout" ColumnSpacing="4px" RowSpacing="4px" OnResize="@ItemResize"> <TileLayoutItems> </TileLayoutItems> </TelerikTileLayout> } Dashboard.razor.cs: using Microsoft.AspNetCore.Components; namespace DA.BrrMs.Portal.Blazor.Pages { public class DashboardModel: BasePage { protected override async Task OnInitializedAsync ( ) { await base.OnInitializedAsync();
}

}
} BasePage.cs: using Microsoft.AspNetCore.Components; namespace DA.BrrMs.Portal.Blazor.Base { public class BasePage: ComponentBase {
[ CascadingParameter ] public DialogFactory Dialogs { get; set; }

[ CascadingParameter(Name="UiIsExtraSmall" ) ] protected bool IsExtraSmall { get; set; }

[ CascadingParameter(Name="UiIsSmall" ) ] protected bool IsSmall { get; set; }

[ CascadingParameter(Name="UiIsMedium" ) ] protected bool IsMedium { get; set; }

[ CascadingParameter(Name="UiIsLarge" ) ] protected bool IsLarge { get; set; }

[ CascadingParameter(Name="UiIsExtraLarge" ) ] protected bool IsExtraLarge { get; set; } protected override async Task OnInitializedAsync ( ) { await base.OnInitializedAsync();
}
}
} All my pages and components are also inheriting a base page. I declared the cascading parameters again in this base page with same signature (copy-paste from BaseLayout).

### Response

**Blazorist** commented on 06 Aug 2021

Sorry, when I copy and paste the code there was still working on it. I realized about the name property of the Cascade Parameters but you already figure it out. I used a very similar approach in my solution. Bye.

### Response

**Matthias** answered on 30 Jul 2021

Hi Hassan, there are several possibilities. For example, I use for communication between the other components: "Cascading Values" but also SignalIR=> Info. Also possible is a "state container" (just a class injected as a singleton or scoped service)=> Info Regards Matthias

### Response

**DoomerDGR8** commented on 30 Jul 2021

For the usage I seek, SignalR and State Container seems like over engineering. I'm hoping you can give an example in context of Cascading Parameters showing a variable defined in MainLayout being accessed by other pages because I have seen the reverse examples a lot but I have the specific requirement.

### Response

**Matthias** commented on 30 Jul 2021

You can read it in the documentation There is also a good example: [https://docs.microsoft.com/en-us/aspnet/core/blazor/components/cascading-values-and-parameters?view=aspnetcore-5.0](https://docs.microsoft.com/en-us/aspnet/core/blazor/components/cascading-values-and-parameters?view=aspnetcore-5.0)

### Response

**Blazorist** answered on 30 Jul 2021

Hi Hassan. Add this to MainLayout.razor markup: <CascadingValue Value=@IsExtraSmall> <CascadingValue Value=@IsSmall> <CascadingValue Value=@IsMedium> <CascadingValue Value=@IsLarge> <CascadingValue Value=@IsExtraLarge> @Body </CascadingValue> </CascadingValue> </CascadingValue> </CascadingValue> </CascadingValue> and this to the code-behind: @{ protected bool IsExtraSmall { get; set; } protected bool IsSmall { get; set; } protected bool IsMedium { get; set; } protected bool IsLarge { get; set; } protected bool IsExtraLarge { get; set; }
} So, we got the CascadingParameter defined. If you wanna use this parameters in your hierachy of components I suggest add the references to the cascade parameters in your parent class: BaseLayout as follows: [ CascadingParameter ] protected bool IsExtraSmall { get; set; }
[ CascadingParameter ] protected bool IsSmall { get; set; }
[ CascadingParameter ] protected bool IsMedium { get; set; }
[ CascadingParameter ] protected bool IsLarge { get; set; }
[ CascadingParameter ] protected bool IsExtraLarge { get; set; } Hope that help.

### Response

**DoomerDGR8** commented on 30 Jul 2021

This is awesome. Now, one last thing that I'm trying to comprehend is that the MainLayout inherit my custom BaseLayout that inherits LayoutComponentBase but all other application pages are inheriting from my custom BasePage that inherits ComponentBase. So, there is a divide here: I'm still not able to get access to IsExtraSmall or IsSmall in any of my actual pages.

### Response

**Blazorist** commented on 31 Jul 2021

Yes, you're right. You still can define the [Cascading Parameter] in any component that need access to IsExtraSmall or IsSmall values.
