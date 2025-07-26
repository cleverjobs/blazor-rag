# Playwright Testing get TelerikTextArea Value

## Question

**Her** asked on 21 Mar 2025

Hi, I am creating E2E testing using Playwright , but I am having issues getting the value of the textearea. As you can see on the screenshot below when using the playwright code generator it picks the label "This project is unique because..." but I want the Value "test user 5.1" , looking at he HTML generated the value "test user 5.1" is not there , how do I get the value ? I also tried using the data-testid tag on the components but it wont work . <TelerikTextArea data-testid="test1" @bind-Value="@extendedData.UniqueBecause" MaxLength="1000" Rows="3"> </TelerikTextArea> What's the best recommendation to test using Playwright ? Thanks .

## Answer

**Anislav** answered on 21 Mar 2025

I think that the root cause of the issue is that you cannot select a <textarea> by its value (text) using something like a CSS selector. This is not a limitation of Telerik components but rather how HTML and selectors work. Since Telerik components do not support the data-testid attribute directly, you won't be able to use it on the <textarea> itself. However, you can wrap the TelerikTextArea inside an HTML element like a <span> or <div> with a data-testid attribute and then target that wrapper element in Playwright. Additionally, TelerikTextArea component supports Id and Class attributes. You can assign values to these attributes and use them to locate the element in your Playwright E2E tests. Regards, Anislav Atanasov

### Response

**Hernando** commented on 21 Mar 2025

Hi , Thanks for your answer , yes I can use the Id to tag components , is Id supported by all components ?

### Response

**Anislav** commented on 21 Mar 2025

I believe that Telerik's BaseComponent is at the root of the inheritance hierarchy and defines the Class property. Then most components inherit from a more specialized base component (e.g., [https://www.telerik.com/blazor-ui/documentation/api/telerik.blazor.components.common.telerikinputbase-1](https://www.telerik.com/blazor-ui/documentation/api/telerik.blazor.components.common.telerikinputbase-1) ), which adds an Id parameter. Therefore, all components should have the Class parameter, and most should also have an Id. At the moment, I can't think of any component that lacks an Id parameter, but there may be some exceptions. Regards, Anislav Atanasov
