# Min Max Values

## Question

**Dou** asked on 23 May 2020

Hello: Is there no way to limit the value of a NumericTextBox with a Type of Int32 (or anything other than a decimal value)?

## Answer

**Doug** answered on 23 May 2020

please disregard this post

### Response

**Svetoslav Dimitrov** answered on 25 May 2020

Hello Doug, I am happy to see you managed to resolve that question on your own. For future questions of that sort I am posting two possible solutions (that you can, of course, combine): Using the Min and Max parameters of the component: <TelerikNumericTextBox @bind-Value="@TheValue" Min="-100" Max="10000"> </TelerikNumericTextBox> @code {
public int TheValue { get; set; }
} Using Form Validation: @using System.ComponentModel.DataAnnotations

<EditForm Model="@MyModel">
<DataAnnotationsValidator />
<ValidationSummary />

<TelerikNumericTextBox @bind-Value="@MyModel.TheValue"></TelerikNumericTextBox>

</EditForm>

@code {
MyDataModel MyModel=new MyDataModel(); public class MyDataModel {
[ Range(-100, 1000, ErrorMessage="The number should be between {1} and {2}" ) ] public int TheValue { get; set; }
}
} Regards, Svetoslav Dimitrov
