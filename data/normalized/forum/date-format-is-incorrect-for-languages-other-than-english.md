# Date Format is incorrect for languages other than English

## Question

**Kis** asked on 20 Jan 2022

Hello there, In my Application, I use Telerik Blazor, Localization and Globalization there is a Date field, I Display date based on culture but something is wrong with the Date field other than English here is my code <Template> @((context as User).BirthDate.Value.ToShortDateString()) </Template> see this attached screenshot for your reference.

### Response

**Dimo** commented on 20 Jan 2022

KIshan, ToShortDateString () depends on general app globalization. Please refer to the Microsoft article. Other than that, you can also see our globalization docs.

### Response

**Kishan** commented on 21 Jan 2022

yeah! you are right, but I am using the Telerik grid where the date filter shows the date format-based culture selected as looks like in the attached image. the column of the date data format is displayed wrong. can you please let me know how can fix this issue
