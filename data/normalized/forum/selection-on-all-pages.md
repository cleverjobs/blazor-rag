# Selection on All pages

## Question

**Ale** asked on 01 Dec 2020

Hello Marin, Now i have the following: <GridCheckboxColumn SelectAll="true" SelectAllMode="GridSelectAllMode.Current"> it woks will with one thing, if i have several pages i need to go to every page to selected the items, is it possible to have everything that we have using GridSelectAllMode.Current, but also select items thought all pages (GridSelectAllMode.All does not fit due to the ignoring filter)? Thx Alex

## Answer

**Marin Bratanov** answered on 01 Dec 2020

Hi Alex, Thank you for asking for me by name, but I must say I may not be the only person who responds here :) The way things work is important in a couple of ways: when you set the Data property of the grid to have the entire data collection, then selecting all items would literally select all items. when you use OnRead the grid does not have all the data to select for you, so it could only work with the current page that is available. That said, I do see the point of SelectAll taking filtering into account so I logged this for review and implementation here: [https://feedback.telerik.com/blazor/1497485-selectall-header-checkbox-to-take-filtering-into-account.](https://feedback.telerik.com/blazor/1497485-selectall-header-checkbox-to-take-filtering-into-account.) Another change for this could be possible if a HeaderTemplate gets implemented for the selection column so you could write your own select-all logic: [https://feedback.telerik.com/blazor/1497026-add-headertemplate-for-the-gridcheckboxcolumn.](https://feedback.telerik.com/blazor/1497026-add-headertemplate-for-the-gridcheckboxcolumn.) Regards, Marin Bratanov
