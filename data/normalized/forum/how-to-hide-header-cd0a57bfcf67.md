# How to: Hide Header?

## Question

**benben** asked on 16 May 2020

Is there a way to hide the header? I'm trying to use the Grid as a ListBox and it almost works using an empty span for the <HeaderTemplate> <TelerikGrid SelectionMode="@GridSelectionMode.Multiple" Data=@AvailableSerialNumbers Pageable="false" Sortable="false" SelectedItemsChanged="@((IEnumerable<TSerialNumberDto> serialNumbers)=> OnSelectSerialNumbers(serialNumbers))" SelectedItems="@SelectedSerialNumbers"> <GridColumns> <GridColumn Field="Number"> <HeaderTemplate> <span class="k-display-flex k-align-items-center"> </span> </HeaderTemplate> </GridColumn> </GridColumns> </TelerikGrid> However it leaves just a little bit of a bar at the very top that I can't get rid up...seems like there should be a way to hide that.

## Answer

**Marin Bratanov** answered on 18 May 2020

Hello Ben, I made the following page that you can use the track the status of a feature for this, and I added a solution for the time being (a line of CSS): [https://feedback.telerik.com/blazor/1467583-ability-to-hide-the-header-row](https://feedback.telerik.com/blazor/1467583-ability-to-hide-the-header-row) Regards, Marin Bratanov
