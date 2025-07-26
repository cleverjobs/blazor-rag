# Control the TabIndex order of fields in an editform across multiple tabs

## Question

**Joh** asked on 05 Jul 2021

I have an EditForm with a couple fields followed by a TabStrip. Each TabStripTab has multiple fields. The Tabstrip is followed by a final couple of fields and the usual Submit/Cancel buttons. How do I control the sequence of fields if I tab through the form? First couple of fields, fine. TabStripTab it jumps over and goes right to the final fields and buttons. Keyboard tabbing will not enter the TabStrip. How do we get this to work properly?

## Answer

**Nadezhda Tacheva** answered on 08 Jul 2021

Hi John, If a TabStripTab header is focused, as per the TabStrip keyboard navigation setup you are able to move through the tabs with the Up and Down or Left and Right arrows depending on the TabStrip orientation. Once the desired TabStripTab header is focused you can press Tab to focus its content container. The subsequent Tab presses will loop you through the content of the active TabStripTab. At any point you can press Tab + Shift to return the focus to the TabStripTab header and then use the arrows if you want to focus another TabStripTab. I used the below snippet to demonstrate the keyboard navigation behavior in a scenario similar to yours. See the attached video of the result. @using System.ComponentModel.DataAnnotations

<div style="width:400px">
<EditForm Model="@person">
<DataAnnotationsValidator />
<TelerikValidationSummary />
<p>
<label for="NameFieldId">Name</label>
<TelerikTextBox @bind-Value="@person.Name" Id="NameFieldId"></TelerikTextBox>
<TelerikValidationMessage For="@( ()=> person.Name)" />
</p>
<TelerikTabStrip TabPosition="Telerik.Blazor.TabPosition.Top">
<TabStripTab Title="First">
First tab content.
<br />
<TelerikTextBox @bind-Value="@TB1Value"></TelerikTextBox>
</TabStripTab>
<TabStripTab Title="Second">
Second tab content.
<br />
<TelerikTextBox @bind-Value="@TB2Value"></TelerikTextBox>
</TabStripTab>
<TabStripTab Title="Third">
Third tab content.
<br />
<TelerikTextBox @bind-Value="@TB3Value"></TelerikTextBox>
</TabStripTab>
</TelerikTabStrip>
<p>
<label for="AgeFieldId">Age</label>
<TelerikNumericTextBox @bind-Value="@person.Age" Id="AgeFieldId"></TelerikNumericTextBox>
<TelerikValidationMessage For="@( ()=> person.Age)" />
</p>

<TelerikButton ButtonType="ButtonType.Submit">Submit</TelerikButton>
</EditForm>
</div>

@code { public string TB1Value { get; set; } public string TB2Value { get; set; } public string TB3Value { get; set; }

Person person=new Person(); public class Person {
[ Required ] public string Name { get; set; }

[ Required ] public int? Age { get; set; }

[ Required ] public bool IsMarried { get; set; }
}
} I hope you will find the above information useful. If any further questions appear, please do not hesitate to contact us. Thank you for choosing Telerik UI for Blazor! Regards, Nadezhda Tacheva Progress Telerik
