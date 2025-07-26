# How to set the Width of the input text box

## Question

**Den** asked on 20 Aug 2020

We are trying out the Telerik controls and in my scenario I want the width of the AutoComplete input box to be, say 80% of the page. Now I saw in browser Debug view that there seems to be a hardcoded width of 300px in the elements style? Is that correct? How can I change that?

## Answer

**Marin Bratanov** answered on 20 Aug 2020

Hi Denis, While there is a default value for the width (300px), this does not prevent you from setting your own (you may, by the way, find the Dimensions article useful): User input: @TheValue <br /> <TelerikAutoComplete Data="@Suggestions" @bind-Value="@TheValue" Width="80%" Placeholder="Enter your role (can be free text)" ClearButton="true" /> @code{
string TheValue { get; set; }

List <string> Suggestions { get; set; }=new List <string> {
"Manager", "Developer", "QA", "Technical Writer", "Support Engineer", "Sales Agent", "Architect", "Designer"
};
} Regards, Marin Bratanov

### Response

**Denis** answered on 20 Aug 2020

Thank you. I must have missed this attribute is available.
