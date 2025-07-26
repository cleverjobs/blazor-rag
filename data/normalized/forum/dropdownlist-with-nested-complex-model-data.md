# DropDownList with nested complex model data

## Question

**Adr** asked on 21 Apr 2021

Hi, Can the DropDownList TextField property access fields on nested objects? For example: 01. <TelerikDropDownList 02. TItem="PersonModel" 03. TValue="int" 04. Data="@Data" 05. ValueField="@nameof(PersonModel.PersonId)" 06. TextField="@nameof(PersonModel.Person.DisplayName)"> 07. </TelerikDropDownList> 08. @code { 09. private IEnumerable<PersonModel> Data { get; set; } 10. 11. protected override Task OnInitializedAsync() 12. { 13. Data=new PersonModel[] 14. { 15. new() { PersonId=1, Person=new Person { FirstName="A", LastName="B"}}, 16. new() { PersonId=2, Person=new Person { FirstName="C", LastName="D"}}, 17. new() { PersonId=3, Person=new Person { FirstName="E", LastName="F"}} 18. }; 19. 20. return base.OnInitializedAsync(); 21. } 22. 23. private class PersonModel 24. { 25. public int PersonId { get; init; } 26. 27. public Person Person { get; init; } 28. } 29. 30. private class Person 31. { 32. public string FirstName { get; init; } 33. 34. public string LastName { get; init; } 35. 36. public string DisplayName=> $"{FirstName} {LastName}"; 37. } 38. }

## Answer

**Marin Bratanov** answered on 21 Apr 2021

Hi Adrian, I expect that all select-type components will get that ability when this is implemented: [https://feedback.telerik.com/blazor/1464290-combobox-support-nested-complex-models.](https://feedback.telerik.com/blazor/1464290-combobox-support-nested-complex-models.) At the moment, I'm afraid that's not possible, you'd have to use the ItemTemplate and ValueTemplate to render complex information (see more about the dropdownlist templates in its docs ). Regards, Marin Bratanov
