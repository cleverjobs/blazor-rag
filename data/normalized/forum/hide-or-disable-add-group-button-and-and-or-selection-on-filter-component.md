# Hide or disable "Add Group" button and "And/Or" selection on Filter component

## Question

**Joh** asked on 05 Jun 2024

For my use case the logical operator will always be "And" and there is no grouping. I'd like to hide those buttons to avoid confusing end users. Is that possible?

## Answer

**Tsvetomir** answered on 10 Jun 2024

Hello John, Thank you for the provided screenshot and clear explanation of the expected layout of the Filter component. To hide the buttons in the Filter, override the default theme style of the component with the following CSS approach: <style>.custom-filter.k-toolbar-button-group { display: none;
}.custom-filter button:nth-child ( 3 ){ display: none;
} </style> @using Telerik.DataSource <TelerikFilter @ref="FilterRef" @bind-Value="@FilterValue" Class="custom-filter"> <FilterFields> <FilterField Name="@(nameof(Person.EmployeeId))" Type="@(typeof(int))" Label="Id"> </FilterField> <FilterField Name="@(nameof(Person.Name))" Type="@(typeof(string))" Label="First Name"> </FilterField> <FilterField Name="@(nameof(Person.AgeInYears))" Type="@(typeof(int))" Label="Age"> </FilterField> </FilterFields> </TelerikFilter> @code {

private TelerikFilter? FilterRef { get; set; }

private CompositeFilterDescriptor FilterValue { get; set; }=new CompositeFilterDescriptor();

public class Person
{
public int EmployeeId { get; set; }

public string Name { get; set; }=string.Empty;

public int AgeInYears { get; set; }
}
} I hope the provided approach helps you to move forward with your requirements. If you face any difficulties with it, let me know. Regards, Tsvetomir Progress Telerik
