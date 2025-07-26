# Force multiselect not to create new row when there is no data

## Question

**Eth** asked on 31 Aug 2022

I have a multiselect component that I'm trying to filter based on the options chosen in another multiselect component that I'm having trouble with. In my code I got the multiselect to only display text for the options I want but there are still empty rows included where I did not display text. I was wondering if there is a way to remove rows that do not have any text or if I'm just going about filtering the multiselect the wrong way. I've included the code below and a picture of the blank rows. <TelerikMultiSelect Class="lightBlueGray col-2" Width="200px" Data="@MonthOptions" @bind-Value="@model.Months"> <ItemTemplate Context="ITContext"> @if (model.Year.Count()> 0)
{
@if (model.Year.ElementAt(0) !="(All)")
{
int validMonth=0;
int i=0;
while (i <model.Year.Count())
{
if (ITContext.Contains(model.Year.ElementAt(i)))
{
validMonth=1;
}
i++;
}
if (validMonth==1)
{
@ITContext
}
}
else
{
@ITContext
}
}
else
{
@ITContext
} </ItemTemplate> </TelerikMultiSelect>

### Response

**Hristian Stefanov** commented on 05 Sep 2022

Hi Ethan, Thank you for attaching a screenshot that helped me illustrate the problem. As far as I understand, the desired behavior is to reduce the options of one MultiSelect based on selected options from another. I reviewed the provided code part, but I will need more parts from the actual configuration to see how it works. However, I still prepared for you an example by carefully following the described scenario - REPL link. The example demonstrates a possible implementation of the above functionality. It uses the ValueChanged event to change the second MultiSelect data (options) list. It also does not contain a template, but it will work the same way. You can run and test it to see the result. If that's not the case, please modify the above example to reproduce/show the problem and send it back (or maybe create a REPL). That will allow me to see the problem first hand and suggest a more suitable approach. I would be glad to keep me updated on the situation.

### Response

**Ethan** commented on 06 Sep 2022

Thank you for taking the time to create that example that was very helpful! I had thought there might be a better strategy for what I wanted to do and I believe what you've shown is what I was looking for. I tried to recreate the same thing but the multiselect aren't able to load the way I set it up. I replicated what I did into a REPL here if you could take a look at it [https://blazorrepl.telerik.com/cGutuqFj02Bodoax14.](https://blazorrepl.telerik.com/cGutuqFj02Bodoax14.)

### Response

**Hristian Stefanov** commented on 09 Sep 2022

Hi Ethan, I'm glad to see that the strategy suits you. I carefully reviewed the latest REPL sample you sent. It seems that you've almost done it yourself. I modified the REPL sample to make it load - REPL link. You can run and test it to see the result. The changes are small - added a new " MonthOptions " instance and changed an " if " condition in the " OnYearSelect " handler. I also left comments on every changed place.

### Response

**Ethan** commented on 09 Sep 2022

Thank you again! I'm not sure why but my application requires that I use "ValueExpression" with my multiselect which ended up fixing the issue but it was helpful to be pointed towards this strategy of handling multiselect boxes in the first place. In case anyone runs into a similar issue I followed this page to fix my problem [https://docs.telerik.com/blazor-ui/knowledge-base/requires-valueexpression.](https://docs.telerik.com/blazor-ui/knowledge-base/requires-valueexpression.) Specifically I added 'ValueExpression="@( ()=> model.Year)"' to my year multiselect box.
