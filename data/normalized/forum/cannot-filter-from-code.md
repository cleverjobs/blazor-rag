# cannot filter from code

## Question

**n/an/a** asked on 31 Jan 2022

Hi, I am trying to filter items from code and get this error: cannot implicity convert type 'system.collections.generic.list<telerik.datasource.filterdescritptorbase>' to 'system.collections.generic.icollection<telerik.datasource.ifilterdescriptor>'> Please see code below: private async Task FilterByNameAndWritter() { List<FilterDescriptorBase> filterDescriptorBases=new List<FilterDescriptorBase>(); filterDescriptorBases.Add(new FilterDescriptor() { Member="Name", Operator=FilterOperator.Contains, Value=Name, MemberType=typeof(string) }); filterDescriptorBases.Add(new FilterDescriptor() { Member="Writter", Operator=FilterOperator.Contains, Value=Writter, MemberType=typeof(string) }); GridState<BookDto> gridState=new GridState<BookDto>(); gridState.FilterDescriptors=filterDescriptorBases; // the error comes from here await BookGrid.SetState(gridState); }

### Response

**n/a** commented on 31 Jan 2022

any help would be appreciated. Thank you

## Answer

**Marin Bratanov** answered on 02 Feb 2022

Hello, I recommend you start from the samples in the documentation for filtering the grid from code: for filter menu: [https://docs.telerik.com/blazor-ui/components/grid/filter/filter-menu#filter-from-code](https://docs.telerik.com/blazor-ui/components/grid/filter/filter-menu#filter-from-code) for filter row: [https://docs.telerik.com/blazor-ui/components/grid/filter/filter-row#filter-from-code](https://docs.telerik.com/blazor-ui/components/grid/filter/filter-row#filter-from-code) and if following the same pattern and using the same classes does not help you move forward, I recommend opening a support ticket with a relevant, runnable sample that shows the issue. Regards, Marin Bratanov
