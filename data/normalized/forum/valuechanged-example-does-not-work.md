# ValueChanged example does not work

## Question

**BobBob** asked on 30 Sep 2020

I am following the example for the ValueChanged event with setting an initial value and it does not work. I get the error that ValueExpression is required. I try putting that in, but now when I click on the numeric textbox, Below is the code in your documentation for the example from the handler: @result <br /> from model: @theTbValue <br /> <TelerikNumericTextBox Value="@theTbValue" ValueChanged="@( (decimal v)=> MyValueChangeHandler(v) )"></TelerikNumericTextBox> @code { string result; decimal theTbValue { get; set; }=1.2345m; private void MyValueChangeHandler(decimal theUserInput) { result=string.Format("The user entered: {0}", theUserInput); //you have to update the model manually because handling the ValueChanged event does not let you use @bind-Value theTbValue=theUserInput; } }

## Answer

**Marin Bratanov** answered on 01 Oct 2020

Hello Bob, I just tried this on a new project with 2.17.0 and it works fine for me. The error about a value expression being required is something that comes from the framework and happens when you nest the component in forms, and you can read more about it here: [https://docs.telerik.com/blazor-ui/knowledge-base/requires-valueexpression](https://docs.telerik.com/blazor-ui/knowledge-base/requires-valueexpression) Regards, Marin Bratanov

### Response

**Bob** answered on 01 Oct 2020

Got it, I am in an EditForm. Thanks for the info. Also, thanks for all the quick responses to my questions.
