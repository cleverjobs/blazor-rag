# Pass "Data" parameter for a TelerikGrid encapsulated in a component

## Question

**NiV** asked on 25 Aug 2023

Good morning. I've encapsulated a TelerikGrid in a component. I would like to pass to this component the "Data" parameter to be assigned to the encapsulated TelerikGrid. I haven't found which type to define for the parameter "Data" to be received. Example of TelerikGrid encapsulated in the component, I would like to know what type must be the parameter " ReceivedDataParameter". (I've put ??? in the code to show the information I need). Thank you. <TelerikGrid Data=@ReceivedDataParameter> </TelerikGrid> @code {
[Parameter]
public ??? ReceivedDataParameter { get; set; };
}

### Response

**Nikita** commented on 14 Nov 2023

Hi, did you manage to encapsulate the GridColumns component, too? If so, could you tell how?

### Response

**NiV-L-A** commented on 14 Nov 2023

Currently I've not tried yet. I've understood that is needed to use "typeparam" in the component to have a generic data to pass and "renderfragment" to inject in the component the razor part of the rows, I think I'll try in the next days.

## Answer

**Hristian Stefanov** answered on 30 Aug 2023

Hi Fabio, I confirm that the appropriate " ReceivedDataParameter " type is a collection housing models of the same type employed by the Grid. I have prepared an example for you in this REPL link to demonstrate. Please run and test it to see whether the result suits your needs. Regards, Hristian Stefanov Progress Telerik

### Response

**NiV-L-A** commented on 31 Aug 2023

Thank you for the example, anyway I need to pass to the encapsulated grid a different data type for each page, so the type of the "ReceivedDataParameter" (taken from your repl link example) is not known by the component. In other words, the grid is encapsulated in a component because the intention is to use this component in each page, passing to the component a different data model (parameter "ReceivedDataParameter") depending by the data that must be shown in the grid in that page. This way I can centralize in the component the generic grid settings (say "Sortable=true") so they are not repeated in each page. I was thinking to create a class library to generate the html of the grid and then use it in the page as a renderfragment, this way I can control what to put in the "Data" parameter of the grid (passing the string that contains the model name to the class library that generates the renderfragment and will also populate the bounded "<GridColumns>" in which I need to put the name of the model's fields). I think I'll go this way to centralize the grid generation (using renderfragment), if there are suggestions please add. Thank you.

### Response

**Hristian Stefanov** commented on 01 Sep 2023

Hi Fabio, Thank you for providing me with feedback. I appreciate your effort in helping me understand the scenario better. I confirm that the approach you've presented, involving the creation of a class library to generate the HTML for the Grid and subsequently utilizing it as a render fragment on the page, is indeed a valid solution. However, I'd like to propose an alternative approach for your consideration, which you may like as well - use ExpandoObject with dynamic columns. Kind Regards, Hristian
