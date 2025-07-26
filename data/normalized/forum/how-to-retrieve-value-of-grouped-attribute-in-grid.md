# How to retrieve value of grouped attribute in grid

## Question

**Eth** asked on 16 Jan 2023

Hello, I am trying to set up a GroupFooterTemplate and to calculate a value to put in the footer I need to know the value of the grouped attribute. In this case I am grouping on a column named "Category" and I call a function that needs to know the value of the category column in the group above the footer. If that's not clear here is a screenshot to help illustrate the value I'm trying to find when generating the group footer. So I'm hoping to be able to pull that category value, "Biological" or "Kiln", when generating the group footer which I do by using the code here. <GridColumn Field="@lengthColumnName" FieldType="@typeof(decimal)" Title="@myName" Width="180px"> <GroupFooterTemplate Context="unitFooterContext"> Total: %@calculateSubtotal(lengthColumnName, "Biological").ToString() </GroupFooterTemplate> </GridColumn> Currently it is just hard coded to use Biological but I would like it to be able to use the category column value for each group to generate the correct value in each footer under each group. So ideally there is something I can access from the grid that will correspond to the value of the grouped column at each point where the footer is generated (so some variable that would change between biological, kilns, etc as the grid is created).

## Answer

**Hristian Stefanov** answered on 19 Jan 2023

Hi Ethan, Thank you for sending screenshots that help me see the scenario better. I confirm that you can get the " Category " value in the GridFooterTemplate through the context. Here is how to modify the provided code to make it achieve the desired result: <GridColumn Field="@lengthColumnName" FieldType="@typeof(decimal)" Title="@myName" Width="180px"> <GroupFooterTemplate Context="unitFooterContext"> Total: %@calculateSubtotal(lengthColumnName, unitFooterContext.Value ).ToString() </GroupFooterTemplate> </GridColumn> If we can assist further, I would be glad. Regards, Hristian Stefanov

### Response

**Ethan** commented on 19 Jan 2023

Thank you for your response! I'm getting a compiler error when trying to use unitFooterContext.Value as a string argument. The error states cannot convert method group to string and I can't seem to figure out how to resolve this issue. Am I missing something about how to access unitFooterContext.Value?

### Response

**Hristian Stefanov** commented on 23 Jan 2023

Hi Ethan, I retested the configuration in this REPL sample. It seems that the " unitFooterContext.Value " works as expected. Please run and test it by grouping the " Team " column to see if the result you get is the same. As a next step, use the above sample as a comparison. I would be glad to keep me updated on how things are going.
