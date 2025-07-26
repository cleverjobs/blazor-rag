# Upgrade to 3.6.0 results in Grid Pager not rendering correctly

## Question

**EdEd** asked on 20 Sep 2022

When I upgraded to 3.6.0 my TelerikGrid pager stopped rendering correctly. The first image below is after the page has been rendered and the data source contains 10 rows. Paging is enabled using a server-side data source/database repository. The second image below is simply what it looks like when I click on the dropdown. If I hit refresh I see the normal-looking pager with 7 buttons horizontal as expected. Like the one that works with version 3.5.0, included below. But it only appears for a second and then it changes back to the one above. The grid OnReadHandler looks like this: protected async Task OnReadHandler ( GridReadEventArgs args ) { InquiryResponse <Drug> response=await _drugAdapter. FindByDataSourceRequestAsync (args. Request, true ); if ( response. ResponseData. Any ()) { args. Data=response. ResponseData; } args. Total=response. AvailableTotalItems; } All downstream methods are async and await is used on all method calls just like I have seen in the demos for using remote data service. The grid is defined as follows: <TelerikGrid @ref=" @DrugListGridRef " TItem=" @Drug " OnRead=" @OnReadHandler " Sortable="true" SortMode=" @SortMode. Multiple " EnableLoaderContainer="false" FilterMode=" @GridFilterMode. FilterMenu " Pageable="true" PageSize=" @PageSize " Resizable="true"> <GridSettings> <GridPagerSettings InputType=" PagerInputType. Buttons " PageSizes=" @PageSizes " ButtonCount="7" Adaptive="true"> </GridPagerSettings> </GridSettings> If I downgrade to 3.5.0 everything works as expected. Thanks, Ed

### Response

**Martin** commented on 21 Sep 2022

Following, same problem here

## Answer

**Joana** answered on 22 Sep 2022

Hi everyone, Please make sure that you use the latest version of the integrated themes of Telerik UI for Blazor. We recommend the usage of the themes that are part of the nuget as static assets. However, if you use a local copy of the themes, or a cdn , you need to update it. You can find more information in our documentation: [https://docs.telerik.com/blazor-ui/styling-and-themes/overview](https://docs.telerik.com/blazor-ui/styling-and-themes/overview) If the app is created by the Telerik VS extensions, the styles added to the app need to be updated. We have released an Update Project Wizard to facilitate the process. If the theme is created by the ThemeBuilder app, use the associated json file to import in our new ThemeBuilder. In the past months we have been working hard on improving our ThemeBuilder. We provided more customization options and tremendously improved the performance and UX of the application. So, in order to update the theme: [https://themebuilder.telerik.com/blazor-ui](https://themebuilder.telerik.com/blazor-ui) 1. Go to the ThemeBuilder app 2. Log in with your credentials 3. Import the json file through Themes Styles dropdown You might find useful our release notes and demo site: [https://www.telerik.com/support/whats-new/blazor-ui/release-history/ui-for-blazor-3-6-0](https://www.telerik.com/support/whats-new/blazor-ui/release-history/ui-for-blazor-3-6-0) [https://demos.telerik.com/blazor-ui](https://demos.telerik.com/blazor-ui) [https://docs.telerik.com/blazor-ui/upgrade/rendering-changes/3-6-0](https://docs.telerik.com/blazor-ui/upgrade/rendering-changes/3-6-0) Regards, Joana

### Response

**Ed** commented on 22 Sep 2022

Thank you for your help. I was able to run the upgrade tool however, I still needed to manually edit the _Layout.cshtml file to point to the correct, versioned, CSS theme files. using the links you provided. I switched to the CDN version to stay current. Always a pleasure working with Telerik support :) :) Thanks again, Ed
