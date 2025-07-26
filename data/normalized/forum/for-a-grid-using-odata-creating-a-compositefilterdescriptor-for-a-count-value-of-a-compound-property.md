# For a grid using Odata creating a CompositeFilterDescriptor for a count value of a compound property?

## Question

**Jst** asked on 09 Jan 2023

I have a grid that I am filling using an OData endpoint. To this, I would like to add a CompositeFilterDescriptor or a filter that only retrieves records that have at least a count of> 0 for a child collection of the parent data. i.e. MyClass{ public int Id { get; set;} public List<Flag> Flags { get; set;}
} I want to bring back all records that have at least one flag record in the Flags collection. I am able to manually add the filter to the url and retrieve the object but when I try to add a filter via the DataSourceRequest it treats the>0 as a string character and tries to surround it with double quotes.

## Answer

**Dimo** answered on 12 Jan 2023

Hi John, Our filter descriptors can work with several different filter operators. Alas, a count condition is not among them, as this is not a condition that you can evaluate against a single primitive value. The other requirement for the built-in filtering is to work for primitive types. You will need to add this count condition manually to the OData request URL to retrieve the desired records. (P.S. Or, populate the Flags count value as a property of the MyClass data item.) Regards, Dimo
