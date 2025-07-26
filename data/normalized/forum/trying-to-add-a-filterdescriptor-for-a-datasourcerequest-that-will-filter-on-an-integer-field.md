# Trying to add a FilterDescriptor for a DataSourceRequest that will filter on an integer field.

## Question

**Jst** asked on 09 Feb 2023

I'm trying to create a DataSourceRequest that has several filters that I am creating and inserting into a CompositeFilterDescriptor. One of those filters is an integer data type. When I have the DataSourceRequest output the request via "ToODataString()" the integer filter is treated as a string, i.e. surrounded by single quotes. This will then not work in my OData endpoint. How do I specify that this should be an int and not surrounded by single quotes in the output? var request=new DataSourceRequest()
{
PageSize=1,
Skip=0,
Filters=new List<IFilterDescriptor>(),
Sorts=new List<SortDescriptor>(),
Groups=new List<GroupDescriptor>()
}; var cfd=new CompositeFilterDescriptor
{
LogicalOperator=FilterCompositionLogicalOperator.Or
}; var fd=new FilterDescriptor()
{
Value="MyTestValue",
Operator=FilterOperator.Contains,
Member="Status" };
cfd.FilterDescriptors.Add(fd);
request.Filters.Add(cfd); var cfd2=new CompositeFilterDescriptor
{
LogicalOperator=FilterCompositionLogicalOperator.And
}; var fd2=new FilterDescriptor()
{
Value=123456,
Operator=FilterOperator.IsEqualTo,
Member="MyId" };

cfd2.FilterDescriptors.Add(fd2);
request.Filters.Add(cfd2); var query=request.ToODataString(); The "query" then contains something like : (contains(Status,%27MyTestValue%27)%20and%20(MyId%20eq%20%27123456%27)) or (contains(Status,'MyTestValue') and (MyId eq ' 123456 ' )) what I need is (contains(Status,'MyTestValue') and (MyId eq 123456 )) How do I get it to form the correct Odata Url?

## Answer

**Dimo** answered on 14 Feb 2023

Hello John, The FilterDescriptor needs a MemberType: var fd2=new FilterDescriptor()
{
Value=123456,
Operator=FilterOperator.IsEqualTo,
Member="MyId", MemberType=typeof ( int ) }; Regards, Dimo
