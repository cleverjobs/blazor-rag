# Define ComboBox value type when using custom values

## Question

**Rom** asked on 25 Aug 2021

Hello According to the Telerik Blazor Combobox documentation, it is not possible to have e.g. decimal values when I want to use AllowCustom="true": The ComboBox provides the following features: AllowCustom - whether the user can enter custom values. If enabled, the ValueField must be a string. In my application it would be great to have the option to allow custom values, but decimal only. I've seen this for e.g. NumericTextBox. There is a parameter "T" where one can define the type of the value. Here you can see an example code extracted from my application: <TelerikComboBox Data="@Data" @bind-Value="@SelectedValue" TextField="Value" ValueField="Value" AllowCustom="true" Placeholder="Select a value or set a custom value"> </TelerikComboBox> public List<MyData> Data { get; set; } public decimal SelectedValue { get; set; } public class MyData { public decimal Value { get; set; }
} Is there already such a feature and I simply didn't see it or is this really not possible and never will be? Best Regards, Roman

## Answer

**Marin Bratanov** answered on 28 Aug 2021

Hello Roman, The numeric textbox has a type parameter because it can take different types such as int, decimal, float, etc., and the rules for working with them and what should render, and how steps are handled vary greatly between them. On the other hand, the combo box is a text input - there is a plain textbox in it that filters and highlights items based on an arbitrary string. The fact that this string may contain only numbers is a specific corner case, but the common case is that this is a string. The Value and thus ValueField are a unique identifier in case you use more complex model whose string representation the users chooses by (say, a collection of mailing addresses that has a name like "HR" or "Security Taskforce" who have real IDs behind the scenes). This works in the common case bacause the UI uses the string in the input and in the TextField to match those items, and the Value can be populate with the matching ValueField. Custom Values changes that because: The user input is always a string (explained why above - mostly this has to match the TextField). This input, this string, must now be something that can go into the Value - this means that the Value must also be a string (and, by extension, the ValueField). You can consider using the ValueChanged event to try to parse the number and if it can't be parsed, show a message to the user and avoid updating the view model. The view-model will still require a string that the backend will have to parse to get the real number too. So, to summarize, custom values will always be strings. Regards, Marin Bratanov Progress Telerik
