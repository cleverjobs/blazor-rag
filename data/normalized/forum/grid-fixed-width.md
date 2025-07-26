# Grid fixed width

## Question

**Ila** asked on 11 Apr 2021

Is there a way to make the TelerikGrid not Width 100% as on mobile devices it looks very small, I would like it to be scrollable and show the entire header texts

## Answer

**Svetoslav Dimitrov** answered on 13 Apr 2021

Hello Ilan, I would like to offer two different approaches when working with the Grid on mobile devices. Make the Grid horizontally scrollable In order to make the Grid horizontally scrollable, you should set the Width parameter of each column explicitly so that their cumulative sum is greater than the width of the Grid. For example, if the Grid has 10 columns and the Width of the Grid is set to 1000px the sum of the Widths of the columns should be 1000 or more to render a horizontal scrollbar. In order to fully render the Title of the Grid column, you should apply a high enough width so that it incorporates the full length of the text. Use the TelerikMediaQuery component You can use the TelerikMediaQuery component to show or hide different columns based on the browser size. In our Integration documentation article and our live demos, you can see an example of how does the component work together with Grid. Let me know if any of those two suggestions work for you as expected and if you have any further questions. Regards, Svetoslav Dimitrov

### Response

**Ilan** answered on 13 Apr 2021

The problem is that my grid has AutoGenerateColumns="true" so I can't set width to each column individually

### Response

**Svetoslav Dimitrov** answered on 14 Apr 2021

Hello Ilan, I could offer an alternative solution to automatically generate columns. You can use reflection to obtain the properties of your class and use a foreach loop to generate the columns. This would allow you to set a common Width across all Grid columns. Below, I have added an example that you can use as a reference in your own application. <TelerikGrid Data="@GridData" Width="1000px" Pageable="true" PageSize="4">
<GridColumns>
@if(GridData !=null && GridData.Any())
{ var listOfClassProperties=typeof (GridDataModel).GetProperties().Select(p=> p.Name).ToList(); foreach ( var item in listOfClassProperties)
{
<GridColumn Field="@item" Width="200px"></GridColumn>
} }
</GridColumns>
</TelerikGrid>

@code { public class GridDataModel { public int Id { get; set; } public string Username { get; set; } public string EmailAddress { get; set; } public DateTime? RegistrationDate { get; set; } public DateTime? LocalTime { get; set; } public string BoughtBooks { get; set; }=String.Join( ", ", Books);
}

List<GridDataModel> GridData { get; set; }=Enumerable.Range( 1, 15 ).Select(i=> new GridDataModel()
{
Id=i,
Username=$"Username {i} ",
EmailAddress=$"user {i} @mail.com",
RegistrationDate=DateTime.Now.AddDays( -2 ),
LocalTime=DateTime.Now
}).ToList(); static List <string> Books=new List<string>() { "Wolf", "Lord of the Rings", "The Hobbit" };
} Could you get back to me if this solution is viable for you? Regards, Svetoslav Dimitrov
