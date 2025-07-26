# Display after picking choice

## Question

**Cha** asked on 22 Sep 2020

I want to use an auto complete for selecting an item from an object. I'm using the item template and setting the value to a string. When selecting the name, which is 2 properties on the object it puts the id in the text box. How do I get the name to display while still using the id as the selected value? 01. @page "/test" 02. 03. <h3>Test</h3> 04. <TelerikAutoComplete Data="@users" ValueField="@(nameof(TestUser.Id))" @bind-Value="@userId"> 05. <ItemTemplate Context="user"> 06. @user.FirstName @user.LastName 07. </ItemTemplate> 08. </TelerikAutoComplete> 09. <button class="btn btn-primary edit-btn" @onclick="@Test">Test</button> 10. 11. @code { 12. 13. private List<TestUser> users; 14. private string userId; 15. 16. protected override Task OnInitializedAsync() 17. { 18. users=new List<TestUser>(); 19. users.Add(new TestUser { Id=1, FirstName="John", LastName="Smith" }); 20. users.Add(new TestUser { Id=2, FirstName="Jane", LastName="Doe" }); 21. users.Add(new TestUser { Id=3, FirstName="Olivia", LastName="Williams" }); 22. users.Add(new TestUser { Id=4, FirstName="Noah", LastName="Jones" }); 23. 24. return base.OnInitializedAsync(); 25. } 26. 27. async Task Test() 28. { 29. Console.WriteLine(userId); 30. } 31. 32. public class TestUser{ 33. 34. public int Id { get; set; } 35. public string LastName { get; set; } 36. public string FirstName { get; set; } 37. } 38. }

## Answer

**Marin Bratanov** answered on 22 Sep 2020

Hello Charles, I'd recommend using the ComboBox for that, here's an example of using one field to show the text, and another to use as a value identifier: [https://docs.telerik.com/blazor-ui/components/combobox/data-bind#bind-to-a-model](https://docs.telerik.com/blazor-ui/components/combobox/data-bind#bind-to-a-model) The autocomplete is a plain text input, think of it as a simple <input type=text> but where you (the application developer) control the autocomplete options instead of the browser. Regards, Marin Bratanov

### Response

**Charles** answered on 22 Sep 2020

Can you filter it as the user types? We may have 100+ users which is why I chose autocomplete.

### Response

**Marin Bratanov** answered on 22 Sep 2020

Yes, you can, you can check it out in this demo: [https://demos.telerik.com/blazor-ui/combobox/filtering](https://demos.telerik.com/blazor-ui/combobox/filtering) Here are some more docs on the matter: filtering: [https://docs.telerik.com/blazor-ui/components/combobox/filter](https://docs.telerik.com/blazor-ui/components/combobox/filter) custom filtering on demand through the OnRead event: [https://docs.telerik.com/blazor-ui/components/combobox/events#onread](https://docs.telerik.com/blazor-ui/components/combobox/events#onread) Regards, Marin Bratanov
