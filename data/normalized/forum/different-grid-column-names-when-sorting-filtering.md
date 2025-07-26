# Different Grid column names when sorting/filtering

## Question

**Adr** asked on 07 May 2021

Hi, I have inherited a data access layer which uses OrmLite and the database POCOs have been auto generated and it uses the actual database column names as the property names in the POCOs. e.g. person_firstname, person_lastname etc. public class PersonPoco { public string person_firstname { get; set; } public string person_lastname { get; set; }
} Then I'm using AutoMapper to map the POCOs to business objects which in turn are used as the data source for the Telerik Grid. public class PersonBusinessClass { public string Firstname { get; set; } public string Lastname { get; set; }
} So in the Telerik Grid I would bind the columns as so: <GridColumn Field="@(nameof(PersonBusinessClass.Firstname))" Title="First Name" /> <GridColumn Field="@(nameof(PersonBusinessClass.Lastname))" Title="Last Name" /> This causes an issue because when it comes to column filtering/sorting it uses the GridColumn Field value for the database column name which in my case is different, so I end up with errors e.g: Invalid column name 'Firstname' as it should be 'person_firstname'. Invalid column name 'Lastname' as it should be 'person_lastname'. Is there a way to specify a different column name to use for filtering/sorting ?

## Answer

**Marin Bratanov** answered on 07 May 2021

Hi Adrian, The grid "sees" only the object it is bound to and it cannot know what happens in the backedn logic. Thus, it cannot use different names because that would, in turn, break the common case where it works with the models it is provided. If you need to make such changes to the field names and a DTO object is not an option for transferring the data, you should use the mapping tool to change the field names in the DataSourceRequest object the grid gives you before you use it in the backend. Regards, Marin Bratanov
