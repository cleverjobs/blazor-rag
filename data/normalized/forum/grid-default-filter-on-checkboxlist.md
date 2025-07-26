# Grid : Default filter on CheckBoxList

## Question

**Que** asked on 08 May 2024

Hello, I have a grid filterable with one column with FilterMenuType.CheckBoxList. I initialize a defaut filter with OnStateInit which work fine. But when I change the filter by selecting "Select all", nothing is return. It only work when I clear the filter first. I reproduce the issue here : [https://blazorrepl.telerik.com/GokJaiFR56kNGYBW07](https://blazorrepl.telerik.com/GokJaiFR56kNGYBW07) Am I doing something wrong with the default filter or is it a bug? I can't find anything related. Thanks in advance

## Answer

**Nansi** answered on 13 May 2024

Hi Quentin, Thank you for the runnable code example. The CompositeFilterDescriptors have a collection of FilterDescriptors and a LogicalOperator. The default LogicalOperator is And, which in the described case is not working. Please set the LogicalOperator to Or. I added it in the example and now the change in the filter is working as expected. Here is the updated REPL example. Regards, Nansi Progress Telerik

### Response

**Quentin** commented on 14 May 2024

Hi Nansi, Tanks for the answer, it works fine now! Kind regards, Quentin
