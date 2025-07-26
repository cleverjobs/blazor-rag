# Centering GridCheckBoxColumn

## Question

**Bob** asked on 26 Oct 2021

I am coming up to speed on using Blazor with little other web experience, so the answer probably a gap in my knowledge that is right in front of me and I can't see it... that being said: I have a fairly standard DataGrid (included below), and it has been requested that the GridCheckBoxColumn have the checkbox centered. For other items requiring some kind of formatting, I would just template the column with a <div> and handle things. However, I could not find anything on how to manipulate the GridCheckBoxColumn other than the OnCellRender event. I have been able to verify I am receiving the event by changing the background color, but I have not found anything that will center the checkbox Thanks! Bob <TelerikGrid Data=@lstGridData SelectionMode="GridSelectionMode.Single" Pageable="true" SelectedItemsChanged="@((IEnumerable<CEnterprise> enterprises)=> OnSelect(enterprises))" Width="100%" PageSize="12"> <GridToolBar> <TelerikButton OnClick="@( ()=> EnterpriseEdit(null) )" Icon="add">Add new Enterprise</TelerikButton> </GridToolBar> <GridColumns> <GridCheckboxColumn SelectAll="false" Title="Select" OnCellRender="@( (e)=> MakeItCentered(e) )" /> <GridColumn Field="EnterpriseName" Title="Name" /> <GridColumn Field="DisplayLocation" Title="Location" /> <GridColumn Field="ContactName1" Title="Contact" /> <GridColumn Field="ContactName2" Title="Contact 2" /> <GridCommandColumn Title="Edit" Width="8%" Context="ctxAuthorizeViewRender"> <GridCommandButton OnClick="@((args)=> EnterpriseEdit(args.Item as CEnterprise))" Icon="edit">Edit</GridCommandButton> </GridCommandColumn> </GridColumns> </TelerikGrid> @Code { void MakeItCentered(GridCellRenderEventArgs args) { args.Class="tiddleywinks"; } }

## Answer

**Dimo** answered on 27 Oct 2021

Hello Bob, By default, the Grid is affected by the following CSS rule in our theme: .k-grid th,.k-grid td { text-align: inherit;
} The CSS specificity of the above selectors is 0,0,1,1. In order to override the style and apply custom text alignment, you will need a selector with greater specificity, for example 0,0,2,0 or 0,0,1,2. /* 0,0,2,0 */.k-grid.tiddleywinks { text-align: center;
} /* OR */ /* 0,0,1,2 */ tr td.tiddleywinks { text-align: center;
} On a side note, currently there is no way to apply a custom CSS class to header cells. If you decide to use a "Select All" checkbox, there are two other options to center: Set a smaller width to the checkbox column, e.g. around 40px. Use a custom CSS rule that targets the first column, no matter what it is: .k-grid th:first-child,.k-grid td:first-child { text-align: center;
} Regards, Dimo

### Response

**Bob Nonnemann** commented on 23 Nov 2021

Belatedly, thank you!
