# grid for Blazor problem

## Question

**CAR** asked on 29 Jul 2023

Hi, how can I display an age column based on birthdate. I have this code that displays no data in the age column <GridColumn Field="LasName Title="Lase name" /> @Age=DateTime.Now.Year - Person.BirthDateYear <GridColumn Field="Age" Title="Age" /> Age is defined in the @Code section: public int Age; Thanks

## Answer

**Hristian Stefanov** answered on 01 Aug 2023

Hi CARLOS, I've created an example for you, demonstrating how to set an age column calculated from a birthdate column: <TelerikGrid Data="@GridData" Pageable="true" Sortable="true"> <GridColumns> <GridColumn Field="@nameof(Person.FirstName)" Title="First Name" /> <GridColumn Field="@nameof(Person.LastName)" Title="Last Name" /> <GridColumn Field="@nameof(Person.BirthDateYear)" DisplayFormat="{0:yyyy}" Title="Birth Date Year" /> <GridColumn Field="@nameof(Person.Age)" /> </GridColumns> </TelerikGrid> @code {
private List <Person> GridData { get; set; }

protected override void OnInitialized()
{
GridData=new List <Person> ();

var rnd=new Random();
int currentYear=DateTime.Now.Year;
int earliestYear=currentYear - 100;

for (int i=1; i <=30; i++)
{
DateTime birthYear=new DateTime(rnd.Next(earliestYear, currentYear + 1), 1, 1);
GridData.Add(new Person
{
Id=i,
FirstName="Person " + i,
LastName=$"Person {i} Last Name", BirthDateYear=birthYear,
Age=currentYear - birthYear.Year });
}

base.OnInitialized();
}

public class Person
{
public int Id { get; set; }
public string FirstName { get; set; }
public string LastName { get; set; }
public int Age { get; set; }
public DateTime BirthDateYear { get; set; }
}
} Please run and test the above code to ensure it aligns with your requirements. Let me know if you face any further difficulties during the testing phase. Regards, Hristian Stefanov Progress Telerik

### Response

**CARLOS** commented on 01 Aug 2023

Thanks for your help. Didn't think of adding an age property to the class. Thanks for the help and the code. :-)
