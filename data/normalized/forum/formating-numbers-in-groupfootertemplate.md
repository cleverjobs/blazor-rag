# formating numbers in groupfootertemplate

## Question

**Mau** asked on 02 Mar 2021

Hi, How can I format the resulting data. I want to only show a rounded value. So 10.123456 hours will be 10 hours. Thanks in advance <GridColumn Field="Hours"> <GroupFooterTemplate Context="gridContext"> @{ <div>@gridContext.Sum.ToString()</div> } </GroupFooterTemplate> </GridColumn>

## Answer

**Marin Bratanov** answered on 02 Mar 2021

Hello Maurice, You can use standard .NET format strings and rounding, for example: @* Group by the Team column to see the results and aggregate data in the footer *@<TelerikGrid Data=@GridData Groupable="true" Pageable="true" Height="650px">
<GridAggregates>
<GridAggregate Field=@nameof(Employee.Team) Aggregate="@GridAggregateType.Count" />
<GridAggregate Field=@nameof(Employee.Salary) Aggregate="@GridAggregateType.Max" />
<GridAggregate Field=@nameof(Employee.Salary) Aggregate="@GridAggregateType.Sum" />
</GridAggregates>
<GridColumns>
<GridColumn Field=@nameof(Employee.Name) Groupable="false" />
<GridColumn Field=@nameof(Employee.Team) Title="Team">
<GroupFooterTemplate>
Team Members: <strong>@context.Count</strong>
</GroupFooterTemplate>
</GridColumn>
<GridColumn Field=@nameof(Employee.Salary) Title="Salary" Groupable="false">
<GroupFooterTemplate> Total montly salary ( no decimals ): @context.Sum?. ToString ( " N0 " ) <br />
<span style="color: red;"> Salary sum ( default ): @context.Sum</span>
</GroupFooterTemplate>
</GridColumn>
<GridColumn Field=@nameof(Employee.ActiveProjects) Title="Active Projects">
</GridColumn>
</GridColumns>
</TelerikGrid>

@code { public List<Employee> GridData { get; set; } protected override void OnInitialized ( ) {
GridData=new List<Employee>(); var rand=new Random(); for ( int i=0; i <15; i++)
{
Random rnd=new Random();
GridData.Add( new Employee()
{
EmployeeId=i,
Name="Employee " + i.ToString(),
Team="Team " + i % 3,
Salary=NextDecimal(rand),
ActiveProjects=i % 4==0? 2: 5 });
}
} //taken from and simplified for this examle [https://stackoverflow.com/questions/609501/generating-a-random-decimal-in-c-sharp](https://stackoverflow.com/questions/609501/generating-a-random-decimal-in-c-sharp) decimal NextDecimal ( Random rng ) { byte scale=( byte )rng.Next( 29 ); bool sign=rng.Next( 2 )==1; return new decimal (NextInt32(rng),
NextInt32(rng),
NextInt32(rng),
sign,
scale);
} int NextInt32 ( Random rng ) { int firstBits=rng.Next( 0, 1 <<4 ) <<28; int lastBits=rng.Next( 0, 1 <<28 ); return firstBits | lastBits;
} public class Employee { public int EmployeeId { get; set; } public string Name { get; set; } public string Team { get; set; } public decimal Salary { get; set; } public int ActiveProjects { get; set; }
}
} Regards, Marin Bratanov

### Response

**Maurice** answered on 02 Mar 2021

I had tried this before but sometimes the differences between working and not working are small @context.Sum.ToString("N0") versus @context.Sum?.ToString("N0") Only the ? is the difference

### Response

**Marin Bratanov** answered on 02 Mar 2021

Hi Maurice, The question mark is there because the .Sum field we provide is nullable (like the other fields). It might be null if there isn't a defined aggregate of that type for that field. You can obtain such information from the intellisense: Regards, Marin Bratanov
