# Using DataSourceRequest is there an example of using Aggregates and Groups?

## Question

**Jst** asked on 10 Aug 2021

I am trying to use DataSourceRequest to query a table with a joined table to bring back a total count for each joined item in the second table. i.e. Notes joined to NoteTypes Is there an example of how to use the DataSourceRequest to access an OData api and get a count of each item that is joined to records in the second table? This works but now I need to add in grouping and counts. var request=new DataSourceRequest()
{
Page=0,
Skip=0,
Filters=new List<IFilterDescriptor>(),
Sorts=new List<SortDescriptor>(),
Aggregates=new List<AggregateDescriptor>(),
Groups=new List<GroupDescriptor>()
};
request. Filters. Add( new FilterDescriptor() { Member="AssignedToUser", Operator=FilterOperator. Contains, Value=CurrentUserName, MemberType=typeof ( string ) });
request. Filters. Add( new FilterDescriptor() { Member="IsActive", Operator=FilterOperator. IsEqualTo, Value=true, MemberType=typeof ( bool ) });
request. Filters. Add( new FilterDescriptor() { Member="IsResolved", Operator=FilterOperator. IsEqualTo, Value=false, MemberType=typeof ( bool ) }); var results=await NotesService. GetNotesAsync(request);

## Answer

**Marin Bratanov** answered on 10 Aug 2021

Hi, The purpose of this class (together with a few others) is to return data for Telerik components based on their needs. Its input is effectively an IEnumerable, and it does not do database-level join or count operations. You can read more about what the DataSource package we offer does here: [https://docs.telerik.com/blazor-ui/common-features/telerik-datasource-package.](https://docs.telerik.com/blazor-ui/common-features/telerik-datasource-package.) Aggregates simply describe over which fields to perform aggregations (like sum, count) and that depends on the groups, but that still starts from the simple flat source. Regards, Marin Bratanov
