# Dropdownlist will not dropdown

## Question

**Rob** asked on 04 Oct 2019

I have tried to implement the dropdownlist and the data is being populated to the control, but the control will not dropdown when selected on. I have tried to changed from Server/Prerender and also tried a static list. I also have the same issues with Telerik menus. What do I have configured wrong. Running Blazor UI 2.1.1 <TelerikDropDownList Data="@DropDownListData" @bind-Value=@SelectedValue ValueField="ID" TextField="Organization"> </TelerikDropDownList> <br />Selected product: @SelectedValue @code { public IEnumerable<OrgModel> DropDownListData { get; set; } public int SelectedValue { get; set; }=3; WeatherForecast[] forecasts; OrgModel[] Orgs; protected override async Task OnInitializedAsync() { forecasts=await ForecastService.GetForecastAsync(DateTime.Now); DropDownListData=await OrgService.Get_OrgList_Async(); } //protected async Task OnAfterRenderAsync() //{ // forecasts=await ForecastService.GetForecastAsync(DateTime.Now); // DropDownListData=await OrgService.Get_OrgList_Async(); //}

## Answer

**Marin Bratanov** answered on 06 Oct 2019

Hello Robert, There is nothing obviously wrong in this snippet and my best guess is that one of the following issues is manifesting in the project: there is no <TelerikRootComponent> in the root of the layout, and it is required for popups to work: [https://docs.telerik.com/blazor-ui/getting-started/what-you-need#project-configuration.](https://docs.telerik.com/blazor-ui/getting-started/what-you-need#project-configuration.) the JS Interop file is not being fetched properly, you can read more about it here: [https://docs.telerik.com/blazor-ui/upgrade/overview#microsoftjsinteropjsexception-could-not-find-.](https://docs.telerik.com/blazor-ui/upgrade/overview#microsoftjsinteropjsexception-could-not-find-.) Both will cause errors in the console, so you can monitor it to see the details. Regards, Marin Bratanov

### Response

**Robert** answered on 07 Oct 2019

Thank you for the help and pointing me the in the right direction. I was fetching the incorrect JS interop file.

### Response

**BitShift** answered on 30 Oct 2019

Glad I found this thread, I was running into the same issue.
