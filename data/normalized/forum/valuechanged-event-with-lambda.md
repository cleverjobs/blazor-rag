# ValueChanged event with lambda

## Question

**Jua** asked on 08 Nov 2020

Documentation suggest a lamba expression in ValueChanged event because it's requiered by framewoek, but for me this sentences are equivalent: from the handler: @result <br /> from model: @theTbValue <br /> <TelerikTextBox ValueChanged="@( (string s)=> MyValueChangeHandler(s) )" Value="@theTbValue"></TelerikTextBox> <TelerikTextBox ValueChanged="@MyValueChangeHandler" Value="@theTbValue"></TelerikTextBox> @code { string result; public string theTbValue { get; set; }="lorem ipsum"; private void MyValueChangeHandler (string theUserInput) { result=string.Format("The user entered: {0}", theUserInput); //you have to update the model manually because handling the ValueChanged event does not let you use @bind-Value theTbValue=theUserInput; } }

## Answer

**Kristian** answered on 11 Nov 2020

Hello Juan Angel, The approach you are using is the correct one. Using only lambdas was a limitation in the Blazor framework before but it seems they fixed it with one of the new releases. I changed the documentation and it will go live with our next deploy. Thanks for bringing this up and helping us to improve the documentation. Regards, Kristian
