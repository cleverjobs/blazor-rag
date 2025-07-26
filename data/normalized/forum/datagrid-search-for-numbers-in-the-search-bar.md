# DataGrid: Search for numbers in the search bar

## Question

**Mar** asked on 05 Jan 2022

I read the documentation for the grid search bar and it says you can only search for string. There must be a workaround (: Should I convert numbers to strings? I only want to search for integers, not decimal numbers.

## Answer

**Nadezhda Tacheva** answered on 06 Jan 2022

Hi Martin, Yes, currently the SearchBox is designed to work with all visible string columns. We have an opened feature request for allowing the SearchBox to work with other data types which I can see you already voted for. In case you haven't, you may also follow it as this is the best way to keep in track with its progress - once its status changes in the portal, you will automatically receive an email notification. For the time being, you can indeed convert the numbers to strings when passing the Grid data. Thus, the Grid will treat them as strings and they will be included in the SearchBox filtering. An important point to take into consideration in this case is that when the numbers are treated as strings, they will behave as such and this will affect other operations - such as sorting, filtering (in case you have enabled them in the Grid). For example, if you have numbers 1 to 20 and you sort them in ascending order, you will get the following outcome in the two cases: If they are threated as numbers, the sorted result will be - 1, 2, 3, 4, 5, 6, 7... If they are treated as strings, the sorted result will be - 1, 10, 11, 12, 13, 14... In regards to filtering, if the numbers are converted to strings, the default filter input will be a TextBox (the default one for string fields by design) instead of a NumericTextBox as for number fields. If you do not consider such differences to be obstacles in your use case, you can proceed with this approach by the time the feature is available. I hope you will find this information useful. Please let us know if any further questions appear. Regards, Nadezhda Tacheva
