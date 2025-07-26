# Components with Javascript turned off

## Question

**Bil** asked on 20 Mar 2020

Will a Visual Studio created project using the Telerik extensions still require javascript to run in the browser. I'm trying this out with the server-hosted Blazor project and it does not seem to carry out the button action when Javascript is turned off. The following code is what is running on the Index.razor page in the generated app. -------------------------------------------------------------------------------------------------------------------------------------------------------- <TelerikButton OnClick="@SayHelloHandler" Primary="true">Say Hello</TelerikButton> <br /> @helloString @code { MarkupString helloString; void SayHelloHandler() { string msg=string.Format("Hello from <strong>Telerik Blazor</strong> at {0}.<br /> Now you can use C# to write front-end!", DateTime.Now); helloString=new MarkupString(msg); }

## Answer

**Marin Bratanov** answered on 20 Mar 2020

Hello Bill, You can't use Blazor without JS, the framework itself relies on it. Thus, our components rely on it as well. Regards, Marin Bratanov
