# TelerikMultiSelect hide selected items in header

## Question

**Ila** asked on 04 Aug 2022

Is it possible to hide the selected values on top of the control and continue showing the hint?? as it doesn't look so good on narrow control

## Answer

**Hristian Stefanov** answered on 08 Aug 2022

Hi Ilan, I confirm it is possible to hide the selected values. To do so, the easiest way is to use CSS style for " display:none " on the " k-chip " CSS selector. I have prepared an example for you below. Setting the Class parameter allows targeting a specific instance of the component. <style>.my-multiselect.k-chip { display: none;
} </style> <TelerikMultiSelect Class="my-multiselect" Data="@Roles" @bind-Value="@TheValues" AutoClose="false" Placeholder="Write the roles you need"> <ItemTemplate> <input type="checkbox" id="@( " cb " + context.Replace (" ", "") )" class="k-checkbox k-rounded-md k-checkbox-md" checked="@GetChecked(context)"> @context </ItemTemplate> </TelerikMultiSelect> @foreach (var item in TheValues)
{ <div> @item </div> }

@code{
bool GetChecked(string text)
{
return TheValues.Contains(text);
}

List <string> TheValues { get; set; }=new List <string> ();

List <string> Roles { get; set; }=new List <string> {
"Manager", "Developer", "QA", "Technical Writer", "Support Engineer", "Sales Agent", "Architect", "Designer"
};
} Regards, Hristian Stefanov

### Response

**Ilan** commented on 09 Aug 2022

Now it's totally empty, Can I leave the Placeholder?

### Response

**Nadezhda Tacheva** answered on 12 Aug 2022

Hi Ilan, I am stepping in the discussion as my colleague, Hristian, is currently out of office. You may as well consider the summary tag mode which will cover your desired behavior once available. I added your vote to the request to increase its popularity as we prioritize the enhancements based on the community interest and demand. You may also follow it to get notifications on status updates. The admin edit of the post suggests a couple of workarounds you may try for the time being. Take your time to revise them and please let us know if any further questions as raised. Regards, Nadezhda Tacheva
