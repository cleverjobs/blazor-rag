# Set scrollbar invisible

## Question

**And** asked on 19 Jul 2019

Can I hide vertical scroll bar? In this example scroll bar present but absolutely unusable [https://demos.telerik.com/blazor-ui/grid/custom-editor](https://demos.telerik.com/blazor-ui/grid/custom-editor) Thank you.

## Answer

**Marin Bratanov** answered on 19 Jul 2019

Hello Andriy, You could with CSS, but then the columns would get misaligned. At the moment built-in scrolling settings are not implemented in the grid. Perhaps once virtualization gets implemented we will see how that can be exposed for configuration, but at the moment we don't want to make rash decisions that we may have to break later. Regards, Marin Bratanov

### Response

**Sean** answered on 03 Oct 2019

Does this mean my non functional vertical scroll is supposed to be that way?

### Response

**Marin Bratanov** answered on 04 Oct 2019

Hi Sean, For the time being - yes. We have not gotten to implementing scrolling as a feature in the grid and the current solution is the most stable that requires no configuration and tweaks on your part. Once more scrolling options start becoming available, I expect there will be a way to get rid of it. Regards, Marin Bratanov

### Response

**Roger** answered on 21 Jan 2020

Is there a way to remove the horizontal scrollbar in a TelerikGrid yet?

### Response

**Marin Bratanov** answered on 21 Jan 2020

Hi Roger, The horizontal scrollbar is shown only when the combined column widths are larger than the grid width: [https://docs.telerik.com/blazor-ui/components/grid/columns/width.](https://docs.telerik.com/blazor-ui/components/grid/columns/width.) While an out-of-the-box feature for stopping it does not exist (and that would likely be detrimental to the user experience), you could find the scrollbable element by inspecting the rendered DOM with the browser dev toolbar, and devise a CSS rule that will prevent it from having the horizontal scrollbar (you could cascade it through a specific Class on the grid to make it target only specific instances). Regards, Marin Bratanov

### Response

**Roger** answered on 21 Jan 2020

I am sorry, I meant the vertical scroll bar. Is there a way to remove that?

### Response

**Marin Bratanov** answered on 22 Jan 2020

Hello Roger, At the moment, it is not possible to hide it out-of-the-box. You could add CSS to remove it, but you'd also have to add CSS to remove the padding-right on the header. Here is an example: <style>.no-scroll.k-grid-content { overflow-y: hidden;
}.no-scroll.k-grid-header { padding-right: 0!important;
}.no-scroll.k-grid-header-wrap { border-width: 0px!important;
} </style> <TelerikGrid Data="@MyData" Class="no-scroll" Pageable="true" Sortable="true" Groupable="true" FilterMode="Telerik.Blazor.GridFilterMode.FilterRow" Resizable="true" Reorderable="true"> <GridColumns> <GridColumn Field="@(nameof(SampleData.Id))" Width="120px" /> <GridColumn Field="@(nameof(SampleData.Name))" Title="Employee Name" Groupable="false" /> <GridColumn Field="@(nameof(SampleData.Team))" Title="Team" /> <GridColumn Field="@(nameof(SampleData.HireDate))" Title="Hire Date" /> </GridColumns> </TelerikGrid> @code {
public IEnumerable <SampleData> MyData=Enumerable.Range(1, 30).Select(x=> new SampleData
{
Id=x,
Name="name " + x,
Team="team " + x % 5,
HireDate=DateTime.Now.AddDays(-x).Date
});

public class SampleData
{
public int Id { get; set; }
public string Name { get; set; }
public string Team { get; set; }
public DateTime HireDate { get; set; }
}
} Regards, Marin Bratanov

### Response

**Roger** answered on 22 Jan 2020

Thanks for responding and providing an example. Appreciated.

### Response

**Flemming** answered on 19 Apr 2021

Thanks. Any idea of ETA on this as build-in feature?

### Response

**Marin Bratanov** answered on 19 Apr 2021

Hi Flemming, This isn't planned as a built-in feature. The scrollbar is taken into account by the grid as it will show up quite often at runtime (e.g., if you group a grid with a preset height). If you are OK with the risks of misaligning the column headers when you hide the scorllbar, doing so with CSS is a perfectly valid approach. Regards, Marin Bratanov

### Response

**Flemming** answered on 19 Apr 2021

Ok, thx Marin :)

### Response

**Marat** commented on 12 May 2023

Hello, Is there any way of hiding the horizontal scrollbar only of Telerik's Blazor grid as of today? The reason it's needed is that the grid's footer is sticky - when you scroll horizontally, it does not move, while the grid's header and main content are scrolled, which can confuse users. Alternatively, as a workaround, is there any way to determine programmatically if the horizontal scrollbar is present in Telerik's Blazor grid so that users can be warned about it and its related side effect? Kind regards, Marat.

### Response

**Nadezhda Tacheva** commented on 17 May 2023

Hi Marat, If I correctly understand, you want to hide this scrollbar: Is that correct? By design, this horizontal scrollbar appears when the cumulative width of the Grid columns is higher than the Grid width. Its purpose is to allow the user to scroll horizontally in order to view the columns that are not visible in the current view. In case you hide this scrollbar, the users will not be able to scroll the Grid on desktop to see its full content. Can you please share more details on how this would improve the user experience? Or, is there any aspect that I am missing in the scenario? Thank you in advance!
