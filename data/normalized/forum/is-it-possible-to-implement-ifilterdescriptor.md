# Is it possible to implement IFilterDescriptor?

## Question

**Ale** asked on 22 Mar 2022

I have experience with Linq Expressions and like to implement my own. The gridState.FilterDescriptors.Add method accepts anything of interface IFilterDescriptor. However, when I give it my own implementation of IFilterDescriptor, it compiles fine but then throws an error during runtime: System.InvalidCastException: 'Unable to cast object of type 'MyFilterDescriptor' to type 'Telerik.DataSource.FilterDescriptor'.' I thought to inherit Telerik.DataSource.FilterDescriptor and Telerik.DataSource.CompositeFilterDescriptor and override the CreateFilterExpression method, but that didn't work either, as it always ends up calling the method in the base FilterDescriptor. Is this by design, or is there a way now or in the future to implement my own IFilterDescriptor? Thanks.

### Response

**Dimo** commented on 24 Mar 2022

Hello Alex, The IFilterDescriptor interface provides some abstraction and flexibility for developers when they filter the Grid programmatically. In general, the Grid works with FilterDescriptors or CompositeFilterDescriptors, depending on the filtering scenario. In your case, you can download and review the source code. It may give you ideas how to proceed, or even how to rebuild it, so that it suits your requirements. I could provide more information if you tell me: How exactly are you trying to inherit the classes and override their methods - send the code. What are you trying to achieve, which is not possible with the built-in filter descriptors? Regards, Dimo Progress Telerik

### Response

**Alex** commented on 28 Mar 2022

Hello Dimo, Thanks a lot for your response. I prefer to not rebuild the source code, as that will make it harder for me to upgrade to new builds. I tried implemtning the IFilterDescriptor interface, and I got a runtime error saying the class is not FilterDescriptor. I also tried to create a class inherting from FilterDescriptor and Telerik ended up calling the base class method and not mine. My exact use case is to create a new filter descriptor that gets a list of values and only shows rows where a specific column has any of those values. I tried implementing this indirectly using the ContainsAny but that was too slow to be practical (I have tens of thousands of values), as it seems the internal implementation does not use a hash table. My implementation would use HashSet to make a very fast ContainsAny filter. Thanks, Alex

### Response

**Dimo** commented on 28 Mar 2022

Thanks for the follow-up, Alex. Different places in our code depend on the type of the filter descriptor object and its properties. That's why we expect it to be either FilterDescriptor or CompositeFilterDescriptor. Based on my discussion with the developers, it's not trivial or very likely for us to expose the ability to use custom filter descriptor types. If source code modification is not an option, then these are the remaining alternatives: use a different implementation for data operations, instead of . ToDataSourceResult () pre-filter the data outside the Grid and then call . ToDataSourceResult () without the filters that hinder performance
