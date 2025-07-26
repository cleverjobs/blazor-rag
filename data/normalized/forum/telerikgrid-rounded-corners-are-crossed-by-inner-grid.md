# TelerikGrid rounded corners are crossed by inner grid

## Question

**Ric** asked on 20 Jun 2023

I want to create a table with TelerikGrid whose border corners are rounded (border-radius: 8px). However, I noticed that the corners are under the table's sharp corners as exemplified in the files below. My TelerikGrid is as follows: <span> <TelerikGrid Data=@GridData> <GridColumns> <GridColumn Width="5%" /> <GridColumn Field="@nameof(...)" /> <GridColumn Field="@nameof(...)" /> <GridColumn Field="@nameof(...)" /> <GridColumn Field="@nameof(...)" /> <GridColumn Field="@nameof(...)" /> </GridColumns> </TelerikGrid> </span> and its css rules in the corresponding razor.css (wrapped the telerik component within a span tag so as to use the ::deep selector): ::deep .k-grid{ width: 100%; height: 100%; border: 1px solid #6495Ed4D; border-radius: 8px; opacity: 1;
} Is there a way to the Grid's border to be on top for the rest of the component?

## Answer

**Radko** answered on 22 Jun 2023

Hello Ricardo, The needed CSS might differ based on all the settings the Grid has currently enabled(e.g. Grouping, Toolbar, etc are just some of the elements that might render above the Grid), but for a rather straightforward config as per the snippet you have proposed, something like this should do the trick: [https://blazorrepl.telerik.com/GHOUmQPc105NQvQp44.](https://blazorrepl.telerik.com/GHOUmQPc105NQvQp44.) Regards, Radko
