# Possible to write a custom filter for a subset of columns?

## Question

**Dou** asked on 07 Apr 2021

I have a wide grid and need to write custom filters for two of the columns. I've implemented this in OnRead but is there a way to do that while allowing the default filter to run for all the other columns or do I need to write custom filters for all columns?

## Answer

**Marin Bratanov** answered on 09 Apr 2021

Hi Doug, The grid uses the first filter descriptor matching a given field to populate its UI. You can read more in the Set Grid Options Through State section of the State article, make sure to check out the second code snippet and its description. So, you can add more filter descriptors or otherwise modify the DataSourceRequest as required by your business logic and keep the grid functioning, you only have to ensure you edit the collection correctly. There is another path you can take - you can add those filters to the DataSourceRequest object only before using it to query the database, not in the grid-related events, but in the backend. Regards, Marin Bratanov Progress Telerik
