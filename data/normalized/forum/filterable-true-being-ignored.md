# Filterable="true" being ignored

## Question

**Dea** asked on 21 Oct 2024

Hi, are there any restrictions on when Filterable="true" will be respected on a grid column? I have a grid where I can't filter on one particular column - the Id. Anything it could be?

### Response

**Dean** commented on 21 Oct 2024

I have tried it with and without the Locked property being true, and as a string as well as an int

## Answer

**Tsvetomir** answered on 22 Oct 2024

Hi Dean, Thank you for the attached screenshots. By design, the Grid SearchBox searches in all visible columns that are bound to string fields because it uses the " contains " filter operator. Thus, achieving the desired search result requires a more custom approach. In short, the solution relies on Grid filter descriptors and Grid State. To gather more detailed information about it and see an example firsthand, I recommend referring to our KB article: Search Grid in numeric and date fields. On the other hand, if the " Id " field is a property of type string, the default SeachBox filtering works as expected. To demonstrate that, I've prepared a REPL example. Please run it on your side, and let me know if that is the result you are looking for. On a side note, the Filterable="true" is not required here, because the default value of the parameter is " true ". Also, the Locked parameter value has no relation with the filtering functionality, so it can't compromise the search result. I hope the provided information serves you well. Look forward for your reply. Regards, Tsvetomir Progress Telerik
