# TelerikComboBox OnRead doesnt fire

## Question

**Evg** asked on 05 May 2021

I'm using TelerikComboBox and came across a problem that when I select a value from the drop-down list and the value changes, the method is not called. <TelerikComboBox Data="@SuggestedEmployees" TItem="@CompanyEmployeeDropDownInfoModel" TValue="string" TextField="Email" ValueField="Email" Placeholder="E-mail" ClearButton="true" Filterable="true" Width="100%" OnRead="@(OnEmailChanged)" @bind-Value="@Email" AllowCustom="true"> <ItemTemplate Context="newContext"> <strong>@((newContext as CompanyEmployeeDropDownInfoModel).FirstName) @((newContext as CompanyEmployeeDropDownInfoModel).LastName) @((newContext as CompanyEmployeeDropDownInfoModel).PhoneNumber)</strong> </ItemTemplate> </TelerikComboBox> At first, SuggestedEmployees is empty. When user inputs more than 3 symbols, we get list of employees and show it to user. Everything works fine, when user manually input symbols, but when user select target employee from list and email changes, nothing happened, OnRead method doesn't trigger. Any suggestion?

## Answer

**Marin Bratanov** answered on 05 May 2021

Hello Evgeny, OnRead is not supposed to fire after an item selection, it fires only when the component initializes or the user filters. In our next release, it will also fire when virtualization is enabled and the user scrolls too. You can read more about it in its documentation: [https://docs.telerik.com/blazor-ui/components/combobox/events#onread](https://docs.telerik.com/blazor-ui/components/combobox/events#onread) If you need to fetch an entire model based on the selected model, the OnRead event is not hte place - ValueChanged or OnChange are, and you can see more details and code samples in this article: [https://docs.telerik.com/blazor-ui/knowledge-base/dropdowns-get-model](https://docs.telerik.com/blazor-ui/knowledge-base/dropdowns-get-model) If this does not help you move forward, I advise that you open a support ticket and send us a small runnable code snippet of what you are trying to do and the Telerik component problem, so we can review and advise. Regards, Marin Bratanov
