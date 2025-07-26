# Error while adding Min and Max values in TelerikNumericTextBox

## Question

**Anj** asked on 02 Dec 2020

<TelerikNumericTextBox Min="0" Max="100" @bind-Value=@Model.HeadSkip Id="header_skip"></TelerikNumericTextBox> After adding the Minimum and Maximum value it shows an error as below The type arguments for method 'TypeInference.CreateTelerikNumericTextBox_0<T>(RenderTreeBuilder, int, int, T, int, T, int, string, int, T, int, EventCallback<T>, int, Expression<Func<T>>)' cannot be inferred from the usage. Try specifying the type arguments explicitly. The binding value is of type short and I am trying to restrict the negative numbers in numeric textbox.

## Answer

**Svetoslav Dimitrov** answered on 03 Dec 2020

Hello Anju, What I suspect is happening is that the Model.HeadSkip is a string value, whereas you should bind the value of the component to a numeric type. Below, you could see two code snippets, the first where the error is reproducible and the @bind-Value is bound to a string, and the second one (where it is not) - the @bind-Value is bound to an integer. You can find more information on the suitable data types for the component from this documentation article. Reproducible example: <TelerikNumericTextBox Min="0" Max="100" @bind-Value="@NumericValue" Id="header_skip"></TelerikNumericTextBox>

@code { public string NumericValue { get; set; } } Working example: <TelerikNumericTextBox Min="0" Max="100" @bind-Value="@NumericValue" Id="header_skip"></TelerikNumericTextBox>

@code { public int NumericValue { get; set; } } Does this help you move forward with your application? If it does not you can follow up on this thread. Regards, Svetoslav Dimitrov

### Response

**Anju** answered on 03 Dec 2020

Headskip is of Type Short

### Response

**Svetoslav Dimitrov** answered on 03 Dec 2020

Hello Anju, Since our 2.6.0 release, we support the short type for the NumericTextBox. What is happening that the types are different - for the Min and Max you provide integers (0 and 100). You could use the example below as a base to implement it in your own project. <TelerikNumericTextBox Min="@((short)0)" Max="@((short)100)" @bind-Value="@NumericValue" Id="header_skip"> </TelerikNumericTextBox> @code {
public short NumericValue { get; set; }
} Regards, Svetoslav Dimitrov

### Response

**Anju** answered on 03 Dec 2020

Thank you! Its Worked :)
