# passing parameter to click event on row template

## Question

**EdEd** asked on 14 Jan 2020

Hi, I am having trouble getting cell specific data in response to a click event on an href that is defined in my row template. Below is a rough idea of what I am doing. <RowTemplate Context="rowCtx"> <td> <a href="#" id="@(rowCtx.CellSpecificId1)" @onclick="@(e=> HandleClick(rowCtx.CellSpecificId)" @onclick:preventDefault> </td> <td> <a href="#" id="@(rowCtx.CellSpecificId2)" @onclick="@(e=> HandleClick(rowCtx.CellSpecificId)" @onclick:preventDefault> </td> <td> <a href="#" id="@(rowCtx.CellSpecificId3)" @onclick="@(e=> HandleClick(rowCtx.CellSpecificId)" @onclick:preventDefault> </td> </RowTemplate> The problem seems to be that no matter what, the LAST rowCtx.CellSpecificId is passed to my event handler instead of the cell I want. In the code above, if I click on teh first href, in the first <td>, I get the CellSpecificId3 instead of 1 Can someone share with me how to get a specific cell's value/id/whatever passed to the event handler? Seems like this should be easy, but it's not. Basically, I want to pop a dialog that displays info for a clicked on cell. I am not married to the anchor tag. If there is a better way (i.e. one that works!), I'm all ears. Thanks ... Ed

## Answer

**Marin Bratanov** answered on 14 Jan 2020

Hello Ed, Here are the problems I can see in this code: the anchor tags are not closed the @() expression for the @onclick handler is missing its closing bracket all the @onclick handlers receive the same argument, so it's expected that the HandleClick method receives the same info for each cell in the row That said, here's an example I made for you that fixes those issues and seems to work fine for me (I highlighted the key changes that fix the issue, the rest is data and sample logic for handling the click): @result

<TelerikGrid Data=@MyData Height="500px">
<RowTemplate Context="rowCtx">
<td>
<a href="#" id="@(rowCtx.CellSpecificId1)" @onclick="@(e=> HandleClick(rowCtx.CellSpecificId 1 ) ) " @onclick:preventDefault> first</a> </td>
<td>
<a href="#" id="@(rowCtx.CellSpecificId2)" @onclick="@(e=> HandleClick(rowCtx.CellSpecificId 2 ) ) " @onclick:preventDefault> second</a> </td>
<td>
<a href="#" id="@(rowCtx.CellSpecificId3)" @onclick="@(e=> HandleClick(rowCtx.CellSpecificId 3 ) ) " @onclick:preventDefault> third</a> </td>
</RowTemplate>
<GridColumns>
<GridColumn Field=@nameof (SampleData.CellSpecificId1) Title="First" />
<GridColumn Field=@nameof (SampleData.CellSpecificId2) Title="Second" />
<GridColumn Field=@nameof (SampleData.CellSpecificId3) Title="Third" />
</GridColumns>
</TelerikGrid>

@code { string result; void HandleClick ( string cellId ) {
result=$"last click was on {cellId} at {DateTime.Now} ";
} public class SampleData { public int Id { get; set; } public string CellSpecificId1 { get; set; } public string CellSpecificId2 { get; set; } public string CellSpecificId3 { get; set; }
} public IEnumerable<SampleData> MyData=Enumerable.Range( 1, 50 ).Select(x=> new SampleData
{
Id=x,
CellSpecificId1="one" + x,
CellSpecificId2="two" + x,
CellSpecificId3="three" + x
});
} You may also find useful this example on showing a custom popup for grid records: [https://github.com/telerik/blazor-ui/tree/master/grid/custom-popup-form](https://github.com/telerik/blazor-ui/tree/master/grid/custom-popup-form) Regards, Marin Bratanov

### Response

**Ed** answered on 14 Jan 2020

Thanks so much! The code I posted wasn't the real code and of course I screwed it up. I'll look more closely at what you did and get back to you. THanks ... Ed

### Response

**Marin Bratanov** answered on 14 Jan 2020

Sure, Ed, take your own time. I just had to point out every issue I see to be on the safe side. --Marin
