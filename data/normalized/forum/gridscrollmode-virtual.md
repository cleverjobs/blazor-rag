# GridScrollMode.Virtual

## Question

**Mar** asked on 22 Apr 2022

I'm using a Grid with GridScrollMode set to Virtual, and a custom filtering function. When the list is filtered and a checkbox is selected the grid reloads and scrolls back to the top of the list. This only happens when Scroll Mode is Virtual. The following example demonstrates the issue. Steps to recreate Load the page Enter a single character in the Filter Criteria box Scroll down the grid for a page or so Check a check box You should be immediately taken back to the to first entry in the filtered list @page "/"

@using Telerik.Blazor.Components;
@using System;
@using System.Text;
@using System.Linq; <PageTitle> Index </PageTitle> <div class="row"> <div class="col-md-6 offset-md-6"> <input type="text" class="form-control" placeholder="Filter Criteria..." @bind="Filter" @bind:event="oninput" /> </div> </div> <div class="row"> &nbsp; </div> <div class="row"> <div class="ac-criteria-list"> <TelerikGrid Data=GetFilteredRows() PageSize="20" Height="295px" RowHeight="50" ScrollMode="@Telerik.Blazor.GridScrollMode.Virtual"> <GridColumns> <GridColumn Field="@(nameof(GridRow.Text))"> <Template> @{
var item=context as GridRow; <input type="checkbox" id="@item.Id.ToString()" @bind="@item.Selected" @key="@item" /> <label for="@item.Id.ToString()"> @item.Text </label> } </Template> </GridColumn> </GridColumns> </TelerikGrid> </div> </div> @code
{
public string Filter { get; set; }=string.Empty;

public List <GridRow> FilteredRows { get; set; }=new();
public List <GridRow> OriginalRows { get; set; }=new();

protected override void OnInitialized()
{
for (var i=0; i <200; i++)
{
OriginalRows.Add(new GridRow
{
Id=i,
Selected=false,
Text=$"{i} - {Utility.GenerateRandomString(10)}"
});
}

FilteredRows=OriginalRows.OrderBy(x=> x.Text).ToList();

base.OnInitialized();
}

private List <GridRow> GetFilteredRows()
{
if (string.IsNullOrWhiteSpace(Filter))
{
return FilteredRows;
}

return FilteredRows.Where(row=> row.Text.Contains(Filter)).ToList();
}

public class GridRow
{
public bool Selected { get; set; }

public int Id { get; set; }

public string Text { get; set; }
}

public class Utility
{
private static char[] _chars=new char[36]
{
'0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
};

public static string GenerateRandomString(int length)
{
StringBuilder stringBuilder=new StringBuilder(length);
Random random=new Random();
for (int i=0; i <length; i++)
{
stringBuilder.Append(_chars[random.Next(_chars.Length)]);
}

return stringBuilder.ToString();
}
}
}

## Answer

**Marin Bratanov** answered on 23 Apr 2022

Hello Mark, This code re-renders the component by changing the Data collection reference, and when it re-renders it re-initializes and so starts from the top as it can't know any better. Perhaps you can save and load the grid state when doing that custom filtering so that the Skip can stay (in virtual scrolling the Skip parameter controls how many rows are scrolled). Regards, Marin Bratanov
