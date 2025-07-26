# How could I format TelerikGrid's paging numbers?

## Question

**Mar** asked on 24 Apr 2024

I have a TelerikGrid with paging enabled. The pager on the left hand side displays the page numbers as buttons, and on the right hand side displays the current items being displayed and the total number of items. The problem is that the right-hand side '1 - 1000 of 440000000' does not format the numbers, and for a grid with millions of possible rows reading the exact numbers is difficult. So I wrote a little javascript to manipulate the dom and format these numbers. In particular I query the document for 'span.k-pager-info' and manipulate the innerText property. This works fine until I filter my grid, at which point it re-fetches data from the db BUT does NOT update that span with the new filtered innerText. In fact, any manipulation with javascript of the 'span.k-page-info' element causes that element to no longer be updated upon filtering data. Why? Is there any other way to format the numbers in the pager so that they display more clearly (ie. 44,000,000)? Much thanks to all.

## Answer

**Tsvetomir** answered on 29 Apr 2024

Hello Marcin, Thank you for the clear explanation of the result you are looking for. To achieve custom formatting of the pager numbers, you can use the CSS rules shown below to create a pseudo element that displays the new custom content. This is useful if you want to make a small change like the desired one. To demonstrate this approach, I've prepared an example for you: <TelerikGrid Data="@GridData" Pageable="true" @bind-Page="@GridPage" PageSize="@GridPageSize" Class="custom-pager-info"> <GridColumns> <GridColumn Field="@nameof(User.Name)" Title="User Name" /> </GridColumns> </TelerikGrid> <style>.custom-pager-info>.k-grid-pager.k-pager-info { font-size: 0;
}. custom-pager-info>.k-grid-pager.k-pager-info::before { font-size: 14px; content: " @GridPagerInfo ";
} </style> @code {
private List <User> GridData { get; set; }

private int GridPage { get; set; }=1;
private int GridPageSize { get; set; }=5;

private int GridTotal=> GridData.Count; private string GridPagerInfo=> $"{(GridPage - 1) * GridPageSize + 1} - {GridPage * GridPageSize} of {GridTotal.ToString("n0")} items"; protected override void OnInitialized()
{
GridData=new List <User> ();
var rnd=new Random();

for (int i=1; i <=20000; i++)
{
GridData.Add(new User()
{
Id=i,
Name="User " + i
});
}
}

public class User
{
public int Id { get; set; }
public string Name { get; set; }
}
} I hope this approach serves you well in continuing with your project. Regards, Tsvetomir Progress Telerik
