# How do you get the filter menu in a Grid to be ordered?

## Question

**Jer** asked on 16 Feb 2022

I set a Grid to have the property FilterMode="@GridFilterMode.FilterMenu" and find that the items in the filter for the column are not ordered ascending. How can I assure that the filter menu list is ordered? <GridColumn Field="@nameof(PackageRequest.Product)" Title="Product" Width="120px"> <Template> @{ var item=context as PackageRequest; @item.Product } </Template> </GridColumn>

## Answer

**Marin Bratanov** answered on 17 Feb 2022

Hi, You can Follow the implementation of such functionality here: [https://feedback.telerik.com/blazor/1504816-sorted-checkboxlistfilter-by-default.](https://feedback.telerik.com/blazor/1504816-sorted-checkboxlistfilter-by-default.) Regards, Marin Bratanov Progress Telerik
