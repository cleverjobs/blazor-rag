# multiple values in a cell

## Question

**n/an/a** asked on 07 Mar 2022

Hello, I have a model to serve as data in a grid. Besides regular single field data, like strings and numbers etc, the model also contains a List of multiple subitems which need to be added to each row, in a cell. My grid would look like this: FirstFieldName SecondFieldName ListOfItemsField ------------------------------------------------------------------------------------------------ DataForItemOne DataForItemOne SubItemOneOfItemOne SubItemTwoOfItemOne SubItemThreeOfItemOne ------------------------------------------------------------------------------------------------ DataForItemTwo DataForItemTwo SubItemOneOfItemTwo SubItemTwoOfItemTwo SubItemThreeOfItemTwo ----------------------------------------------------------------------------------------------- etc etc etc etc. My question is: how am I able to add multiple values into a cell? As mentioned, the values belong to a List contained by the model. Each model in the table would have its own List of subitems. Thank you very much. Kind regards

## Answer

**Nadezhda Tacheva** answered on 08 Mar 2022

Hi Astig, You can use Column Template for the ListOfItemsField. Through its context you can get the field holding the subitems collection, loop through it and render the subitems in the desired way. Here is a runnable example demonstrating this approach - [https://blazorrepl.telerik.com/GGuHEClc31GigOy707.](https://blazorrepl.telerik.com/GGuHEClc31GigOy707.) I am simply creating an <ul> with the available addresses for every Grid record. You can use that as a base to setup the Grid in your application. Please let us know if any further assistance is needed in the meantime. Apart from this approach, there is also another option for displaying hierarchical data in the Grid. Its Detail Template allows you to render a child Grid for the subitems. You may check it and see if it could be a better fit for your use case. Regards, Nadezhda Tacheva Progress Telerik

### Response

**n/a** commented on 08 Mar 2022

Got it! Thank you very much Nadezhda, that's very helpful
