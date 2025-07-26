# Grid OnRowClick event for middle mouse button click

## Question

**Len** asked on 25 Jan 2024

Hi, Any way to have an event callback when clicking a row in the TelerikGrid with middle mouse button? Looks like the OnRowClick event is only triggered when using left mouse button. KR, Lennert

## Answer

**Hristian Stefanov** answered on 30 Jan 2024

Hi Lennert, I confirm that it is possible to handle the middle mouse button click on a row. To achieve this, leverage the RowTemplate of the Grid component, allowing you to manage the " onmousedown " event. I have prepared an example for you that demonstrates this approach: <TelerikGrid Data=@MyData Height="500px"> <RowTemplate Context="employee"> <td @onmousedown="OnMouseDown"> <strong> @employee.Name </strong> </td> <td @onmousedown="OnMouseDown"> Hired on: @(String.Format("{0:dd MMM yyyy}", employee.HireDate)) </td> </RowTemplate> <GridColumns> <GridColumn Field=@nameof(SampleData.Name) Title="Employee Name" /> <GridColumn Field=@nameof(SampleData.HireDate) Title="Hire Date" /> </GridColumns> </TelerikGrid> @code { private void OnMouseDown(MouseEventArgs e)
{
// Check if the middle mouse button is clicked (button value of 1)
if (e.Button==1)
{
// Handle middle mouse button click
// Your custom logic here
Console.WriteLine("Middle mouse button clicked!");
}
} public class SampleData
{
public int ID { get; set; }
public string Name { get; set; }
public DateTime HireDate { get; set; }
}

private IEnumerable <SampleData> MyData=Enumerable.Range(1, 50).Select(x=> new SampleData
{
ID=x,
Name="name " + x,
HireDate=DateTime.Now.AddDays(-x)
});
} Regards, Hristian Stefanov Progress Telerik

### Response

**Lennert** commented on 30 Jan 2024

Hi Hristian, Unfortunately we can't implement a RowTemplate to resolve this, since we make extensive use of GridColumn templates. From what I can find, the two can not be combined, correct? Any other suggestions? KR, Lennert

### Response

**Hristian Stefanov** commented on 02 Feb 2024

Hi Lennert, I confirm that your observations are correct. In this scenario, an alternative method to address the middle mouse button click is to use a concise JavaScript function. This function can listen for the "mousedown" event across the page and handle interactions with the Grid rows. I've crafted an illustrative example to showcase the implementation of this approach below. It's important when you are testing it to change the " YourAssemblyName " text in the JS function to the actual name of your project. @inject IJSRuntime JSRuntime; <TelerikGrid Data=@MyData Height="500px"> <GridColumns> <GridColumn Field=@nameof(SampleData.Name) Title="Employee Name" /> <GridColumn Field=@nameof(SampleData.HireDate) Title="Hire Date" /> </GridColumns> </TelerikGrid> <script suppress-error="BL9992"> document.addEventListener( "mousedown", function ( e ) { let element=e.target.closest( "tr.k-master-row" ); if (e.which==2 && element) { let rowRenderId=element.getAttribute( "data-render-row-index" );

DotNet.invokeMethodAsync( " YourAssemblyName ", "OnMouseDown", rowRenderId);
}
}); </script> @code {
[JSInvokable]
public static void OnMouseDown(string rowRenderId)
{
SampleData clickedRow=MyData.FirstOrDefault(i=> i.ID==int.Parse(rowRenderId));
}

public class SampleData
{
public int ID { get; set; }
public string Name { get; set; }
public DateTime HireDate { get; set; }
}

private static IEnumerable <SampleData> MyData=Enumerable.Range(1, 50).Select(x=> new SampleData
{
ID=x,
Name="name " + x,
HireDate=DateTime.Now.AddDays(-x)
});
} Kind Regards, Hristian Kind Regards, Hristian
