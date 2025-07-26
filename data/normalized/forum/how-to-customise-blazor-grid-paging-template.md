# How to customise Blazor Grid paging template

## Question

**CJCJ** asked on 10 Apr 2025

We want to customise the controls inside the Grid's pager. With the following settings it's generating what's in the actual.png. We would like to achieve the template in required.png. Is it possible to move the controls and change the content inside the pager? <GridSettings> <GridPagerSettings InputType="PagerInputType.Input" PageSizes="@PageSizes" ButtonCount="5" Adaptive="true" Position="PagerPosition.Bottom"> </GridPagerSettings> </GridSettings>

## Answer

**Anislav** answered on 11 Apr 2025

You can customize the Grid's pager using custom CSS or by applying a theme. However, reordering the built-in pager controls is not supported. If you'd like a more customized pager, you can use a custom pager template, which is supported. You can find an example here: [https://www.telerik.com/blazor-ui/documentation/components/grid/templates/pager.](https://www.telerik.com/blazor-ui/documentation/components/grid/templates/pager.) Keep in mind, though, that using a custom pager template means you'll need to handle most of the work yourself. As for the issue with the Pager dropdown width, you can apply the fix outlined here: [https://www.telerik.com/blazor-ui/documentation/knowledge-base/pager-dropdown-width](https://www.telerik.com/blazor-ui/documentation/knowledge-base/pager-dropdown-width) Regards, Anislav Atanasov
