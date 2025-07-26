# Virtual Scrolling, Group Load On Demand with ExpandoObject

## Question

**Joh** asked on 08 Oct 2024

The docs/demos use the classic list of Employee class as data source, but what if the data source is an ExpandoObject instead? I've tried a few things, but the expanded group only fetches one row, and sometimes no rows at all. I'd love to hear if anyone has got this working?

## Answer

**Tsvetomir** answered on 11 Oct 2024

Hello Johan, To gather more information on how to bind the Grid component to the Expando object, I recommend referring to our KB article - Bind Grid to Expando Object. The article, also how to use such a Grid configuration with the Load on Demand Groups functionality. I hope the provided information and examples in the article help you to move forward with your requirements. Regards, Tsvetomir Progress Telerik

### Response

**Johan** commented on 12 Oct 2024

I am well aware of those articles, but when I try load groups on demand with a virtual grid but with ExpandoObject, incorrect number of items gets loaded. That's why I asked for an example.

### Response

**Tsvetomir** commented on 16 Oct 2024

Thank you for coming back with feedback. After further observation of the described Grid configuration, I can inform you that the behavior is a known bug, that has already been reported in our

### Response

**Johan** commented on 22 Oct 2024

Ok, that explains. Thanks for getting back on this. I'll look at the linked item. Unfortunately I cannot use a "real" class/object because the result may have one or many columns depending on a search results.

### Response

**Tsvetomir** commented on 25 Oct 2024

Thank you Johan for sharing more information about your scenario. For the time being, the other alternative is to remove the LoadGroupsOnDemand functionality and use regular paging so you can still have grouping.
